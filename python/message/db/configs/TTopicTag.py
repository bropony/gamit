#
# file: TTopicTag.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *


# message.db.configs.TTopicTag.TTopicTag
class TTopicTag:
    __slots__ = dict()
    __slots__['tagId'] = int
    __slots__['tagType'] = int
    __slots__['tagName'] = str
    __slots__['isDefualt'] = int
    __slots__['shortDesc'] = str

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TTopicTag.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type tagId: int
    type tagType: int
    type tagName: str
    type isDefualt: int
    type shortDesc: str
    """
    def __init__(self):
        self.tagId = int()
        self.tagType = int()
        self.tagName = str()
        self.isDefualt = int()
        self.shortDesc = str()

    def _read(self, _is):
        self.tagId = _is.readInt()
        self.tagType = _is.readInt()
        self.tagName = _is.readString()
        self.isDefualt = _is.readInt()
        self.shortDesc = _is.readString()

    def _write(self, _os):
        _os.writeInt(self.tagId)
        _os.writeInt(self.tagType)
        _os.writeString(self.tagName)
        _os.writeInt(self.isDefualt)
        _os.writeString(self.shortDesc)

    def _fromJson(self, js):
        if 'tagId' in js and isinstance(js['tagId'], int):
            self.tagId = js['tagId']
        if 'tagType' in js and isinstance(js['tagType'], int):
            self.tagType = js['tagType']
        if 'tagName' in js and isinstance(js['tagName'], str):
            self.tagName = js['tagName']
        if 'isDefualt' in js and isinstance(js['isDefualt'], int):
            self.isDefualt = js['isDefualt']
        if 'shortDesc' in js and isinstance(js['shortDesc'], str):
            self.shortDesc = js['shortDesc']

    def _toJson(self):
        js = dict()
        js['tagId'] = self.tagId
        js['tagType'] = self.tagType
        js['tagName'] = self.tagName
        js['isDefualt'] = self.isDefualt
        js['shortDesc'] = self.shortDesc
        return js

MessageBlock.register(TTopicTag)

# message.db.configs.TTopicTag.SeqTTopicTag
class SeqTTopicTag(ListBase):
    def __init__(self, _data=None):
        super().__init__(TTopicTag, 'SeqTTopicTag')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TTopicTag()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TTopicTag()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

