"""
* @name gmt2java.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/16 15:01
*
* @desc gmt2java.py
"""

import sys
import os.path
import re
import datetime
from optparse import OptionParser

from gmtloader.loader import *
from gmtloader.structmanager import StructManager

class Gmt2Java:
    @staticmethod
    def raiseExcept(what):
        raise Exception(what)

    def __init__(self, structManager, loader, enableJson):
        self.structManager = structManager
        self.loader = loader
        self.indent = 0
        self.fjava = None
        self.filename = ""
        self.scopes = []
        self.isJsonEnabled = enableJson
        if self.isJsonEnabled:
            print(".........JsonEnabled............")

        self.registTypeList = []

    @staticmethod
    def _getIndent(indent):
        if not indent:
            return ""

        return "    " * indent

    def getIndent(self):
        return self._getIndent(self.indent)

    def _write(self, fout, indent, line=None, endl=True):
        if line:
            res = "{}{}".format(indent, line)
            fout.write(res)

        if endl:
            fout.write("\n")

    def write(self, line=None, endl=True):
        self._write(self.fjava, self.getIndent(), line, endl)

    def openFiles(self, rootDir):
        if not os.path.exists(rootDir):
            self.raiseExcept("outdir {} does not exist".format(rootDir))

        packages = re.split(r'\.', self.loader.scope)
        self.scopes = packages

        subDir = "/".join(packages[:-1])
        absDir = os.path.join(rootDir, subDir)
        if not os.path.exists(absDir):
            os.makedirs(absDir)

        self.filename = packages[-1] + ".java"

        self.fjava = open(os.path.join(absDir, self.filename), 'w')

    def closeFiles(self):
        self.fjava.close()

    def generate(self):
        print("Generation java code for {}".format(self.loader.filepath))
        outRootDir = self.structManager.outRootDir
        self.openFiles(outRootDir)

        self.writeComments()
        self.writeIncludes()
        self.begin()

        for dataType in self.loader.types:
            if isinstance(dataType, Struct):
                self.parseStruct(dataType)
            elif isinstance(dataType, Enum):
                self.parseEnum(dataType)
            elif isinstance(dataType, List):
                self.parseList(dataType)
            elif isinstance(dataType, Dict):
                self.parseDict(dataType)
            elif isinstance(dataType, Interface):
                self.parseInterface(dataType)
            else:
                self.raiseExcept("Unexpected datatype {}".format(type(dataType)))

        self.end()

        self.closeFiles()

    def writeComments(self):
        self.write("/*")
        self.write("* @filename {}".format(self.filename))
        self.write("*")
        self.write("* @author ahda86@gmail.com")
        self.write("*")
        self.write("* @brief This files is Auto-Generated. Please DON'T modify it EVEN if")
        self.write("*        you know what you are doing.")
        self.write("*/")
        self.write()

    def writeIncludes(self):
        self.write("package {};".format(".".join(self.scopes[:-1])))
        self.write()
        self.write()
        self.write("import java.util.Date;")
        self.write("import java.util.HashMap;")
        self.write("import java.util.Set;")
        self.write("import java.util.Iterator;")
        if self.isJsonEnabled:
            self.write("import org.json.JSONArray;")
            self.write("import org.json.JSONObject;")
            self.write("import org.json.JSONException;")
            self.write("import java.text.SimpleDateFormat;")

        self.write()
        self.write("import rmi.Serializer;")
        self.write("import rmi.MessageBlock;")
        if self.loader.hasInterface:
            self.write("import rmi.RmiCore;")
            self.write("import rmi.ProxyManager;")
            self.write("import rmi.RmiManager;")
            self.write("import rmi.RmiErrorDefaultHandler;")

        for include in self.loader.includes:
            self.write("import {};".format(include))

        self.write()
        self.write()

    def begin(self):
        self.write("public class {}".format(self.scopes[-1]))
        self.write("{")
        self.indent += 1

    def end(self):
        self.indent -= 1
        self.write("}")
        self.write()

    def getJavaType(self, dataType):
        if isinstance(dataType, BasicType):
            if dataType.name == "bool":
                return "boolean"
            if dataType.name == "string":
                return "String"
            if dataType.name == "binary":
                return "byte[]"
            if dataType.name == "date":
                return "Date"
            return dataType.name

        if isinstance(dataType, Enum):
            return "int"

        if isinstance(dataType, Struct):
            if self.isJsonEnabled:
                return dataType.name + "C"
            else:
                return dataType.name

        return dataType.name

    def getJavaRef(self, dataType):
        if self.loader.scope == dataType.scope:
            return self.getJavaType(dataType)

        if isinstance(dataType, BasicType):
            return self.getJavaType(dataType)

        if isinstance(dataType, Enum):
            return "int"

        scopeFields = dataType.scope.split(".")
        return "{}.{}".format(scopeFields[-1], self.getJavaType(dataType))

    def getInitValue(self, dataType):
        if isinstance(dataType, BasicType):
            if dataType.name == "bool":
                return "false"
            if dataType.name == "string":
                return '""'
            if dataType.name == "binary":
                return "new byte[0]"
            if dataType.name == "date":
                return "new Date()"
            return "0"

        if isinstance(dataType, Enum):
            if self.loader.scope == dataType.scope:
                return "{}.{}".format(dataType.name, dataType.pairs[0][0])
            else:
                scopeFields = dataType.scope.split(".")
                return "{}.{}.{}".format(scopeFields[-1], dataType.name, dataType.pairs[0][0])

        return "new {}()".format(self.getJavaRef(dataType))

    def getReadExpr(self, dataType, name):
        if isinstance(dataType, BasicType):
            return "{0} = __is.read({0})".format(name)

        if isinstance(dataType, Enum):
            return "{} = __is.readInt()".format(name)

        return "{}.__read(__is)".format(name)

    def getWriteExpr(self, dataType, name):
        if isinstance(dataType, BasicType):
            return "__os.write({})".format(name)

        if isinstance(dataType, Enum):
            return "__os.write({})".format(name)

        return "{}.__write(__os)".format(name)

    def parseStruct(self, dataType):
        self.registTypeList.append(dataType)

        className = dataType.name
        if self.isJsonEnabled:
            className += "C"

        self.write("// class {}".format(className))
        self.write("public static class {} extends MessageBlock.MessageBase".format(className))
        self.write("{")
        self.indent += 1

        # AutoRegist
        self.write("public static class AutoRegist extends MessageBlock.AutoRegist")
        self.write("{")
        self.indent += 1
        self.write("@Override")
        self.write("public MessageBlock.MessageBase create()")
        self.write("{")
        self.indent += 1
        self.write("return new {}();".format(className))
        self.indent -= 1
        self.write("}")
        self.indent -= 1
        self.write("}")
        self.write()

        ## static block
        self.write("public static void __regist(){")
        self.indent += 1
        self.write("MessageBlock.regist(\"{0}\", new AutoRegist());".format(className))
        self.indent -= 1
        self.write("}")
        self.write()

        # fields
        dataType.hasDateFields = False
        for field in dataType.fields:
            self.write("public {} {};".format(self.getJavaRef(field.type), field.name))
            if field.type.name == 'date':
                dataType.hasDateFields = True
        self.write()

        # constructor
        self.write("public {}()".format(className))
        self.write("{")
        self.indent += 1
        for field in dataType.fields:
            self.write("{} = {};".format(field.name, self.getInitValue(field.type)))
        self.indent -= 1
        self.write("}")
        self.write()

        # __read
        self.write("@Override")
        self.write("public void __read(Serializer __is)")
        self.write("{")
        self.indent += 1
        for field in dataType.fields:
            self.write(self.getReadExpr(field.type, field.name) + ";")

        self.indent -= 1
        self.write("}")
        self.write()

        # __write
        self.write("@Override")
        self.write("public void __write(Serializer __os)")
        self.write("{")
        self.indent += 1
        for field in dataType.fields:
            self.write(self.getWriteExpr(field.type, field.name) + ";")
        self.indent -= 1
        self.write("}")

        self.indent -= 1
        self.write("} // end of class " + className)
        self.write()

    def parseEnum(self, dataType):
        enumName = dataType.name
        self.write("// enum {}".format(enumName))
        self.write("public static class {}".format(enumName))
        self.write("{")
        self.indent += 1

        # consts
        for pair in dataType.pairs:
            self.write("final public static int {} = {};".format(*pair))
        self.write()

        self.indent -= 1
        self.write("}")
        self.write()

    def parseList(self, dataType):
        listName = dataType.name
        self.write("// List {}".format(listName))
        self.write("public static class {}".format(listName))
        self.write("{")
        self.indent += 1

        # members
        self.write("private {}[] __array;".format(self.getJavaRef(dataType.type)))
        self.write()

        # constructor
        self.write("public {}()".format(listName))
        self.write("{")
        self.indent += 1
        self.write("__array = new {}[0];".format(self.getJavaRef(dataType.type)))
        self.indent -= 1
        self.write("}")
        self.write()

        # constructor
        self.write("public {}({}[] initArray)".format(listName, self.getJavaRef(dataType.type)))
        self.write("{")
        self.indent += 1
        self.write("__array = initArray;")
        self.indent -= 1
        self.write("}")
        self.write()

        # constructor
        self.write("public {}(int arraySize)".format(listName))
        self.write("{")
        self.indent += 1
        self.write("arraySize = (arraySize >= 0 ? arraySize : 0);")
        self.write()
        self.write("__array = new {}[arraySize];".format(self.getJavaRef(dataType.type)))
        self.write("for (int i = 0; i < arraySize; i++)")
        self.write("{")
        self.indent += 1
        self.write("__array[i] = {};".format(self.getInitValue(dataType.type)))
        self.indent -= 1
        self.write("}")
        self.indent -= 1
        self.write("}")
        self.write()

        # accessor
        self.write("public {}[] getArray()".format(self.getJavaRef(dataType.type)))
        self.write("{")
        self.indent += 1
        self.write("return __array;")
        self.indent -= 1
        self.write("}")
        self.write()

        self.write("public int getSize()")
        self.write("{")
        self.indent += 1
        self.write("return (__array != null) ? __array.length : 0;")
        self.indent -= 1
        self.write("}")
        self.write()

        self.write("public boolean isEmpty()")
        self.write("{")
        self.indent += 1
        self.write("return (getSize() == 0);")
        self.indent -= 1
        self.write("}")
        self.write()

        # __reads
        self.write("public void __read(Serializer __is)")
        self.write("{")
        self.indent += 1
        self.write("int __dataSize = __is.readInt();")
        if dataType.type.name == "binary":
            self.write("__array = new byte[__dataSize][];")
        else:
            self.write("__array = new {}[__dataSize];".format(self.getJavaRef(dataType.type)))

        self.write("for (int i = 0; i < __dataSize; ++i)")
        self.write("{")
        self.indent += 1
        self.write("{} __val = {};".format(self.getJavaRef(dataType.type), self.getInitValue(dataType.type)))
        self.write(self.getReadExpr(dataType.type, "__val") + ";")
        self.write("__array[i] = __val;")
        self.indent -= 1
        self.write("}")

        self.indent -= 1
        self.write("}")
        self.write()

        # __write
        self.write("public void __write(Serializer __os)")
        self.write("{")
        self.indent += 1
        self.write("int __dataSize = (__array != null) ? __array.length : 0;")
        self.write("__os.write(__dataSize);")
        self.write("for (int i = 0; i < __dataSize; ++i)")
        self.write("{")
        self.indent += 1
        self.write(self.getWriteExpr(dataType.type, "__array[i]") + ";")
        self.indent -= 1
        self.write("}")
        self.indent -= 1
        self.write("}")
        self.write()

        # _fromjson
        if not self.isJsonEnabled:
            self.indent -= 1
            self.write("} //..")
            self.write()
            return

        self.write("public void fromJsonArray(String jsonArrayStr) throws JSONException")
        self.write("{")
        self.indent += 1
        self.write("JSONArray jsonArray = new JSONArray(jsonArrayStr);")
        self.write("int arraySize = jsonArray.length();")
        self.write("__array = new {}[arraySize];".format(self.getJavaRef(dataType.type)))
        if dataType.type.hasDateFields:
            self.write("SimpleDateFormat dtFmt = new SimpleDateFormat(\"yyyy-MM-dd HH:mm:ss\");")
        self.write()
        self.write("for (int i = 0; i < arraySize; i++)")
        self.write("{")
        self.indent += 1
        self.write("JSONObject jsonObject = jsonArray.getJSONObject(i);")
        self.write("{0} newObj = new {0}();".format(self.getJavaRef(dataType.type)))
        self.write()
        for field in dataType.type.fields:
            if field.type.name == "bool":
                self.write('newObj.{0} = jsonObject.optBoolean("{0}", false);'.format(field.name))
            elif field.type.name == "int":
                self.write('newObj.{0} = jsonObject.optInt("{0}", 0);'.format(field.name))
            elif field.type.name == "long":
                self.write('newObj.{0} = jsonObject.optLong("{0}", (long)0);'.format(field.name))
            elif field.type.name == "float":
                self.write('newObj.{0} = (float)jsonObject.optDouble("{0}", 0.0);'.format(field.name))
            elif field.type.name == "double":
                self.write('newObj.{0} = jsonObject.optDouble("{0}", 0.0);'.format(field.name))
            elif field.type.name == "date":
                self.write('String dtString{0} = jsonObject.optString("{0}", "1979-01-01 00:00:00");'.format(field.name))
                self.write("try{")
                self.indent += 1
                self.write("newObj.{0} = dtFmt.parse(dtString{0});".format(field.name))
                self.indent -= 1
                self.write("}catch (Exception ex){}")
            elif field.type.name == "string":
                self.write('newObj.{0} = jsonObject.optString("{0}", "");'.format(field.name))
            else:
                self.raiseExcept("DateType not supported in json parsing: " + field.name)
            self.write()
        self.write("__array[i] = newObj;")
        self.indent -= 1
        self.write("}")

        self.indent -= 1
        self.write("}")
        self.write()

        self.indent -= 1
        self.write("} // end of " + listName)
        self.write()

    def getDictKeyType(self, dataType):
        if dataType.name == "string":
            return "String"

        if dataType.name == "int":
            return "Integer"
        if dataType.name == "bool":
            return "Boolean"

        return dataType.name.capitalize()

    def getDictValType(self, dataType):
        if isinstance(dataType, BasicType):
            return self.getDictKeyType(dataType)

        return self.getJavaRef(dataType)

    def parseDict(self, dataType):
        dictName = dataType.name
        keyType = dataType.keyType
        valType = dataType.valType

        keyRef = self.getDictKeyType(keyType)
        valRef = self.getDictValType(valType)

        self.write("// Dict {}".format(dictName))
        self.write("public static class {}".format(dictName))
        self.write("{")
        self.indent += 1

        # member
        self.write("private HashMap<{}, {}> __map;".format(keyRef, valRef))
        self.write()

        # constructor
        self.write("public {}()".format(dictName))
        self.write("{")
        self.indent += 1
        self.write("__map = new HashMap<{}, {}>();".format(keyRef, valRef))
        self.indent -= 1
        self.write("}")
        self.write()

        # constructor
        self.write("public {}(HashMap<{}, {}> initMap)".format(dictName, keyRef, valRef))
        self.write("{")
        self.indent += 1
        self.write("__map = initMap;")
        self.indent -= 1
        self.write("}")
        self.write()

        # getter
        self.write("public HashMap<{}, {}> getMap()".format(keyRef, valRef))
        self.write("{")
        self.indent += 1
        self.write("return __map;")
        self.indent -= 1
        self.write("}")
        self.write()

        # read
        self.write("public void __read(Serializer __is)")
        self.write("{")
        self.indent += 1
        self.write("int __dataSize = __is.readInt();")
        self.write("for (int i = 0; i < __dataSize; ++i)")
        self.write("{")
        self.indent += 1

        if keyType.name == "string":
            self.write("String __key = __is.readString();")
        else:
            self.write("{} __key = new {}(__is.read{}());".format(keyRef, keyRef, keyType.name.capitalize()))

        if isinstance(valType, BasicType) and valType.name != "string":
            self.write("{} __val = new {}(__is.read{}());".format(valRef, valRef, valType.name.capitalize()))
        else:
            self.write("{} __val = {};".format(self.getJavaRef(valType), self.getInitValue(valType)))
            self.write(self.getReadExpr(valType, "__val") + ";")

        self.write("__map.put(__key, __val);")

        self.indent -= 1
        self.write("}")
        self.indent -= 1
        self.write("}")
        self.write()

        # write
        self.write("public void __write(Serializer __os)")
        self.write("{")
        self.indent += 1
        self.write("__os.write(__map.size());")
        self.write()
        self.write("Set<{}> __keySet = __map.keySet();".format(self.getDictKeyType(keyType)))
        self.write("Iterator<{}> __it = __keySet.iterator();".format(self.getDictKeyType(keyType)))
        self.write("while (__it.hasNext())")
        self.write("{")
        self.indent += 1
        self.write("{} __key = __it.next();".format(self.getDictKeyType(keyType)))
        if keyType.name != "string":
            self.write("__os.write(__key.{}Value());".format(keyType.name))
        else:
            self.write("__os.write(__key);")

        self.write("{} __val = __map.get(__key);".format(valRef))

        if isinstance(valType, BasicType) and valType.name != "string":
            if valType.name == "bool":
                self.write("__os.write(__val.booleanValue());")
            else:
                self.write("__os.write(__val.{}Value());".format(valType.name))
        else:
            self.write(self.getWriteExpr(valType, "__val") + ";")

        self.indent -= 1
        self.write("}")
        self.indent -= 1
        self.write("}")
        self.write()

        # end of class
        self.indent -= 1
        self.write("}")
        self.write()

    def parseInterface(self, dataType):
        for method in dataType.methodList:
            self.parseResponse(dataType, method)

        self.parseProxy(dataType)

    def parseResponse(self, interfaceType, method):
        interfaceName = interfaceType.name
        methodName = method.name
        className = "{}_{}_response".format(interfaceName, methodName)

        # class
        self.write("// Reponse " + className)
        self.write("public static abstract class {} extends RmiCore.RmiResponseBase".format(className))
        self.write("{")
        self.indent += 1

        self.write("/*")
        self.write("* RmiErrorDefaultHandler.onError() will be called before onError()")
        self.write("* when useDefaultErrorHandler is true;")
        self.write("*/")
        self.write("protected boolean useDefaultErrorHandler = true;")
        self.write()
        # ctor
        self.write("public {}()".format(className))
        self.write("{")
        self.indent += 1
        self.write("super();")
        self.indent -= 1
        self.write("}")
        self.write()

        # override
        # __onResponse
        self.write("@Override")
        self.write("public void __onResponse(Serializer __is)")
        self.write("{")
        self.indent += 1

        for field in method.outfields:
            self.write("{} {} = {};".format(self.getJavaRef(field.type), field.name, self.getInitValue(field.type)))
            self.write(self.getReadExpr(field.type, field.name) + ";")

        if method.outfields:
            self.write()

        self.write("onResponse(", False)
        isFirst = True
        for field in method.outfields:
            if not isFirst:
                self.fjava.write(", ")
            else:
                isFirst = False
            self.fjava.write(field.name)
        self.fjava.write(");\n")

        self.indent -= 1
        self.write("}")
        self.write()

        # override
        # __onError
        self.write("@Override")
        self.write("public void __onError(String what, int code)")
        self.write("{")
        self.indent += 1
        self.write("onError(what, code);")
        self.write()
        self.write("if (useDefaultErrorHandler)")
        self.write("{")
        self.indent += 1
        self.write("RmiErrorDefaultHandler.onError(what, code);")
        self.indent -= 1
        self.write("}")
        self.indent -= 1
        self.write("}")
        self.write()

        # override
        # __onTimeout
        self.write("@Override")
        self.write("public void __onTimeout()")
        self.write("{")
        self.indent += 1
        self.write("onTimeout();")
        self.indent -= 1
        self.write("}")
        self.write()

        # abstract methods
        self.write("public abstract void onResponse(", False)
        isFirst = True
        for field in method.outfields:
            if not isFirst:
                self.fjava.write(", ")
            else:
                isFirst = False
            self.fjava.write("{} {}".format(self.getJavaRef(field.type), field.name))
        self.fjava.write(");\n")

        self.write("public abstract void onError(String what, int code);")
        self.write("public abstract void onTimeout();")

        # end of class
        self.indent -= 1
        self.write("}")
        self.write()

    def parseProxy(self, interfaceType):
        self.registTypeList.append(interfaceType)

        className = "{}Proxy".format(interfaceType.name)
        self.write("// Proxy {}".format(className))
        self.write("public static class {} extends RmiCore.RmiProxyBase".format(className))
        self.write("{")
        self.indent += 1

        # regist
        self.write("public static void __regist(){")
        self.indent += 1
        self.write("// regist proxy at startup...")
        self.write("ProxyManager.instance().addProxy(new {}());".format(className))
        self.indent -= 1
        self.write("}")
        self.write()

        # ctor
        self.write("public {}()".format(className))
        self.write("{")
        self.indent += 1
        self.write("super(\"{}\");".format(interfaceType.name))
        self.indent -= 1
        self.write("}")
        self.write()

        # methods
        for method in interfaceType.methodList:
            self.parseProxyOutCall(interfaceType, method)

        # end of class
        self.indent -= 1
        self.write("}")
        self.write()

    def parseProxyOutCall(self, interfaceType, method):
        callbackName = "{}_{}_response".format(interfaceType.name, method.name)
        self.write("public void {}({} __response".format(method.name, callbackName), False)
        for field in method.infields:
            self.fjava.write(", {} {}".format(self.getJavaRef(field.type), field.name))
        self.fjava.write(")\n")
        self.write("{")
        self.indent += 1

        self.write("Serializer __os = new Serializer();")
        self.write("__os.startToWrite();")
        self.write("__os.write(Serializer.RmiDataCall);")
        self.write("__os.write(getName());")
        self.write("__os.write(new String(\"{}\"));".format(method.name))
        self.write()
        self.write("if (__response != null)")
        self.write("{")
        self.indent += 1
        self.write("int __msgId = MessageBlock.getMsgId();")
        self.write("__response.setMsgId(__msgId);")
        self.write("__os.write(__msgId);")
        self.indent -= 1
        self.write("}")
        self.write("else")
        self.write("{")
        self.indent += 1
        self.write("__os.write(0);")
        self.indent -= 1
        self.write("}")

        if method.infields:
            self.write()

        for field in method.infields:
            self.write(self.getWriteExpr(field.type, field.name) + ";")

        if method.infields:
            self.write()

        self.write("this.call(__os, __response);")

        # end of definition
        self.indent -= 1
        self.write("}")
        self.write()

def processRegist(outDir, scope, typeList):
    if scope:
        outDir = os.path.join(outDir, scope)

    outFileName = os.path.join(outDir, "MessageRegister.java")
    registSet = set()
    if os.path.exists(outFileName):
        lines = open(outFileName, 'r').readlines()
        for line in lines:
            line = line.strip()
            if line.find("__regist") >= 0:
                registSet.add(line)

    fout = open(outFileName, "w")
    if scope:
        fout.write("package {};\n\n".format(scope))

    for dataType in typeList:
        if not isinstance(dataType, Interface):
            line = "{}.__regist();".format(dataType.fullname)
        else:
            line = "{}Proxy.__regist();".format(dataType.fullname)
        registSet.add(line)

    registSet = [line for line in registSet]
    registSet.sort()

    fout.write("import rmi.MessageBlock;\n")
    for line in registSet:
        m = re.match(r"^(.+)\.__regist", line)
        if m:
            fout.write("import {};\n".format(m.group(1)))

    fout.write("\n")
    fout.write("public class MessageRegister{\n")
    fout.write("    public static void regist(){\n")
    for line in registSet:
        fout.write("        {}\n".format(line))
    fout.write("    }\n")
    fout.write("}\n\n")

def main():
    parser = OptionParser()
    parser.add_option("-n", "--namespace", help="root python module name",
                      dest="scope")
    parser.add_option("-g", "--gmt-dir", help="root directory of gmt files",
                      dest="inRootDir")
    parser.add_option("-o", "--out-dir", help="root directory of generated java files",
                      dest="outRootDir")
    parser.add_option("-f", "--file", dest="sources", action="append",
                      help="relative path of source gmt file. Multi-assignation is allowed.")
    parser.add_option("-j","--json", help="support json", dest="enable_json", action="store_true")

    options, args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return

    scope = options.scope or ""
    inRootDir = options.inRootDir or "."
    outRootDir = options.outRootDir or "."
    sources = options.sources or []
    enable_json = options.enable_json

    if not sources:
        return

    structManager = StructManager(scope, inRootDir, outRootDir)
    loaders = []
    typeList = []
    for f in sources:
        loader = structManager.loadFile(f)
        gmt = Gmt2Java(structManager, loader, enable_json)
        gmt.generate()

        if not enable_json:
            typeList.extend(gmt.registTypeList)

    processRegist(outRootDir, scope, typeList)

if __name__ == "__main__":
    main()
