"""
* @name SerializerTest.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/15 18:03
*
* @desc SerializerTest.py
"""

from message.db.mongodb.usertables import TUserFan, SeqTUserFan
from gamit.serialize.serializer import Serializer
from gamit.serialize.encrypt import simpleDecrypt, simpleEncrypt

def printObj(obj, desc):
    __os = Serializer()
    __os.startToWrite()

    userFan = TUserFan()
    userFan.fanUserId = "4acf3860-4bd4-11e5-b592-989096e48b93"
    userFan._write(__os)

    __is = Serializer(__os.getBuffer())
    __is.startToRead()
    back = TUserFan()
    back._read(__is)

    print("done...")

def runTest():
    __os = Serializer()
    __os.startToWrite()
    __os.writeInt(5)

    fanList = SeqTUserFan()

    userFan = TUserFan()
    userFan.fanUserId = "4acf3860-4bd4-11e5-b592-989096e48b93"
    userFan.myUserId = "a9835e44-48a6-11e5-9679-989096e48b93"
    fanList.append(userFan)
    fanList._write(__os)
    res = simpleEncrypt(__os.getBuffer())

    __is = Serializer(simpleDecrypt(res))
    __is.startToRead()
    msg = __is.readInt()

    back = SeqTUserFan()
    back._read(__is)

    print("done...")
