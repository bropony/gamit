"""
* @name db2json.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/10 20:04
*
* @desc db2json.py
"""

from optparse import OptionParser
import sys
import os
import re
import datetime
import MySQLdb
import json

print("Encoding: ", sys.getdefaultencoding())

def toCamel(src, cap):
    tags = re.split(r'_', src)
    flag = 0 if cap else 1

    tags[flag:] = [t.capitalize() for t in tags[flag:]]
    return "".join(tags)

def table2json(name, fields, data, outdir):
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    res = []
    jsFile = os.path.join(outdir, name + ".json")
    fields = [toCamel(field[0], False) for field in fields]
    fieldSize = len(fields)
    for rec in data:
        js = {}
        for i in range(fieldSize):
            if not rec[i]:
                continue

            if isinstance(rec[i], datetime.datetime) or isinstance(rec[i], datetime.date):
                js[fields[i]] = rec[i].strftime("%Y-%m-%d %H:%M:%S")
            else:
                js[fields[i]] = rec[i]
        res.append(js)

    fout = open(jsFile, "w", encoding='utf-8')
    json.dump(res, fout, indent="    ", ensure_ascii=False, sort_keys=True)
    fout.close()

def table2Java(name, data, outdir):
    if not os.path.exists(outdir):
        print("{} not exists".format(outdir))
        return

    javaFile = open(os.path.join(outdir, "TErrorConfigEnum.java"), "w")

    javaFile.write("package message;\n")
    javaFile.write("\n")
    javaFile.write("public class TErrorConfigEnum{\n")

    for rec in data:
        name = rec[1]
        code = rec[0]
        desc = rec[2]
        javaFile.write("    static public final int {} = {}; // {}\n".format(name, code, desc))
    javaFile.write("}\n")

def main():
    parser = OptionParser()
    parser.add_option("-H", "--host", help="database host. Default:localhost",
                      dest="host")
    parser.add_option("-P", "--port", help="port of database host. Default: 3306",
                      dest="port", type="int")
    parser.add_option("-d", "--database", help="database. Always required", dest="database")
    parser.add_option("-u", "--user", help="username. Default: root", dest="username")
    parser.add_option("-p", "--passwd", help="passwords. Always required", dest="passwd")
    parser.add_option("-o", "--out-dir", help="output dir of generated json files. Default: working dir",
                      dest="outDir")
    parser.add_option("-t", "--table", dest="tables", action="append",
                      help="Table to deal with. By default, all tables are dealt with. "
                           "Multi-assignation is allowed.")
    parser.add_option("-e", "--error-to-java", help="outdir for generating java file for t_error_config.",
                      dest="errorToEnum")

    options, args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return

    host = options.host or "localhost"
    port = options.port or 3306
    database = options.database or ""
    username = options.username or "root"
    passwd = options.passwd or ""
    outDir = options.outDir or "."
    tables = options.tables or []
    errorToEnum = options.errorToEnum or False

    if not database:
        print("database is not specified")
        sys.exit()

    conn = MySQLdb.connect(host=host, user=username, passwd=passwd, db=database, port=port, charset='utf8')
    cursor = conn.cursor()
    # cursor.execute("SET NAMES utf8")

    cursor.execute("show tables")
    __tables = []
    for t in cursor.fetchall():
        __tables.append(t[0])

    if not tables:
        tables = __tables
    else:
        for t in tables:
            if t not in __tables:
                print("table {} is not found.".format(t))
                sys.exit()

    print("Starting jobs")
    for t in tables:
        cursor.execute("desc {}".format(t))
        fields = cursor.fetchall()
        cursor.execute("select * from {}".format(t))
        data = cursor.fetchall()

        print("Dealing with '{}'".format(t))
        table2json(t, fields, data, outDir)

        if errorToEnum and t == "t_error_config":
            table2Java(t, data, errorToEnum)

    print("All jobs done...")

if __name__ == "__main__":
    main()