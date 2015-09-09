#
# file: TMessageConfig.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *


# message.db.configs.TMessageConfig.TMessageConfig
class TMessageConfig:
    __slots__ = dict()
    __slots__['msgId'] = int
    __slots__['msgKey'] = str
    __slots__['msgContent'] = str
    __slots__['shortDesc'] = str

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TMessageConfig.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type msgId: int
    type msgKey: str
    type msgContent: str
    type shortDesc: str
    """
    def __init__(self):
        self.msgId = int()
        self.msgKey = str()
        self.msgContent = str()
        self.shortDesc = str()

    def _read(self, _is):
        self.msgId = _is.readInt()
        self.msgKey = _is.readString()
        self.msgContent = _is.readString()
        self.shortDesc = _is.readString()

    def _write(self, _os):
        _os.writeInt(self.msgId)
        _os.writeString(self.msgKey)
        _os.writeString(self.msgContent)
        _os.writeString(self.shortDesc)

    def _fromJson(self, js):
        if 'msgId' in js and isinstance(js['msgId'], int):
            self.msgId = js['msgId']
        if 'msgKey' in js and isinstance(js['msgKey'], str):
            self.msgKey = js['msgKey']
        if 'msgContent' in js and isinstance(js['msgContent'], str):
            self.msgContent = js['msgContent']
        if 'shortDesc' in js and isinstance(js['shortDesc'], str):
            self.shortDesc = js['shortDesc']

    def _toJson(self):
        js = dict()
        js['msgId'] = self.msgId
        js['msgKey'] = self.msgKey
        js['msgContent'] = self.msgContent
        js['shortDesc'] = self.shortDesc
        return js

MessageBlock.register(TMessageConfig)

# message.db.configs.TMessageConfig.SeqTMessageConfig
class SeqTMessageConfig(ListBase):
    def __init__(self, _data=None):
        super().__init__(TMessageConfig, 'SeqTMessageConfig')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TMessageConfig()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TMessageConfig()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

