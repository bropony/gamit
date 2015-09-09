#
# file: usertables.py
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


# message.db.mongodb.usertables.TUserBasic
class TUserBasic:
    __slots__ = dict()
    __slots__['userId'] = str
    __slots__['accountType'] = int
    __slots__['account'] = str
    __slots__['password'] = str
    __slots__['nickname'] = str
    __slots__['birthday'] = datetime.datetime
    __slots__['gender'] = int
    __slots__['avatar'] = str
    __slots__['bindPhoneNum'] = str
    __slots__['bindEmailAdress'] = str
    __slots__['createDt'] = datetime.datetime
    __slots__['createdWithDeviceCode'] = str

    # field names
    fn_userId = 'userId'
    fn_accountType = 'accountType'
    fn_account = 'account'
    fn_password = 'password'
    fn_nickname = 'nickname'
    fn_birthday = 'birthday'
    fn_gender = 'gender'
    fn_avatar = 'avatar'
    fn_bindPhoneNum = 'bindPhoneNum'
    fn_bindEmailAdress = 'bindEmailAdress'
    fn_createDt = 'createDt'
    fn_createdWithDeviceCode = 'createdWithDeviceCode'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TUserBasic.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userId: str
    type accountType: int
    type account: str
    type password: str
    type nickname: str
    type birthday: datetime.datetime
    type gender: int
    type avatar: str
    type bindPhoneNum: str
    type bindEmailAdress: str
    type createDt: datetime.datetime
    type createdWithDeviceCode: str
    """
    def __init__(self):
        self.userId = str()
        self.accountType = int()
        self.account = str()
        self.password = str()
        self.nickname = str()
        self.birthday = datetime.datetime.now()
        self.gender = int()
        self.avatar = str()
        self.bindPhoneNum = str()
        self.bindEmailAdress = str()
        self.createDt = datetime.datetime.now()
        self.createdWithDeviceCode = str()

    def _read(self, _is):
        self.userId = _is.readString()
        self.accountType = _is.readInt()
        self.account = _is.readString()
        self.password = _is.readString()
        self.nickname = _is.readString()
        self.birthday = _is.readDate()
        self.gender = _is.readInt()
        self.avatar = _is.readString()
        self.bindPhoneNum = _is.readString()
        self.bindEmailAdress = _is.readString()
        self.createDt = _is.readDate()
        self.createdWithDeviceCode = _is.readString()

    def _write(self, _os):
        _os.writeString(self.userId)
        _os.writeInt(self.accountType)
        _os.writeString(self.account)
        _os.writeString(self.password)
        _os.writeString(self.nickname)
        _os.writeDate(self.birthday)
        _os.writeInt(self.gender)
        _os.writeString(self.avatar)
        _os.writeString(self.bindPhoneNum)
        _os.writeString(self.bindEmailAdress)
        _os.writeDate(self.createDt)
        _os.writeString(self.createdWithDeviceCode)

    def _fromJson(self, js):
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'accountType' in js and isinstance(js['accountType'], int):
            self.accountType = js['accountType']
        if 'account' in js and isinstance(js['account'], str):
            self.account = js['account']
        if 'password' in js and isinstance(js['password'], str):
            self.password = js['password']
        if 'nickname' in js and isinstance(js['nickname'], str):
            self.nickname = js['nickname']
        if 'birthday' in js and isinstance(js['birthday'], datetime.datetime):
            self.birthday = js['birthday']
        elif 'birthday' in js and isinstance(self.birthday, datetime.datetime):
            self.birthday = datetime.datetime.strptime(js['birthday'], '%Y-%m-%d %H:%M:%S')
        if 'gender' in js and isinstance(js['gender'], int):
            self.gender = js['gender']
        if 'avatar' in js and isinstance(js['avatar'], str):
            self.avatar = js['avatar']
        if 'bindPhoneNum' in js and isinstance(js['bindPhoneNum'], str):
            self.bindPhoneNum = js['bindPhoneNum']
        if 'bindEmailAdress' in js and isinstance(js['bindEmailAdress'], str):
            self.bindEmailAdress = js['bindEmailAdress']
        if 'createDt' in js and isinstance(js['createDt'], datetime.datetime):
            self.createDt = js['createDt']
        elif 'createDt' in js and isinstance(self.createDt, datetime.datetime):
            self.createDt = datetime.datetime.strptime(js['createDt'], '%Y-%m-%d %H:%M:%S')
        if 'createdWithDeviceCode' in js and isinstance(js['createdWithDeviceCode'], str):
            self.createdWithDeviceCode = js['createdWithDeviceCode']

    def _toJson(self):
        js = dict()
        js['userId'] = self.userId
        js['accountType'] = self.accountType
        js['account'] = self.account
        js['password'] = self.password
        js['nickname'] = self.nickname
        js['birthday'] = self.birthday
        js['gender'] = self.gender
        js['avatar'] = self.avatar
        js['bindPhoneNum'] = self.bindPhoneNum
        js['bindEmailAdress'] = self.bindEmailAdress
        js['createDt'] = self.createDt
        js['createdWithDeviceCode'] = self.createdWithDeviceCode
        return js

MessageBlock.register(TUserBasic)

# message.db.mongodb.usertables.SeqTUserBasic
class SeqTUserBasic(ListBase):
    def __init__(self, _data=None):
        super().__init__(TUserBasic, 'SeqTUserBasic')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TUserBasic()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TUserBasic()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.db.mongodb.usertables.TUserSettings
class TUserSettings:
    __slots__ = dict()
    __slots__['userId'] = str
    __slots__['lastLoginDeviceCode'] = str
    __slots__['lastLoginDt'] = datetime.datetime
    __slots__['sessionKey'] = str

    # field names
    fn_userId = 'userId'
    fn_lastLoginDeviceCode = 'lastLoginDeviceCode'
    fn_lastLoginDt = 'lastLoginDt'
    fn_sessionKey = 'sessionKey'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TUserSettings.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userId: str
    type lastLoginDeviceCode: str
    type lastLoginDt: datetime.datetime
    type sessionKey: str
    """
    def __init__(self):
        self.userId = str()
        self.lastLoginDeviceCode = str()
        self.lastLoginDt = datetime.datetime.now()
        self.sessionKey = str()

    def _read(self, _is):
        self.userId = _is.readString()
        self.lastLoginDeviceCode = _is.readString()
        self.lastLoginDt = _is.readDate()
        self.sessionKey = _is.readString()

    def _write(self, _os):
        _os.writeString(self.userId)
        _os.writeString(self.lastLoginDeviceCode)
        _os.writeDate(self.lastLoginDt)
        _os.writeString(self.sessionKey)

    def _fromJson(self, js):
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'lastLoginDeviceCode' in js and isinstance(js['lastLoginDeviceCode'], str):
            self.lastLoginDeviceCode = js['lastLoginDeviceCode']
        if 'lastLoginDt' in js and isinstance(js['lastLoginDt'], datetime.datetime):
            self.lastLoginDt = js['lastLoginDt']
        elif 'lastLoginDt' in js and isinstance(self.lastLoginDt, datetime.datetime):
            self.lastLoginDt = datetime.datetime.strptime(js['lastLoginDt'], '%Y-%m-%d %H:%M:%S')
        if 'sessionKey' in js and isinstance(js['sessionKey'], str):
            self.sessionKey = js['sessionKey']

    def _toJson(self):
        js = dict()
        js['userId'] = self.userId
        js['lastLoginDeviceCode'] = self.lastLoginDeviceCode
        js['lastLoginDt'] = self.lastLoginDt
        js['sessionKey'] = self.sessionKey
        return js

MessageBlock.register(TUserSettings)

# message.db.mongodb.usertables.TUserAddress
class TUserAddress:
    __slots__ = dict()
    __slots__['userId'] = str
    __slots__['addressList'] = message.common.publicmsg.SeqAddress

    # field names
    fn_userId = 'userId'
    fn_addressList = 'addressList'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TUserAddress.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userId: str
    type addressList: list[message.common.publicmsg.SAddress]
    """
    def __init__(self):
        self.userId = str()
        self.addressList = message.common.publicmsg.SeqAddress()

    def _read(self, _is):
        self.userId = _is.readString()
        self.addressList._read(_is)

    def _write(self, _os):
        _os.writeString(self.userId)
        self.addressList._write(_os)

    def _fromJson(self, js):
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'addressList' in js and isinstance(js['addressList'], message.common.publicmsg.SeqAddress):
            self.addressList._fromJson(js['addressList'])
        elif 'addressList' in js and isinstance(js['addressList'], list):
            self.addressList._fromJson(js['addressList'])

    def _toJson(self):
        js = dict()
        js['userId'] = self.userId
        js['addressList'] = self.addressList._toJson()
        return js

MessageBlock.register(TUserAddress)

# message.db.mongodb.usertables.SeqTUserSettings
class SeqTUserSettings(ListBase):
    def __init__(self, _data=None):
        super().__init__(TUserSettings, 'SeqTUserSettings')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TUserSettings()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TUserSettings()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.db.mongodb.usertables.TUserProperty
class TUserProperty:
    __slots__ = dict()
    __slots__['userId'] = str
    __slots__['vipLevel'] = int
    __slots__['goldBean'] = int
    __slots__['postNum'] = int
    __slots__['fanNum'] = int
    __slots__['focusNum'] = int

    # field names
    fn_userId = 'userId'
    fn_vipLevel = 'vipLevel'
    fn_goldBean = 'goldBean'
    fn_postNum = 'postNum'
    fn_fanNum = 'fanNum'
    fn_focusNum = 'focusNum'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TUserProperty.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userId: str
    type vipLevel: int
    type goldBean: int
    type postNum: int
    type fanNum: int
    type focusNum: int
    """
    def __init__(self):
        self.userId = str()
        self.vipLevel = int()
        self.goldBean = int()
        self.postNum = int()
        self.fanNum = int()
        self.focusNum = int()

    def _read(self, _is):
        self.userId = _is.readString()
        self.vipLevel = _is.readInt()
        self.goldBean = _is.readInt()
        self.postNum = _is.readInt()
        self.fanNum = _is.readInt()
        self.focusNum = _is.readInt()

    def _write(self, _os):
        _os.writeString(self.userId)
        _os.writeInt(self.vipLevel)
        _os.writeInt(self.goldBean)
        _os.writeInt(self.postNum)
        _os.writeInt(self.fanNum)
        _os.writeInt(self.focusNum)

    def _fromJson(self, js):
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'vipLevel' in js and isinstance(js['vipLevel'], int):
            self.vipLevel = js['vipLevel']
        if 'goldBean' in js and isinstance(js['goldBean'], int):
            self.goldBean = js['goldBean']
        if 'postNum' in js and isinstance(js['postNum'], int):
            self.postNum = js['postNum']
        if 'fanNum' in js and isinstance(js['fanNum'], int):
            self.fanNum = js['fanNum']
        if 'focusNum' in js and isinstance(js['focusNum'], int):
            self.focusNum = js['focusNum']

    def _toJson(self):
        js = dict()
        js['userId'] = self.userId
        js['vipLevel'] = self.vipLevel
        js['goldBean'] = self.goldBean
        js['postNum'] = self.postNum
        js['fanNum'] = self.fanNum
        js['focusNum'] = self.focusNum
        return js

MessageBlock.register(TUserProperty)

# message.db.mongodb.usertables.SeqTUserProperty
class SeqTUserProperty(ListBase):
    def __init__(self, _data=None):
        super().__init__(TUserProperty, 'SeqTUserProperty')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TUserProperty()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TUserProperty()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.db.mongodb.usertables.TFamilyMember
class TFamilyMember:
    __slots__ = dict()
    __slots__['userId'] = str
    __slots__['index'] = int
    __slots__['member'] = str
    __slots__['name'] = str
    __slots__['gender'] = int
    __slots__['birthday'] = datetime.datetime
    __slots__['height'] = float
    __slots__['weight'] = float
    __slots__['bust'] = float
    __slots__['waistline'] = float
    __slots__['hipline'] = float
    __slots__['brachium'] = float
    __slots__['leglength'] = float
    __slots__['shoulder'] = float

    # field names
    fn_userId = 'userId'
    fn_index = 'index'
    fn_member = 'member'
    fn_name = 'name'
    fn_gender = 'gender'
    fn_birthday = 'birthday'
    fn_height = 'height'
    fn_weight = 'weight'
    fn_bust = 'bust'
    fn_waistline = 'waistline'
    fn_hipline = 'hipline'
    fn_brachium = 'brachium'
    fn_leglength = 'leglength'
    fn_shoulder = 'shoulder'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TFamilyMember.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userId: str
    type index: int
    type member: str
    type name: str
    type gender: int
    type birthday: datetime.datetime
    type height: float
    type weight: float
    type bust: float
    type waistline: float
    type hipline: float
    type brachium: float
    type leglength: float
    type shoulder: float
    """
    def __init__(self):
        self.userId = str()
        self.index = int()
        self.member = str()
        self.name = str()
        self.gender = int()
        self.birthday = datetime.datetime.now()
        self.height = float()
        self.weight = float()
        self.bust = float()
        self.waistline = float()
        self.hipline = float()
        self.brachium = float()
        self.leglength = float()
        self.shoulder = float()

    def _read(self, _is):
        self.userId = _is.readString()
        self.index = _is.readInt()
        self.member = _is.readString()
        self.name = _is.readString()
        self.gender = _is.readInt()
        self.birthday = _is.readDate()
        self.height = _is.readFloat()
        self.weight = _is.readFloat()
        self.bust = _is.readFloat()
        self.waistline = _is.readFloat()
        self.hipline = _is.readFloat()
        self.brachium = _is.readFloat()
        self.leglength = _is.readFloat()
        self.shoulder = _is.readFloat()

    def _write(self, _os):
        _os.writeString(self.userId)
        _os.writeInt(self.index)
        _os.writeString(self.member)
        _os.writeString(self.name)
        _os.writeInt(self.gender)
        _os.writeDate(self.birthday)
        _os.writeFloat(self.height)
        _os.writeFloat(self.weight)
        _os.writeFloat(self.bust)
        _os.writeFloat(self.waistline)
        _os.writeFloat(self.hipline)
        _os.writeFloat(self.brachium)
        _os.writeFloat(self.leglength)
        _os.writeFloat(self.shoulder)

    def _fromJson(self, js):
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'index' in js and isinstance(js['index'], int):
            self.index = js['index']
        if 'member' in js and isinstance(js['member'], str):
            self.member = js['member']
        if 'name' in js and isinstance(js['name'], str):
            self.name = js['name']
        if 'gender' in js and isinstance(js['gender'], int):
            self.gender = js['gender']
        if 'birthday' in js and isinstance(js['birthday'], datetime.datetime):
            self.birthday = js['birthday']
        elif 'birthday' in js and isinstance(self.birthday, datetime.datetime):
            self.birthday = datetime.datetime.strptime(js['birthday'], '%Y-%m-%d %H:%M:%S')
        if 'height' in js and isinstance(js['height'], float):
            self.height = js['height']
        if 'weight' in js and isinstance(js['weight'], float):
            self.weight = js['weight']
        if 'bust' in js and isinstance(js['bust'], float):
            self.bust = js['bust']
        if 'waistline' in js and isinstance(js['waistline'], float):
            self.waistline = js['waistline']
        if 'hipline' in js and isinstance(js['hipline'], float):
            self.hipline = js['hipline']
        if 'brachium' in js and isinstance(js['brachium'], float):
            self.brachium = js['brachium']
        if 'leglength' in js and isinstance(js['leglength'], float):
            self.leglength = js['leglength']
        if 'shoulder' in js and isinstance(js['shoulder'], float):
            self.shoulder = js['shoulder']

    def _toJson(self):
        js = dict()
        js['userId'] = self.userId
        js['index'] = self.index
        js['member'] = self.member
        js['name'] = self.name
        js['gender'] = self.gender
        js['birthday'] = self.birthday
        js['height'] = self.height
        js['weight'] = self.weight
        js['bust'] = self.bust
        js['waistline'] = self.waistline
        js['hipline'] = self.hipline
        js['brachium'] = self.brachium
        js['leglength'] = self.leglength
        js['shoulder'] = self.shoulder
        return js

MessageBlock.register(TFamilyMember)

# message.db.mongodb.usertables.SeqTFamilyMember
class SeqTFamilyMember(ListBase):
    def __init__(self, _data=None):
        super().__init__(TFamilyMember, 'SeqTFamilyMember')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TFamilyMember()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TFamilyMember()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.db.mongodb.usertables.TUserImage
class TUserImage:
    __slots__ = dict()
    __slots__['userId'] = str
    __slots__['imgKey'] = str
    __slots__['createDt'] = datetime.datetime
    __slots__['isUploaded'] = bool

    # field names
    fn_userId = 'userId'
    fn_imgKey = 'imgKey'
    fn_createDt = 'createDt'
    fn_isUploaded = 'isUploaded'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TUserImage.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userId: str
    type imgKey: str
    type createDt: datetime.datetime
    type isUploaded: bool
    """
    def __init__(self):
        self.userId = str()
        self.imgKey = str()
        self.createDt = datetime.datetime.now()
        self.isUploaded = bool()

    def _read(self, _is):
        self.userId = _is.readString()
        self.imgKey = _is.readString()
        self.createDt = _is.readDate()
        self.isUploaded = _is.readBool()

    def _write(self, _os):
        _os.writeString(self.userId)
        _os.writeString(self.imgKey)
        _os.writeDate(self.createDt)
        _os.writeBool(self.isUploaded)

    def _fromJson(self, js):
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'imgKey' in js and isinstance(js['imgKey'], str):
            self.imgKey = js['imgKey']
        if 'createDt' in js and isinstance(js['createDt'], datetime.datetime):
            self.createDt = js['createDt']
        elif 'createDt' in js and isinstance(self.createDt, datetime.datetime):
            self.createDt = datetime.datetime.strptime(js['createDt'], '%Y-%m-%d %H:%M:%S')
        if 'isUploaded' in js and isinstance(js['isUploaded'], bool):
            self.isUploaded = js['isUploaded']

    def _toJson(self):
        js = dict()
        js['userId'] = self.userId
        js['imgKey'] = self.imgKey
        js['createDt'] = self.createDt
        js['isUploaded'] = self.isUploaded
        return js

MessageBlock.register(TUserImage)

# message.db.mongodb.usertables.SeqTUserImage
class SeqTUserImage(ListBase):
    def __init__(self, _data=None):
        super().__init__(TUserImage, 'SeqTUserImage')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TUserImage()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TUserImage()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.db.mongodb.usertables.TUserFan
class TUserFan:
    __slots__ = dict()
    __slots__['recordId'] = str
    __slots__['fanUserId'] = str
    __slots__['myUserId'] = str
    __slots__['createDt'] = datetime.datetime

    # field names
    fn_recordId = 'recordId'
    fn_fanUserId = 'fanUserId'
    fn_myUserId = 'myUserId'
    fn_createDt = 'createDt'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TUserFan.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type recordId: str
    type fanUserId: str
    type myUserId: str
    type createDt: datetime.datetime
    """
    def __init__(self):
        self.recordId = str()
        self.fanUserId = str()
        self.myUserId = str()
        self.createDt = datetime.datetime.now()

    def _read(self, _is):
        self.recordId = _is.readString()
        self.fanUserId = _is.readString()
        self.myUserId = _is.readString()
        self.createDt = _is.readDate()

    def _write(self, _os):
        _os.writeString(self.recordId)
        _os.writeString(self.fanUserId)
        _os.writeString(self.myUserId)
        _os.writeDate(self.createDt)

    def _fromJson(self, js):
        if 'recordId' in js and isinstance(js['recordId'], str):
            self.recordId = js['recordId']
        if 'fanUserId' in js and isinstance(js['fanUserId'], str):
            self.fanUserId = js['fanUserId']
        if 'myUserId' in js and isinstance(js['myUserId'], str):
            self.myUserId = js['myUserId']
        if 'createDt' in js and isinstance(js['createDt'], datetime.datetime):
            self.createDt = js['createDt']
        elif 'createDt' in js and isinstance(self.createDt, datetime.datetime):
            self.createDt = datetime.datetime.strptime(js['createDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['recordId'] = self.recordId
        js['fanUserId'] = self.fanUserId
        js['myUserId'] = self.myUserId
        js['createDt'] = self.createDt
        return js

MessageBlock.register(TUserFan)

# message.db.mongodb.usertables.SeqTUserFan
class SeqTUserFan(ListBase):
    def __init__(self, _data=None):
        super().__init__(TUserFan, 'SeqTUserFan')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TUserFan()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TUserFan()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

