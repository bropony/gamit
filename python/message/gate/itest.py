#
# file: itest.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *
from gamit.rmi.rmicore import *
from gamit.serialize.serializer import Serializer
from gamit.serialize.datatype import RmiDataType
import abc
import message.common.publicdef
import message.common.publicmsg
import message.gate.gateconst
import message.gate.gatemsg


class ITest_Addsystopic_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITest_Addsystopic_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITestServant(RmiServant):
    def __init__(self, name='ITest'):
        super().__init__(name)
        self.methodMap['addSysTopic'] = self._addSysTopic

    def _addSysTopic(self, _connId, _msgId, _is):
        newSysTopic = message.gate.gatemsg.SSysTopic()
        newSysTopic._read(_is)
        _request = ITest_Addsystopic_Request(_connId, _msgId, self)
        self.addSysTopic(newSysTopic, _request)


    @abc.abstractmethod
    def addSysTopic(self, newSysTopic, _request):
        """
        :type newSysTopic: message.gate.gatemsg.SSysTopic
        :type _request: message.gate.itest.ITest_Addsystopic_Request
        """
        pass

# message.gate.itest.ITestProxy
class ITestProxy(RmiProxy):
    def __init__(self, name='ITest'):
        super().__init__(name)

    def addSysTopic(self, _response, newSysTopic):
        """
        :type _response: ITest_Addsystopic_Response
        :type newSysTopic: message.gate.gatemsg.SSysTopic
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('addSysTopic')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        newSysTopic._write(_os)
        self.invoke(_os, _response)


