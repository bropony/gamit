#
# file: TConstConfig.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *


# message.db.configs.TConstConfig.TConstConfig
class TConstConfig:
    __slots__ = dict()
    __slots__['constName'] = str
    __slots__['intValue'] = int
    __slots__['strValue'] = str
    __slots__['shortDesc'] = str

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TConstConfig.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type constName: str
    type intValue: int
    type strValue: str
    type shortDesc: str
    """
    def __init__(self):
        self.constName = str()
        self.intValue = int()
        self.strValue = str()
        self.shortDesc = str()

    def _read(self, _is):
        self.constName = _is.readString()
        self.intValue = _is.readInt()
        self.strValue = _is.readString()
        self.shortDesc = _is.readString()

    def _write(self, _os):
        _os.writeString(self.constName)
        _os.writeInt(self.intValue)
        _os.writeString(self.strValue)
        _os.writeString(self.shortDesc)

    def _fromJson(self, js):
        if 'constName' in js and isinstance(js['constName'], str):
            self.constName = js['constName']
        if 'intValue' in js and isinstance(js['intValue'], int):
            self.intValue = js['intValue']
        if 'strValue' in js and isinstance(js['strValue'], str):
            self.strValue = js['strValue']
        if 'shortDesc' in js and isinstance(js['shortDesc'], str):
            self.shortDesc = js['shortDesc']

    def _toJson(self):
        js = dict()
        js['constName'] = self.constName
        js['intValue'] = self.intValue
        js['strValue'] = self.strValue
        js['shortDesc'] = self.shortDesc
        return js

MessageBlock.register(TConstConfig)

# message.db.configs.TConstConfig.SeqTConstConfig
class SeqTConstConfig(ListBase):
    def __init__(self, _data=None):
        super().__init__(TConstConfig, 'SeqTConstConfig')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TConstConfig()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TConstConfig()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

