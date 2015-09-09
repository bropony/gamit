#
# file: tailermsg.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *
import message.common.publicdef
import message.common.publicmsg
import message.gate.gateconst
import message.gate.gatemsg


# message.gate.tailermsg.STailerOrder
class STailerOrder:
    __slots__ = dict()
    __slots__['orderId'] = str
    __slots__['userInfo'] = message.gate.gatemsg.SUserBrief
    __slots__['publishedDt'] = datetime.datetime
    __slots__['orderType'] = int
    __slots__['tags'] = message.common.publicdef.SeqString
    __slots__['title'] = str
    __slots__['content'] = str
    __slots__['imagesInfo'] = message.gate.gatemsg.SImageInfo
    __slots__['viewTimes'] = int
    __slots__['bidderNum'] = int
    __slots__['isBidded'] = bool

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of STailerOrder.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type orderId: str
    type userInfo: message.gate.gatemsg.SUserBrief
    type publishedDt: datetime.datetime
    type orderType: int
    type tags: list[str]
    type title: str
    type content: str
    type imagesInfo: message.gate.gatemsg.SImageInfo
    type viewTimes: int
    type bidderNum: int
    type isBidded: bool
    """
    def __init__(self):
        self.orderId = str()
        self.userInfo = message.gate.gatemsg.SUserBrief()
        self.publishedDt = datetime.datetime.now()
        self.orderType = message.gate.gateconst.ETailerOrderType.NoneType
        self.tags = message.common.publicdef.SeqString()
        self.title = str()
        self.content = str()
        self.imagesInfo = message.gate.gatemsg.SImageInfo()
        self.viewTimes = int()
        self.bidderNum = int()
        self.isBidded = bool()

    def _read(self, _is):
        self.orderId = _is.readString()
        self.userInfo._read(_is)
        self.publishedDt = _is.readDate()
        self.orderType = _is.readInt()
        self.tags._read(_is)
        self.title = _is.readString()
        self.content = _is.readString()
        self.imagesInfo._read(_is)
        self.viewTimes = _is.readInt()
        self.bidderNum = _is.readInt()
        self.isBidded = _is.readBool()

    def _write(self, _os):
        _os.writeString(self.orderId)
        self.userInfo._write(_os)
        _os.writeDate(self.publishedDt)
        _os.writeInt(self.orderType)
        self.tags._write(_os)
        _os.writeString(self.title)
        _os.writeString(self.content)
        self.imagesInfo._write(_os)
        _os.writeInt(self.viewTimes)
        _os.writeInt(self.bidderNum)
        _os.writeBool(self.isBidded)

    def _fromJson(self, js):
        if 'orderId' in js and isinstance(js['orderId'], str):
            self.orderId = js['orderId']
        if 'userInfo' in js and isinstance(js['userInfo'], message.gate.gatemsg.SUserBrief):
            self.userInfo._fromJson(js['userInfo'])
        if 'publishedDt' in js and isinstance(js['publishedDt'], datetime.datetime):
            self.publishedDt = js['publishedDt']
        elif 'publishedDt' in js and isinstance(self.publishedDt, datetime.datetime):
            self.publishedDt = datetime.datetime.strptime(js['publishedDt'], '%Y-%m-%d %H:%M:%S')
        if 'orderType' in js and isinstance(js['orderType'], int):
            self.orderType = js['orderType']
        if 'tags' in js and isinstance(js['tags'], message.common.publicdef.SeqString):
            self.tags._fromJson(js['tags'])
        elif 'tags' in js and isinstance(js['tags'], list):
            self.tags._fromJson(js['tags'])
        if 'title' in js and isinstance(js['title'], str):
            self.title = js['title']
        if 'content' in js and isinstance(js['content'], str):
            self.content = js['content']
        if 'imagesInfo' in js and isinstance(js['imagesInfo'], message.gate.gatemsg.SImageInfo):
            self.imagesInfo._fromJson(js['imagesInfo'])
        if 'viewTimes' in js and isinstance(js['viewTimes'], int):
            self.viewTimes = js['viewTimes']
        if 'bidderNum' in js and isinstance(js['bidderNum'], int):
            self.bidderNum = js['bidderNum']
        if 'isBidded' in js and isinstance(js['isBidded'], bool):
            self.isBidded = js['isBidded']

    def _toJson(self):
        js = dict()
        js['orderId'] = self.orderId
        js['userInfo'] = self.userInfo._toJson()
        js['publishedDt'] = self.publishedDt
        js['orderType'] = self.orderType
        js['tags'] = self.tags._toJson()
        js['title'] = self.title
        js['content'] = self.content
        js['imagesInfo'] = self.imagesInfo._toJson()
        js['viewTimes'] = self.viewTimes
        js['bidderNum'] = self.bidderNum
        js['isBidded'] = self.isBidded
        return js

MessageBlock.register(STailerOrder)

# message.gate.tailermsg.SeqTailerOrder
class SeqTailerOrder(ListBase):
    def __init__(self, _data=None):
        super().__init__(STailerOrder, 'SeqTailerOrder')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = STailerOrder()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = STailerOrder()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.gate.tailermsg.SMyTailerOrder
class SMyTailerOrder:
    __slots__ = dict()
    __slots__['orderId'] = str
    __slots__['publishedDt'] = datetime.datetime
    __slots__['orderType'] = int
    __slots__['tags'] = message.common.publicdef.SeqString
    __slots__['title'] = str
    __slots__['content'] = str
    __slots__['imagesInfo'] = message.gate.gatemsg.SImageInfo
    __slots__['orderStage'] = int
    __slots__['viewTimes'] = int
    __slots__['bidderNum'] = int
    __slots__['isBidded'] = bool

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SMyTailerOrder.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type orderId: str
    type publishedDt: datetime.datetime
    type orderType: int
    type tags: list[str]
    type title: str
    type content: str
    type imagesInfo: message.gate.gatemsg.SImageInfo
    type orderStage: int
    type viewTimes: int
    type bidderNum: int
    type isBidded: bool
    """
    def __init__(self):
        self.orderId = str()
        self.publishedDt = datetime.datetime.now()
        self.orderType = message.gate.gateconst.ETailerOrderType.NoneType
        self.tags = message.common.publicdef.SeqString()
        self.title = str()
        self.content = str()
        self.imagesInfo = message.gate.gatemsg.SImageInfo()
        self.orderStage = message.gate.gateconst.ETailerOrderStage.NotBidded
        self.viewTimes = int()
        self.bidderNum = int()
        self.isBidded = bool()

    def _read(self, _is):
        self.orderId = _is.readString()
        self.publishedDt = _is.readDate()
        self.orderType = _is.readInt()
        self.tags._read(_is)
        self.title = _is.readString()
        self.content = _is.readString()
        self.imagesInfo._read(_is)
        self.orderStage = _is.readInt()
        self.viewTimes = _is.readInt()
        self.bidderNum = _is.readInt()
        self.isBidded = _is.readBool()

    def _write(self, _os):
        _os.writeString(self.orderId)
        _os.writeDate(self.publishedDt)
        _os.writeInt(self.orderType)
        self.tags._write(_os)
        _os.writeString(self.title)
        _os.writeString(self.content)
        self.imagesInfo._write(_os)
        _os.writeInt(self.orderStage)
        _os.writeInt(self.viewTimes)
        _os.writeInt(self.bidderNum)
        _os.writeBool(self.isBidded)

    def _fromJson(self, js):
        if 'orderId' in js and isinstance(js['orderId'], str):
            self.orderId = js['orderId']
        if 'publishedDt' in js and isinstance(js['publishedDt'], datetime.datetime):
            self.publishedDt = js['publishedDt']
        elif 'publishedDt' in js and isinstance(self.publishedDt, datetime.datetime):
            self.publishedDt = datetime.datetime.strptime(js['publishedDt'], '%Y-%m-%d %H:%M:%S')
        if 'orderType' in js and isinstance(js['orderType'], int):
            self.orderType = js['orderType']
        if 'tags' in js and isinstance(js['tags'], message.common.publicdef.SeqString):
            self.tags._fromJson(js['tags'])
        elif 'tags' in js and isinstance(js['tags'], list):
            self.tags._fromJson(js['tags'])
        if 'title' in js and isinstance(js['title'], str):
            self.title = js['title']
        if 'content' in js and isinstance(js['content'], str):
            self.content = js['content']
        if 'imagesInfo' in js and isinstance(js['imagesInfo'], message.gate.gatemsg.SImageInfo):
            self.imagesInfo._fromJson(js['imagesInfo'])
        if 'orderStage' in js and isinstance(js['orderStage'], int):
            self.orderStage = js['orderStage']
        if 'viewTimes' in js and isinstance(js['viewTimes'], int):
            self.viewTimes = js['viewTimes']
        if 'bidderNum' in js and isinstance(js['bidderNum'], int):
            self.bidderNum = js['bidderNum']
        if 'isBidded' in js and isinstance(js['isBidded'], bool):
            self.isBidded = js['isBidded']

    def _toJson(self):
        js = dict()
        js['orderId'] = self.orderId
        js['publishedDt'] = self.publishedDt
        js['orderType'] = self.orderType
        js['tags'] = self.tags._toJson()
        js['title'] = self.title
        js['content'] = self.content
        js['imagesInfo'] = self.imagesInfo._toJson()
        js['orderStage'] = self.orderStage
        js['viewTimes'] = self.viewTimes
        js['bidderNum'] = self.bidderNum
        js['isBidded'] = self.isBidded
        return js

MessageBlock.register(SMyTailerOrder)

# message.gate.tailermsg.SeqMyTailerOrder
class SeqMyTailerOrder(ListBase):
    def __init__(self, _data=None):
        super().__init__(SMyTailerOrder, 'SeqMyTailerOrder')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SMyTailerOrder()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SMyTailerOrder()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

