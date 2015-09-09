#
# file: publicmsg.py
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


# message.common.publicmsg.SAddress
class SAddress:
    __slots__ = dict()
    __slots__['addressIndex'] = int
    __slots__['countryCode'] = str
    __slots__['country'] = str
    __slots__['province'] = str
    __slots__['city'] = str
    __slots__['district'] = str
    __slots__['details'] = str
    __slots__['recipientName'] = str
    __slots__['recipientPhoneNum'] = str
    __slots__['postCode'] = str
    __slots__['isDefault'] = bool
    __slots__['altitude'] = float
    __slots__['longitude'] = float

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SAddress.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type addressIndex: int
    type countryCode: str
    type country: str
    type province: str
    type city: str
    type district: str
    type details: str
    type recipientName: str
    type recipientPhoneNum: str
    type postCode: str
    type isDefault: bool
    type altitude: float
    type longitude: float
    """
    def __init__(self):
        self.addressIndex = int()
        self.countryCode = str()
        self.country = str()
        self.province = str()
        self.city = str()
        self.district = str()
        self.details = str()
        self.recipientName = str()
        self.recipientPhoneNum = str()
        self.postCode = str()
        self.isDefault = bool()
        self.altitude = float()
        self.longitude = float()

    def _read(self, _is):
        self.addressIndex = _is.readInt()
        self.countryCode = _is.readString()
        self.country = _is.readString()
        self.province = _is.readString()
        self.city = _is.readString()
        self.district = _is.readString()
        self.details = _is.readString()
        self.recipientName = _is.readString()
        self.recipientPhoneNum = _is.readString()
        self.postCode = _is.readString()
        self.isDefault = _is.readBool()
        self.altitude = _is.readDouble()
        self.longitude = _is.readDouble()

    def _write(self, _os):
        _os.writeInt(self.addressIndex)
        _os.writeString(self.countryCode)
        _os.writeString(self.country)
        _os.writeString(self.province)
        _os.writeString(self.city)
        _os.writeString(self.district)
        _os.writeString(self.details)
        _os.writeString(self.recipientName)
        _os.writeString(self.recipientPhoneNum)
        _os.writeString(self.postCode)
        _os.writeBool(self.isDefault)
        _os.writeDouble(self.altitude)
        _os.writeDouble(self.longitude)

    def _fromJson(self, js):
        if 'addressIndex' in js and isinstance(js['addressIndex'], int):
            self.addressIndex = js['addressIndex']
        if 'countryCode' in js and isinstance(js['countryCode'], str):
            self.countryCode = js['countryCode']
        if 'country' in js and isinstance(js['country'], str):
            self.country = js['country']
        if 'province' in js and isinstance(js['province'], str):
            self.province = js['province']
        if 'city' in js and isinstance(js['city'], str):
            self.city = js['city']
        if 'district' in js and isinstance(js['district'], str):
            self.district = js['district']
        if 'details' in js and isinstance(js['details'], str):
            self.details = js['details']
        if 'recipientName' in js and isinstance(js['recipientName'], str):
            self.recipientName = js['recipientName']
        if 'recipientPhoneNum' in js and isinstance(js['recipientPhoneNum'], str):
            self.recipientPhoneNum = js['recipientPhoneNum']
        if 'postCode' in js and isinstance(js['postCode'], str):
            self.postCode = js['postCode']
        if 'isDefault' in js and isinstance(js['isDefault'], bool):
            self.isDefault = js['isDefault']
        if 'altitude' in js and isinstance(js['altitude'], float):
            self.altitude = js['altitude']
        if 'longitude' in js and isinstance(js['longitude'], float):
            self.longitude = js['longitude']

    def _toJson(self):
        js = dict()
        js['addressIndex'] = self.addressIndex
        js['countryCode'] = self.countryCode
        js['country'] = self.country
        js['province'] = self.province
        js['city'] = self.city
        js['district'] = self.district
        js['details'] = self.details
        js['recipientName'] = self.recipientName
        js['recipientPhoneNum'] = self.recipientPhoneNum
        js['postCode'] = self.postCode
        js['isDefault'] = self.isDefault
        js['altitude'] = self.altitude
        js['longitude'] = self.longitude
        return js

MessageBlock.register(SAddress)

# message.common.publicmsg.SeqAddress
class SeqAddress(ListBase):
    def __init__(self, _data=None):
        super().__init__(SAddress, 'SeqAddress')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SAddress()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SAddress()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

