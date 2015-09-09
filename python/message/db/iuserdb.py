#
# file: iuserdb.py
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
import message.db.mongodb.usertables
import message.db.dataview


class IUserDb_Loaduserbasic_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, isAllDataLoaded, userBasics):
        if not isinstance(isAllDataLoaded, bool):
            raise Exception("isAllDataLoaded must be instance of bool", 0)

        if not isinstance(userBasics, message.db.mongodb.usertables.SeqTUserBasic):
            raise Exception("userBasics must be instance of message.db.mongodb.usertables.SeqTUserBasic", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeBool(isAllDataLoaded)
        userBasics._write(_os)

        self.sendout()

class IUserDb_Loaduserdataview_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, userDataView):
        if not isinstance(userDataView, message.db.dataview.SUserDataView):
            raise Exception("userDataView must be instance of message.db.dataview.SUserDataView", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        userDataView._write(_os)

        self.sendout()

class IUserDb_Loaduserbasic_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        isAllDataLoaded = bool()
        isAllDataLoaded = _is.readBool()
        userBasics = message.db.mongodb.usertables.SeqTUserBasic()
        userBasics._read(_is)

        self.onResponse(isAllDataLoaded, userBasics)

    @abc.abstractmethod
    def onResponse(self, isAllDataLoaded, userBasics):
        """
        :type isAllDataLoaded: bool
        :type userBasics: list[message.db.mongodb.usertables.TUserBasic]
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


class IUserDb_Loaduserdataview_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        userDataView = message.db.dataview.SUserDataView()
        userDataView._read(_is)

        self.onResponse(userDataView)

    @abc.abstractmethod
    def onResponse(self, userDataView):
        """
        :type userDataView: message.db.dataview.SUserDataView
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


class IUserDbServant(RmiServant):
    def __init__(self, name='IUserDb'):
        super().__init__(name)
        self.methodMap['loadUserBasic'] = self._loadUserBasic
        self.methodMap['loadUserDataView'] = self._loadUserDataView

    def _loadUserBasic(self, _connId, _msgId, _is):
        createdDtLimit = datetime.datetime.now()
        createdDtLimit = _is.readDate()
        targetNum = int()
        targetNum = _is.readInt()
        _request = IUserDb_Loaduserbasic_Request(_connId, _msgId, self)
        self.loadUserBasic(createdDtLimit, targetNum, _request)

    def _loadUserDataView(self, _connId, _msgId, _is):
        account = str()
        account = _is.readString()
        _request = IUserDb_Loaduserdataview_Request(_connId, _msgId, self)
        self.loadUserDataView(account, _request)


    @abc.abstractmethod
    def loadUserBasic(self, createdDtLimit, targetNum, _request):
        """
        :type createdDtLimit: datetime.datetime
        :type targetNum: int
        :type _request: message.db.iuserdb.IUserDb_Loaduserbasic_Request
        """
        pass

    @abc.abstractmethod
    def loadUserDataView(self, account, _request):
        """
        :type account: str
        :type _request: message.db.iuserdb.IUserDb_Loaduserdataview_Request
        """
        pass

# message.db.iuserdb.IUserDbProxy
class IUserDbProxy(RmiProxy):
    def __init__(self, name='IUserDb'):
        super().__init__(name)

    def loadUserBasic(self, _response, createdDtLimit, targetNum):
        """
        :type _response: IUserDb_Loaduserbasic_Response
        :type createdDtLimit: datetime.datetime
        :type targetNum: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('loadUserBasic')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeDate(createdDtLimit)
        _os.writeInt(targetNum)
        self.invoke(_os, _response)

    def loadUserDataView(self, _response, account):
        """
        :type _response: IUserDb_Loaduserdataview_Response
        :type account: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('loadUserDataView')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(account)
        self.invoke(_os, _response)


