#
# file: dataview.py
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
import message.db.mongodb.usertables


# message.db.dataview.SUserDataView
class SUserDataView:
    __slots__ = dict()
    __slots__['basicInfo'] = message.db.mongodb.usertables.TUserBasic
    __slots__['userSettings'] = message.db.mongodb.usertables.TUserSettings
    __slots__['userProperty'] = message.db.mongodb.usertables.TUserProperty
    __slots__['userAddress'] = message.db.mongodb.usertables.TUserAddress
    __slots__['familyMembers'] = message.db.mongodb.usertables.SeqTFamilyMember

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SUserDataView.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type basicInfo: message.db.mongodb.usertables.TUserBasic
    type userSettings: message.db.mongodb.usertables.TUserSettings
    type userProperty: message.db.mongodb.usertables.TUserProperty
    type userAddress: message.db.mongodb.usertables.TUserAddress
    type familyMembers: list[message.db.mongodb.usertables.TFamilyMember]
    """
    def __init__(self):
        self.basicInfo = message.db.mongodb.usertables.TUserBasic()
        self.userSettings = message.db.mongodb.usertables.TUserSettings()
        self.userProperty = message.db.mongodb.usertables.TUserProperty()
        self.userAddress = message.db.mongodb.usertables.TUserAddress()
        self.familyMembers = message.db.mongodb.usertables.SeqTFamilyMember()

    def _read(self, _is):
        self.basicInfo._read(_is)
        self.userSettings._read(_is)
        self.userProperty._read(_is)
        self.userAddress._read(_is)
        self.familyMembers._read(_is)

    def _write(self, _os):
        self.basicInfo._write(_os)
        self.userSettings._write(_os)
        self.userProperty._write(_os)
        self.userAddress._write(_os)
        self.familyMembers._write(_os)

    def _fromJson(self, js):
        if 'basicInfo' in js and isinstance(js['basicInfo'], message.db.mongodb.usertables.TUserBasic):
            self.basicInfo._fromJson(js['basicInfo'])
        if 'userSettings' in js and isinstance(js['userSettings'], message.db.mongodb.usertables.TUserSettings):
            self.userSettings._fromJson(js['userSettings'])
        if 'userProperty' in js and isinstance(js['userProperty'], message.db.mongodb.usertables.TUserProperty):
            self.userProperty._fromJson(js['userProperty'])
        if 'userAddress' in js and isinstance(js['userAddress'], message.db.mongodb.usertables.TUserAddress):
            self.userAddress._fromJson(js['userAddress'])
        if 'familyMembers' in js and isinstance(js['familyMembers'], message.db.mongodb.usertables.SeqTFamilyMember):
            self.familyMembers._fromJson(js['familyMembers'])
        elif 'familyMembers' in js and isinstance(js['familyMembers'], list):
            self.familyMembers._fromJson(js['familyMembers'])

    def _toJson(self):
        js = dict()
        js['basicInfo'] = self.basicInfo._toJson()
        js['userSettings'] = self.userSettings._toJson()
        js['userProperty'] = self.userProperty._toJson()
        js['userAddress'] = self.userAddress._toJson()
        js['familyMembers'] = self.familyMembers._toJson()
        return js

MessageBlock.register(SUserDataView)

# message.db.dataview.SeqUserDataView
class SeqUserDataView(ListBase):
    def __init__(self, _data=None):
        super().__init__(SUserDataView, 'SeqUserDataView')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SUserDataView()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SUserDataView()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

