#
# file: itaileroper.py
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
import message.gate.tailermsg


# message.gate.itaileroper.SNewOrderParams
class SNewOrderParams:
    __slots__ = dict()
    __slots__['orderType'] = int
    __slots__['title'] = str
    __slots__['content'] = str
    __slots__['imageKeys'] = message.common.publicdef.SeqString
    __slots__['tags'] = message.common.publicdef.SeqString

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SNewOrderParams.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type orderType: int
    type title: str
    type content: str
    type imageKeys: list[str]
    type tags: list[str]
    """
    def __init__(self):
        self.orderType = message.gate.gateconst.ETailerOrderType.NoneType
        self.title = str()
        self.content = str()
        self.imageKeys = message.common.publicdef.SeqString()
        self.tags = message.common.publicdef.SeqString()

    def _read(self, _is):
        self.orderType = _is.readInt()
        self.title = _is.readString()
        self.content = _is.readString()
        self.imageKeys._read(_is)
        self.tags._read(_is)

    def _write(self, _os):
        _os.writeInt(self.orderType)
        _os.writeString(self.title)
        _os.writeString(self.content)
        self.imageKeys._write(_os)
        self.tags._write(_os)

    def _fromJson(self, js):
        if 'orderType' in js and isinstance(js['orderType'], int):
            self.orderType = js['orderType']
        if 'title' in js and isinstance(js['title'], str):
            self.title = js['title']
        if 'content' in js and isinstance(js['content'], str):
            self.content = js['content']
        if 'imageKeys' in js and isinstance(js['imageKeys'], message.common.publicdef.SeqString):
            self.imageKeys._fromJson(js['imageKeys'])
        elif 'imageKeys' in js and isinstance(js['imageKeys'], list):
            self.imageKeys._fromJson(js['imageKeys'])
        if 'tags' in js and isinstance(js['tags'], message.common.publicdef.SeqString):
            self.tags._fromJson(js['tags'])
        elif 'tags' in js and isinstance(js['tags'], list):
            self.tags._fromJson(js['tags'])

    def _toJson(self):
        js = dict()
        js['orderType'] = self.orderType
        js['title'] = self.title
        js['content'] = self.content
        js['imageKeys'] = self.imageKeys._toJson()
        js['tags'] = self.tags._toJson()
        return js

MessageBlock.register(SNewOrderParams)

class ITailerOper_Newtailerorder_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, orderId):
        if not isinstance(orderId, str):
            raise Exception("orderId must be instance of string", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeString(orderId)

        self.sendout()

class ITailerOper_Getmytailerordrlist_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, orderList):
        if not isinstance(orderList, message.gate.tailermsg.SeqMyTailerOrder):
            raise Exception("orderList must be instance of message.gate.tailermsg.SeqMyTailerOrder", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        orderList._write(_os)

        self.sendout()

class ITailerOper_Getlatesttailerorderlist_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, orderList):
        if not isinstance(orderList, message.gate.tailermsg.SeqTailerOrder):
            raise Exception("orderList must be instance of message.gate.tailermsg.SeqTailerOrder", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        orderList._write(_os)

        self.sendout()

class ITailerOper_Getoldertailerorderlist_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, orderList):
        if not isinstance(orderList, message.gate.tailermsg.SeqTailerOrder):
            raise Exception("orderList must be instance of message.gate.tailermsg.SeqTailerOrder", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        orderList._write(_os)

        self.sendout()

class ITailerOper_Newtailerorder_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        orderId = str()
        orderId = _is.readString()

        self.onResponse(orderId)

    @abc.abstractmethod
    def onResponse(self, orderId):
        """
        :type orderId: str
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


class ITailerOper_Getmytailerordrlist_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        orderList = message.gate.tailermsg.SeqMyTailerOrder()
        orderList._read(_is)

        self.onResponse(orderList)

    @abc.abstractmethod
    def onResponse(self, orderList):
        """
        :type orderList: list[message.gate.tailermsg.SMyTailerOrder]
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


class ITailerOper_Getlatesttailerorderlist_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        orderList = message.gate.tailermsg.SeqTailerOrder()
        orderList._read(_is)

        self.onResponse(orderList)

    @abc.abstractmethod
    def onResponse(self, orderList):
        """
        :type orderList: list[message.gate.tailermsg.STailerOrder]
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


class ITailerOper_Getoldertailerorderlist_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        orderList = message.gate.tailermsg.SeqTailerOrder()
        orderList._read(_is)

        self.onResponse(orderList)

    @abc.abstractmethod
    def onResponse(self, orderList):
        """
        :type orderList: list[message.gate.tailermsg.STailerOrder]
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


class ITailerOperServant(RmiServant):
    def __init__(self, name='ITailerOper'):
        super().__init__(name)
        self.methodMap['newTailerOrder'] = self._newTailerOrder
        self.methodMap['getMyTailerOrdrList'] = self._getMyTailerOrdrList
        self.methodMap['getLatestTailerOrderList'] = self._getLatestTailerOrderList
        self.methodMap['getOlderTailerOrderList'] = self._getOlderTailerOrderList

    def _newTailerOrder(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        orderParams = SNewOrderParams()
        orderParams._read(_is)
        _request = ITailerOper_Newtailerorder_Request(_connId, _msgId, self)
        self.newTailerOrder(sessionKey, orderParams, _request)

    def _getMyTailerOrdrList(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        pageIndex = int()
        pageIndex = _is.readInt()
        _request = ITailerOper_Getmytailerordrlist_Request(_connId, _msgId, self)
        self.getMyTailerOrdrList(sessionKey, pageIndex, _request)

    def _getLatestTailerOrderList(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        latestOrderDt = datetime.datetime.now()
        latestOrderDt = _is.readDate()
        targetNum = int()
        targetNum = _is.readInt()
        _request = ITailerOper_Getlatesttailerorderlist_Request(_connId, _msgId, self)
        self.getLatestTailerOrderList(sessionKey, latestOrderDt, targetNum, _request)

    def _getOlderTailerOrderList(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        oldestOrderDt = datetime.datetime.now()
        oldestOrderDt = _is.readDate()
        targetNum = int()
        targetNum = _is.readInt()
        _request = ITailerOper_Getoldertailerorderlist_Request(_connId, _msgId, self)
        self.getOlderTailerOrderList(sessionKey, oldestOrderDt, targetNum, _request)


    @abc.abstractmethod
    def newTailerOrder(self, sessionKey, orderParams, _request):
        """
        :type sessionKey: str
        :type orderParams: message.gate.itaileroper.SNewOrderParams
        :type _request: message.gate.itaileroper.ITailerOper_Newtailerorder_Request
        """
        pass

    @abc.abstractmethod
    def getMyTailerOrdrList(self, sessionKey, pageIndex, _request):
        """
        :type sessionKey: str
        :type pageIndex: int
        :type _request: message.gate.itaileroper.ITailerOper_Getmytailerordrlist_Request
        """
        pass

    @abc.abstractmethod
    def getLatestTailerOrderList(self, sessionKey, latestOrderDt, targetNum, _request):
        """
        :type sessionKey: str
        :type latestOrderDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.itaileroper.ITailerOper_Getlatesttailerorderlist_Request
        """
        pass

    @abc.abstractmethod
    def getOlderTailerOrderList(self, sessionKey, oldestOrderDt, targetNum, _request):
        """
        :type sessionKey: str
        :type oldestOrderDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.itaileroper.ITailerOper_Getoldertailerorderlist_Request
        """
        pass

# message.gate.itaileroper.ITailerOperProxy
class ITailerOperProxy(RmiProxy):
    def __init__(self, name='ITailerOper'):
        super().__init__(name)

    def newTailerOrder(self, _response, sessionKey, orderParams):
        """
        :type _response: ITailerOper_Newtailerorder_Response
        :type sessionKey: str
        :type orderParams: message.gate.itaileroper.SNewOrderParams
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('newTailerOrder')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        orderParams._write(_os)
        self.invoke(_os, _response)

    def getMyTailerOrdrList(self, _response, sessionKey, pageIndex):
        """
        :type _response: ITailerOper_Getmytailerordrlist_Response
        :type sessionKey: str
        :type pageIndex: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getMyTailerOrdrList')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeInt(pageIndex)
        self.invoke(_os, _response)

    def getLatestTailerOrderList(self, _response, sessionKey, latestOrderDt, targetNum):
        """
        :type _response: ITailerOper_Getlatesttailerorderlist_Response
        :type sessionKey: str
        :type latestOrderDt: datetime.datetime
        :type targetNum: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getLatestTailerOrderList')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeDate(latestOrderDt)
        _os.writeInt(targetNum)
        self.invoke(_os, _response)

    def getOlderTailerOrderList(self, _response, sessionKey, oldestOrderDt, targetNum):
        """
        :type _response: ITailerOper_Getoldertailerorderlist_Response
        :type sessionKey: str
        :type oldestOrderDt: datetime.datetime
        :type targetNum: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getOlderTailerOrderList')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeDate(oldestOrderDt)
        _os.writeInt(targetNum)
        self.invoke(_os, _response)


