#
# file: publicdef.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *


# message.common.publicdef.SeqInt
class SeqInt(ListBase):
    def __init__(self, _data=None):
        super().__init__(int, 'SeqInt')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = int()
            val = _is.readInt()
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            _os.writeInt(val)

    def _fromJson(self, js):
        for js_c in js:
            self.append(js_c)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val)
        return res

# message.common.publicdef.SeqLong
class SeqLong(ListBase):
    def __init__(self, _data=None):
        super().__init__(int, 'SeqLong')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = int()
            val = _is.readLong()
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            _os.writeLong(val)

    def _fromJson(self, js):
        for js_c in js:
            self.append(js_c)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val)
        return res

# message.common.publicdef.SeqByte
class SeqByte(ListBase):
    def __init__(self, _data=None):
        super().__init__(int, 'SeqByte')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = int()
            val = _is.readByte()
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            _os.writeByte(val)

    def _fromJson(self, js):
        for js_c in js:
            self.append(js_c)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val)
        return res

# message.common.publicdef.SeqString
class SeqString(ListBase):
    def __init__(self, _data=None):
        super().__init__(str, 'SeqString')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = str()
            val = _is.readString()
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            _os.writeString(val)

    def _fromJson(self, js):
        for js_c in js:
            self.append(js_c)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val)
        return res

# message.common.publicdef.SeqDate
class SeqDate(ListBase):
    def __init__(self, _data=None):
        super().__init__(datetime.datetime, 'SeqDate')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = datetime.datetime.now()
            val = _is.readDate()
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            _os.writeDate(val)

    def _fromJson(self, js):
        for js_c in js:
            self.append(js_c)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val)
        return res

# message.common.publicdef.DictIntBool
class DictIntBool(DictBase):
    def __init__(self, _data=None):
        super().__init__(int, bool, 'DictIntBool')

        if _data:
            self.update(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = int()
            val_ = bool()
            key_ = _is.readInt()
            val_ = _is.readBool()
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeInt(item[0])
            _os.writeBool(item[1])

    def _fromJson(self, js):
        for key_ in js:
            self[key_] = js[key_] 

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]
        return res

# message.common.publicdef.DictIntInt
class DictIntInt(DictBase):
    def __init__(self, _data=None):
        super().__init__(int, int, 'DictIntInt')

        if _data:
            self.update(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = int()
            val_ = int()
            key_ = _is.readInt()
            val_ = _is.readInt()
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeInt(item[0])
            _os.writeInt(item[1])

    def _fromJson(self, js):
        for key_ in js:
            self[key_] = js[key_] 

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]
        return res

# message.common.publicdef.DictStringString
class DictStringString(DictBase):
    def __init__(self, _data=None):
        super().__init__(str, str, 'DictStringString')

        if _data:
            self.update(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = str()
            val_ = str()
            key_ = _is.readString()
            val_ = _is.readString()
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeString(item[0])
            _os.writeString(item[1])

    def _fromJson(self, js):
        for key_ in js:
            self[key_] = js[key_] 

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]
        return res

# message.common.publicdef.DictStringInt
class DictStringInt(DictBase):
    def __init__(self, _data=None):
        super().__init__(str, int, 'DictStringInt')

        if _data:
            self.update(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = str()
            val_ = int()
            key_ = _is.readString()
            val_ = _is.readInt()
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeString(item[0])
            _os.writeInt(item[1])

    def _fromJson(self, js):
        for key_ in js:
            self[key_] = js[key_] 

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]
        return res

# message.common.publicdef.DictIntString
class DictIntString(DictBase):
    def __init__(self, _data=None):
        super().__init__(int, str, 'DictIntString')

        if _data:
            self.update(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = int()
            val_ = str()
            key_ = _is.readInt()
            val_ = _is.readString()
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeInt(item[0])
            _os.writeString(item[1])

    def _fromJson(self, js):
        for key_ in js:
            self[key_] = js[key_] 

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]
        return res

# message.common.publicdef.DictStringBool
class DictStringBool(DictBase):
    def __init__(self, _data=None):
        super().__init__(str, bool, 'DictStringBool')

        if _data:
            self.update(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = str()
            val_ = bool()
            key_ = _is.readString()
            val_ = _is.readBool()
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeString(item[0])
            _os.writeBool(item[1])

    def _fromJson(self, js):
        for key_ in js:
            self[key_] = js[key_] 

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]
        return res

# message.common.publicdef.ESysTopicType
class ESysTopicType:
    PlatformTopic = 1
    BusinessTopic = 2
    Advertisement = 3

    @classmethod
    def isValueValid(cls, _val):
        if _val == cls.PlatformTopic:
            return True

        if _val == cls.BusinessTopic:
            return True

        if _val == cls.Advertisement:
            return True

        return False

# message.common.publicdef.ELoginType
class ELoginType:
    MobilePhoneNum = 1
    TencentQQ = 2
    WeChat = 3

    @classmethod
    def isValueValid(cls, _val):
        if _val == cls.MobilePhoneNum:
            return True

        if _val == cls.TencentQQ:
            return True

        if _val == cls.WeChat:
            return True

        return False

# message.common.publicdef.EGender
class EGender:
    Unknown = 0
    Male = 1
    Female = 2

    @classmethod
    def isValueValid(cls, _val):
        if _val == cls.Unknown:
            return True

        if _val == cls.Male:
            return True

        if _val == cls.Female:
            return True

        return False

# message.common.publicdef.EInteractiveType
class EInteractiveType:
    Upvote = 1
    Comment = 2
    Shared = 3

    @classmethod
    def isValueValid(cls, _val):
        if _val == cls.Upvote:
            return True

        if _val == cls.Comment:
            return True

        if _val == cls.Shared:
            return True

        return False

