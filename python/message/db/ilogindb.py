#
# file: ilogindb.py
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
import message.db.mongodb.usertables
import message.db.dataview


class ILoginDb_Createaccount_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, dataView):
        if not isinstance(dataView, message.db.dataview.SUserDataView):
            raise Exception("dataView must be instance of message.db.dataview.SUserDataView", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        dataView._write(_os)

        self.sendout()

class ILoginDb_Createaccount_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        dataView = message.db.dataview.SUserDataView()
        dataView._read(_is)

        self.onResponse(dataView)

    @abc.abstractmethod
    def onResponse(self, dataView):
        """
        :type dataView: message.db.dataview.SUserDataView
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


class ILoginDbServant(RmiServant):
    def __init__(self, name='ILoginDb'):
        super().__init__(name)
        self.methodMap['createAccount'] = self._createAccount

    def _createAccount(self, _connId, _msgId, _is):
        userInfo = message.gate.gatemsg.SSignup()
        userInfo._read(_is)
        _request = ILoginDb_Createaccount_Request(_connId, _msgId, self)
        self.createAccount(userInfo, _request)


    @abc.abstractmethod
    def createAccount(self, userInfo, _request):
        """
        :type userInfo: message.gate.gatemsg.SSignup
        :type _request: message.db.ilogindb.ILoginDb_Createaccount_Request
        """
        pass

# message.db.ilogindb.ILoginDbProxy
class ILoginDbProxy(RmiProxy):
    def __init__(self, name='ILoginDb'):
        super().__init__(name)

    def createAccount(self, _response, userInfo):
        """
        :type _response: ILoginDb_Createaccount_Response
        :type userInfo: message.gate.gatemsg.SSignup
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('createAccount')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        userInfo._write(_os)
        self.invoke(_os, _response)


