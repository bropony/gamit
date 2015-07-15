"""
* @name runtest.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 19:56
*
* @desc runtest.py
"""

from gamit.log.logger import Logger
from gamit.serialize.serializer import Serializer
from gamit.rmi.proxymanager import ProxyManager
from gamit.app import apptype as AppType
from gamit.message.messagemanager import MessageManager

from message.gate import gatemsg
from message.gate.command import ETestCommand

from test.ItestTest import ITest_Getintlist_Response_Impl, ITest_Signup_Response_Impl

def runTest():
    msgDict = {}
    msgDict["msg1"] = gatemsg.SMessage()
    msgDict["msg2"] = gatemsg.SMessage()

    js = gatemsg.DictMessageToJson(msgDict)
    print(js)

    dictBack = gatemsg.DictMessageFromJson(js)
    print(dictBack)

    return

    Logger.logInfo("Sending out first message")
    data = gatemsg.SMessage()
    MessageManager.sendMessageToServant(AppType.GATE, ETestCommand.FirstMessage, [], data)

    Logger.logInfo("calling getIntList")
    proxy = ProxyManager.getProxy(AppType.GATE, "ITest")
    if proxy:
        reponse = ITest_Getintlist_Response_Impl()
        proxy.getIntList(reponse, 10)

        xxx = ITest_Signup_Response_Impl()
        proxy.signup(xxx, gatemsg.SSignup())