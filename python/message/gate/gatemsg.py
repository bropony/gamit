#
# file: gatemsg.py
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


# message.gate.gatemsg.SUserBrief
class SUserBrief:
    __slots__ = dict()
    __slots__['userId'] = str
    __slots__['nickname'] = str
    __slots__['avatarUrl'] = str

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SUserBrief.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userId: str
    type nickname: str
    type avatarUrl: str
    """
    def __init__(self):
        self.userId = str()
        self.nickname = str()
        self.avatarUrl = str()

    def _read(self, _is):
        self.userId = _is.readString()
        self.nickname = _is.readString()
        self.avatarUrl = _is.readString()

    def _write(self, _os):
        _os.writeString(self.userId)
        _os.writeString(self.nickname)
        _os.writeString(self.avatarUrl)

    def _fromJson(self, js):
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'nickname' in js and isinstance(js['nickname'], str):
            self.nickname = js['nickname']
        if 'avatarUrl' in js and isinstance(js['avatarUrl'], str):
            self.avatarUrl = js['avatarUrl']

    def _toJson(self):
        js = dict()
        js['userId'] = self.userId
        js['nickname'] = self.nickname
        js['avatarUrl'] = self.avatarUrl
        return js

MessageBlock.register(SUserBrief)

# message.gate.gatemsg.SeqUserBrief
class SeqUserBrief(ListBase):
    def __init__(self, _data=None):
        super().__init__(SUserBrief, 'SeqUserBrief')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SUserBrief()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SUserBrief()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.gate.gatemsg.SUserBriefWithoutAvatar
class SUserBriefWithoutAvatar:
    __slots__ = dict()
    __slots__['userId'] = str
    __slots__['nickName'] = str

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SUserBriefWithoutAvatar.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userId: str
    type nickName: str
    """
    def __init__(self):
        self.userId = str()
        self.nickName = str()

    def _read(self, _is):
        self.userId = _is.readString()
        self.nickName = _is.readString()

    def _write(self, _os):
        _os.writeString(self.userId)
        _os.writeString(self.nickName)

    def _fromJson(self, js):
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'nickName' in js and isinstance(js['nickName'], str):
            self.nickName = js['nickName']

    def _toJson(self):
        js = dict()
        js['userId'] = self.userId
        js['nickName'] = self.nickName
        return js

MessageBlock.register(SUserBriefWithoutAvatar)

# message.gate.gatemsg.SeqUserBriefWithoutAvatar
class SeqUserBriefWithoutAvatar(ListBase):
    def __init__(self, _data=None):
        super().__init__(SUserBriefWithoutAvatar, 'SeqUserBriefWithoutAvatar')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SUserBriefWithoutAvatar()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SUserBriefWithoutAvatar()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.gate.gatemsg.SMyDetailInfo
class SMyDetailInfo:
    __slots__ = dict()
    __slots__['vipLevel'] = int
    __slots__['goldBean'] = int
    __slots__['postNum'] = int
    __slots__['fanNum'] = int
    __slots__['focusNum'] = int

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SMyDetailInfo.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type vipLevel: int
    type goldBean: int
    type postNum: int
    type fanNum: int
    type focusNum: int
    """
    def __init__(self):
        self.vipLevel = int()
        self.goldBean = int()
        self.postNum = int()
        self.fanNum = int()
        self.focusNum = int()

    def _read(self, _is):
        self.vipLevel = _is.readInt()
        self.goldBean = _is.readInt()
        self.postNum = _is.readInt()
        self.fanNum = _is.readInt()
        self.focusNum = _is.readInt()

    def _write(self, _os):
        _os.writeInt(self.vipLevel)
        _os.writeInt(self.goldBean)
        _os.writeInt(self.postNum)
        _os.writeInt(self.fanNum)
        _os.writeInt(self.focusNum)

    def _fromJson(self, js):
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
        js['vipLevel'] = self.vipLevel
        js['goldBean'] = self.goldBean
        js['postNum'] = self.postNum
        js['fanNum'] = self.fanNum
        js['focusNum'] = self.focusNum
        return js

MessageBlock.register(SMyDetailInfo)

# message.gate.gatemsg.SLogin
class SLogin:
    __slots__ = dict()
    __slots__['deviceCode'] = str
    __slots__['loginType'] = int
    __slots__['account'] = str
    __slots__['password'] = str

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SLogin.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type deviceCode: str
    type loginType: int
    type account: str
    type password: str
    """
    def __init__(self):
        self.deviceCode = str()
        self.loginType = message.common.publicdef.ELoginType.MobilePhoneNum
        self.account = str()
        self.password = str()

    def _read(self, _is):
        self.deviceCode = _is.readString()
        self.loginType = _is.readInt()
        self.account = _is.readString()
        self.password = _is.readString()

    def _write(self, _os):
        _os.writeString(self.deviceCode)
        _os.writeInt(self.loginType)
        _os.writeString(self.account)
        _os.writeString(self.password)

    def _fromJson(self, js):
        if 'deviceCode' in js and isinstance(js['deviceCode'], str):
            self.deviceCode = js['deviceCode']
        if 'loginType' in js and isinstance(js['loginType'], int):
            self.loginType = js['loginType']
        if 'account' in js and isinstance(js['account'], str):
            self.account = js['account']
        if 'password' in js and isinstance(js['password'], str):
            self.password = js['password']

    def _toJson(self):
        js = dict()
        js['deviceCode'] = self.deviceCode
        js['loginType'] = self.loginType
        js['account'] = self.account
        js['password'] = self.password
        return js

MessageBlock.register(SLogin)

# message.gate.gatemsg.SSignup
class SSignup:
    __slots__ = dict()
    __slots__['deviceCode'] = str
    __slots__['loginType'] = int
    __slots__['account'] = str
    __slots__['password'] = str
    __slots__['nickname'] = str
    __slots__['validationCode'] = str
    __slots__['invitationCode'] = str

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SSignup.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type deviceCode: str
    type loginType: int
    type account: str
    type password: str
    type nickname: str
    type validationCode: str
    type invitationCode: str
    """
    def __init__(self):
        self.deviceCode = str()
        self.loginType = message.common.publicdef.ELoginType.MobilePhoneNum
        self.account = str()
        self.password = str()
        self.nickname = str()
        self.validationCode = str()
        self.invitationCode = str()

    def _read(self, _is):
        self.deviceCode = _is.readString()
        self.loginType = _is.readInt()
        self.account = _is.readString()
        self.password = _is.readString()
        self.nickname = _is.readString()
        self.validationCode = _is.readString()
        self.invitationCode = _is.readString()

    def _write(self, _os):
        _os.writeString(self.deviceCode)
        _os.writeInt(self.loginType)
        _os.writeString(self.account)
        _os.writeString(self.password)
        _os.writeString(self.nickname)
        _os.writeString(self.validationCode)
        _os.writeString(self.invitationCode)

    def _fromJson(self, js):
        if 'deviceCode' in js and isinstance(js['deviceCode'], str):
            self.deviceCode = js['deviceCode']
        if 'loginType' in js and isinstance(js['loginType'], int):
            self.loginType = js['loginType']
        if 'account' in js and isinstance(js['account'], str):
            self.account = js['account']
        if 'password' in js and isinstance(js['password'], str):
            self.password = js['password']
        if 'nickname' in js and isinstance(js['nickname'], str):
            self.nickname = js['nickname']
        if 'validationCode' in js and isinstance(js['validationCode'], str):
            self.validationCode = js['validationCode']
        if 'invitationCode' in js and isinstance(js['invitationCode'], str):
            self.invitationCode = js['invitationCode']

    def _toJson(self):
        js = dict()
        js['deviceCode'] = self.deviceCode
        js['loginType'] = self.loginType
        js['account'] = self.account
        js['password'] = self.password
        js['nickname'] = self.nickname
        js['validationCode'] = self.validationCode
        js['invitationCode'] = self.invitationCode
        return js

MessageBlock.register(SSignup)

# message.gate.gatemsg.SLoginReturn
class SLoginReturn:
    __slots__ = dict()
    __slots__['sessionKey'] = str
    __slots__['userId'] = str
    __slots__['nickname'] = str
    __slots__['avatarUrl'] = str
    __slots__['gender'] = int
    __slots__['birthday'] = datetime.datetime

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SLoginReturn.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type sessionKey: str
    type userId: str
    type nickname: str
    type avatarUrl: str
    type gender: int
    type birthday: datetime.datetime
    """
    def __init__(self):
        self.sessionKey = str()
        self.userId = str()
        self.nickname = str()
        self.avatarUrl = str()
        self.gender = message.common.publicdef.EGender.Unknown
        self.birthday = datetime.datetime.now()

    def _read(self, _is):
        self.sessionKey = _is.readString()
        self.userId = _is.readString()
        self.nickname = _is.readString()
        self.avatarUrl = _is.readString()
        self.gender = _is.readInt()
        self.birthday = _is.readDate()

    def _write(self, _os):
        _os.writeString(self.sessionKey)
        _os.writeString(self.userId)
        _os.writeString(self.nickname)
        _os.writeString(self.avatarUrl)
        _os.writeInt(self.gender)
        _os.writeDate(self.birthday)

    def _fromJson(self, js):
        if 'sessionKey' in js and isinstance(js['sessionKey'], str):
            self.sessionKey = js['sessionKey']
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'nickname' in js and isinstance(js['nickname'], str):
            self.nickname = js['nickname']
        if 'avatarUrl' in js and isinstance(js['avatarUrl'], str):
            self.avatarUrl = js['avatarUrl']
        if 'gender' in js and isinstance(js['gender'], int):
            self.gender = js['gender']
        if 'birthday' in js and isinstance(js['birthday'], datetime.datetime):
            self.birthday = js['birthday']
        elif 'birthday' in js and isinstance(self.birthday, datetime.datetime):
            self.birthday = datetime.datetime.strptime(js['birthday'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['sessionKey'] = self.sessionKey
        js['userId'] = self.userId
        js['nickname'] = self.nickname
        js['avatarUrl'] = self.avatarUrl
        js['gender'] = self.gender
        js['birthday'] = self.birthday
        return js

MessageBlock.register(SLoginReturn)

# message.gate.gatemsg.SFamilyMember
class SFamilyMember:
    __slots__ = dict()
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

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SFamilyMember.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
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

MessageBlock.register(SFamilyMember)

# message.gate.gatemsg.SeqFamilyMember
class SeqFamilyMember(ListBase):
    def __init__(self, _data=None):
        super().__init__(SFamilyMember, 'SeqFamilyMember')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SFamilyMember()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SFamilyMember()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.gate.gatemsg.SImageInfo
class SImageInfo:
    __slots__ = dict()
    __slots__['imageKey'] = str
    __slots__['token'] = str
    __slots__['formatedDownloadUrl'] = str
    __slots__['expireDt'] = datetime.datetime

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SImageInfo.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type imageKey: str
    type token: str
    type formatedDownloadUrl: str
    type expireDt: datetime.datetime
    """
    def __init__(self):
        self.imageKey = str()
        self.token = str()
        self.formatedDownloadUrl = str()
        self.expireDt = datetime.datetime.now()

    def _read(self, _is):
        self.imageKey = _is.readString()
        self.token = _is.readString()
        self.formatedDownloadUrl = _is.readString()
        self.expireDt = _is.readDate()

    def _write(self, _os):
        _os.writeString(self.imageKey)
        _os.writeString(self.token)
        _os.writeString(self.formatedDownloadUrl)
        _os.writeDate(self.expireDt)

    def _fromJson(self, js):
        if 'imageKey' in js and isinstance(js['imageKey'], str):
            self.imageKey = js['imageKey']
        if 'token' in js and isinstance(js['token'], str):
            self.token = js['token']
        if 'formatedDownloadUrl' in js and isinstance(js['formatedDownloadUrl'], str):
            self.formatedDownloadUrl = js['formatedDownloadUrl']
        if 'expireDt' in js and isinstance(js['expireDt'], datetime.datetime):
            self.expireDt = js['expireDt']
        elif 'expireDt' in js and isinstance(self.expireDt, datetime.datetime):
            self.expireDt = datetime.datetime.strptime(js['expireDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['imageKey'] = self.imageKey
        js['token'] = self.token
        js['formatedDownloadUrl'] = self.formatedDownloadUrl
        js['expireDt'] = self.expireDt
        return js

MessageBlock.register(SImageInfo)

# message.gate.gatemsg.SeqImageInfo
class SeqImageInfo(ListBase):
    def __init__(self, _data=None):
        super().__init__(SImageInfo, 'SeqImageInfo')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SImageInfo()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SImageInfo()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.gate.gatemsg.SSysTopic
class SSysTopic:
    __slots__ = dict()
    __slots__['topicId'] = str
    __slots__['topicType'] = int
    __slots__['publisherId'] = str
    __slots__['title'] = str
    __slots__['content'] = str
    __slots__['images'] = SeqImageInfo
    __slots__['tags'] = message.common.publicdef.SeqString
    __slots__['createDt'] = datetime.datetime
    __slots__['sharedTimes'] = int
    __slots__['commentedTimes'] = int
    __slots__['upvotedTimes'] = int
    __slots__['viewTimes'] = int

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SSysTopic.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type topicId: str
    type topicType: int
    type publisherId: str
    type title: str
    type content: str
    type images: list[message.gate.gatemsg.SImageInfo]
    type tags: list[str]
    type createDt: datetime.datetime
    type sharedTimes: int
    type commentedTimes: int
    type upvotedTimes: int
    type viewTimes: int
    """
    def __init__(self):
        self.topicId = str()
        self.topicType = message.common.publicdef.ESysTopicType.PlatformTopic
        self.publisherId = str()
        self.title = str()
        self.content = str()
        self.images = SeqImageInfo()
        self.tags = message.common.publicdef.SeqString()
        self.createDt = datetime.datetime.now()
        self.sharedTimes = int()
        self.commentedTimes = int()
        self.upvotedTimes = int()
        self.viewTimes = int()

    def _read(self, _is):
        self.topicId = _is.readString()
        self.topicType = _is.readInt()
        self.publisherId = _is.readString()
        self.title = _is.readString()
        self.content = _is.readString()
        self.images._read(_is)
        self.tags._read(_is)
        self.createDt = _is.readDate()
        self.sharedTimes = _is.readInt()
        self.commentedTimes = _is.readInt()
        self.upvotedTimes = _is.readInt()
        self.viewTimes = _is.readInt()

    def _write(self, _os):
        _os.writeString(self.topicId)
        _os.writeInt(self.topicType)
        _os.writeString(self.publisherId)
        _os.writeString(self.title)
        _os.writeString(self.content)
        self.images._write(_os)
        self.tags._write(_os)
        _os.writeDate(self.createDt)
        _os.writeInt(self.sharedTimes)
        _os.writeInt(self.commentedTimes)
        _os.writeInt(self.upvotedTimes)
        _os.writeInt(self.viewTimes)

    def _fromJson(self, js):
        if 'topicId' in js and isinstance(js['topicId'], str):
            self.topicId = js['topicId']
        if 'topicType' in js and isinstance(js['topicType'], int):
            self.topicType = js['topicType']
        if 'publisherId' in js and isinstance(js['publisherId'], str):
            self.publisherId = js['publisherId']
        if 'title' in js and isinstance(js['title'], str):
            self.title = js['title']
        if 'content' in js and isinstance(js['content'], str):
            self.content = js['content']
        if 'images' in js and isinstance(js['images'], SeqImageInfo):
            self.images._fromJson(js['images'])
        elif 'images' in js and isinstance(js['images'], list):
            self.images._fromJson(js['images'])
        if 'tags' in js and isinstance(js['tags'], message.common.publicdef.SeqString):
            self.tags._fromJson(js['tags'])
        elif 'tags' in js and isinstance(js['tags'], list):
            self.tags._fromJson(js['tags'])
        if 'createDt' in js and isinstance(js['createDt'], datetime.datetime):
            self.createDt = js['createDt']
        elif 'createDt' in js and isinstance(self.createDt, datetime.datetime):
            self.createDt = datetime.datetime.strptime(js['createDt'], '%Y-%m-%d %H:%M:%S')
        if 'sharedTimes' in js and isinstance(js['sharedTimes'], int):
            self.sharedTimes = js['sharedTimes']
        if 'commentedTimes' in js and isinstance(js['commentedTimes'], int):
            self.commentedTimes = js['commentedTimes']
        if 'upvotedTimes' in js and isinstance(js['upvotedTimes'], int):
            self.upvotedTimes = js['upvotedTimes']
        if 'viewTimes' in js and isinstance(js['viewTimes'], int):
            self.viewTimes = js['viewTimes']

    def _toJson(self):
        js = dict()
        js['topicId'] = self.topicId
        js['topicType'] = self.topicType
        js['publisherId'] = self.publisherId
        js['title'] = self.title
        js['content'] = self.content
        js['images'] = self.images._toJson()
        js['tags'] = self.tags._toJson()
        js['createDt'] = self.createDt
        js['sharedTimes'] = self.sharedTimes
        js['commentedTimes'] = self.commentedTimes
        js['upvotedTimes'] = self.upvotedTimes
        js['viewTimes'] = self.viewTimes
        return js

MessageBlock.register(SSysTopic)

# message.gate.gatemsg.SeqSysTopic
class SeqSysTopic(ListBase):
    def __init__(self, _data=None):
        super().__init__(SSysTopic, 'SeqSysTopic')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SSysTopic()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SSysTopic()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.gate.gatemsg.SUserPost
class SUserPost:
    __slots__ = dict()
    __slots__['postId'] = str
    __slots__['userInfo'] = SUserBrief
    __slots__['title'] = str
    __slots__['content'] = str
    __slots__['images'] = SeqImageInfo
    __slots__['tags'] = message.common.publicdef.SeqString
    __slots__['createDt'] = datetime.datetime
    __slots__['sharedTimes'] = int
    __slots__['commentedTimes'] = int
    __slots__['upvotedTimes'] = int
    __slots__['viewTimes'] = int

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SUserPost.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type postId: str
    type userInfo: message.gate.gatemsg.SUserBrief
    type title: str
    type content: str
    type images: list[message.gate.gatemsg.SImageInfo]
    type tags: list[str]
    type createDt: datetime.datetime
    type sharedTimes: int
    type commentedTimes: int
    type upvotedTimes: int
    type viewTimes: int
    """
    def __init__(self):
        self.postId = str()
        self.userInfo = SUserBrief()
        self.title = str()
        self.content = str()
        self.images = SeqImageInfo()
        self.tags = message.common.publicdef.SeqString()
        self.createDt = datetime.datetime.now()
        self.sharedTimes = int()
        self.commentedTimes = int()
        self.upvotedTimes = int()
        self.viewTimes = int()

    def _read(self, _is):
        self.postId = _is.readString()
        self.userInfo._read(_is)
        self.title = _is.readString()
        self.content = _is.readString()
        self.images._read(_is)
        self.tags._read(_is)
        self.createDt = _is.readDate()
        self.sharedTimes = _is.readInt()
        self.commentedTimes = _is.readInt()
        self.upvotedTimes = _is.readInt()
        self.viewTimes = _is.readInt()

    def _write(self, _os):
        _os.writeString(self.postId)
        self.userInfo._write(_os)
        _os.writeString(self.title)
        _os.writeString(self.content)
        self.images._write(_os)
        self.tags._write(_os)
        _os.writeDate(self.createDt)
        _os.writeInt(self.sharedTimes)
        _os.writeInt(self.commentedTimes)
        _os.writeInt(self.upvotedTimes)
        _os.writeInt(self.viewTimes)

    def _fromJson(self, js):
        if 'postId' in js and isinstance(js['postId'], str):
            self.postId = js['postId']
        if 'userInfo' in js and isinstance(js['userInfo'], SUserBrief):
            self.userInfo._fromJson(js['userInfo'])
        if 'title' in js and isinstance(js['title'], str):
            self.title = js['title']
        if 'content' in js and isinstance(js['content'], str):
            self.content = js['content']
        if 'images' in js and isinstance(js['images'], SeqImageInfo):
            self.images._fromJson(js['images'])
        elif 'images' in js and isinstance(js['images'], list):
            self.images._fromJson(js['images'])
        if 'tags' in js and isinstance(js['tags'], message.common.publicdef.SeqString):
            self.tags._fromJson(js['tags'])
        elif 'tags' in js and isinstance(js['tags'], list):
            self.tags._fromJson(js['tags'])
        if 'createDt' in js and isinstance(js['createDt'], datetime.datetime):
            self.createDt = js['createDt']
        elif 'createDt' in js and isinstance(self.createDt, datetime.datetime):
            self.createDt = datetime.datetime.strptime(js['createDt'], '%Y-%m-%d %H:%M:%S')
        if 'sharedTimes' in js and isinstance(js['sharedTimes'], int):
            self.sharedTimes = js['sharedTimes']
        if 'commentedTimes' in js and isinstance(js['commentedTimes'], int):
            self.commentedTimes = js['commentedTimes']
        if 'upvotedTimes' in js and isinstance(js['upvotedTimes'], int):
            self.upvotedTimes = js['upvotedTimes']
        if 'viewTimes' in js and isinstance(js['viewTimes'], int):
            self.viewTimes = js['viewTimes']

    def _toJson(self):
        js = dict()
        js['postId'] = self.postId
        js['userInfo'] = self.userInfo._toJson()
        js['title'] = self.title
        js['content'] = self.content
        js['images'] = self.images._toJson()
        js['tags'] = self.tags._toJson()
        js['createDt'] = self.createDt
        js['sharedTimes'] = self.sharedTimes
        js['commentedTimes'] = self.commentedTimes
        js['upvotedTimes'] = self.upvotedTimes
        js['viewTimes'] = self.viewTimes
        return js

MessageBlock.register(SUserPost)

# message.gate.gatemsg.SeqUserPost
class SeqUserPost(ListBase):
    def __init__(self, _data=None):
        super().__init__(SUserPost, 'SeqUserPost')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SUserPost()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SUserPost()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.gate.gatemsg.SComment
class SComment:
    __slots__ = dict()
    __slots__['commentId'] = str
    __slots__['interActiveType'] = int
    __slots__['commenterInfo'] = SUserBrief
    __slots__['comment'] = str
    __slots__['commentDt'] = datetime.datetime
    __slots__['mentioned'] = SeqUserBriefWithoutAvatar

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SComment.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type commentId: str
    type interActiveType: int
    type commenterInfo: message.gate.gatemsg.SUserBrief
    type comment: str
    type commentDt: datetime.datetime
    type mentioned: list[message.gate.gatemsg.SUserBriefWithoutAvatar]
    """
    def __init__(self):
        self.commentId = str()
        self.interActiveType = message.common.publicdef.EInteractiveType.Upvote
        self.commenterInfo = SUserBrief()
        self.comment = str()
        self.commentDt = datetime.datetime.now()
        self.mentioned = SeqUserBriefWithoutAvatar()

    def _read(self, _is):
        self.commentId = _is.readString()
        self.interActiveType = _is.readInt()
        self.commenterInfo._read(_is)
        self.comment = _is.readString()
        self.commentDt = _is.readDate()
        self.mentioned._read(_is)

    def _write(self, _os):
        _os.writeString(self.commentId)
        _os.writeInt(self.interActiveType)
        self.commenterInfo._write(_os)
        _os.writeString(self.comment)
        _os.writeDate(self.commentDt)
        self.mentioned._write(_os)

    def _fromJson(self, js):
        if 'commentId' in js and isinstance(js['commentId'], str):
            self.commentId = js['commentId']
        if 'interActiveType' in js and isinstance(js['interActiveType'], int):
            self.interActiveType = js['interActiveType']
        if 'commenterInfo' in js and isinstance(js['commenterInfo'], SUserBrief):
            self.commenterInfo._fromJson(js['commenterInfo'])
        if 'comment' in js and isinstance(js['comment'], str):
            self.comment = js['comment']
        if 'commentDt' in js and isinstance(js['commentDt'], datetime.datetime):
            self.commentDt = js['commentDt']
        elif 'commentDt' in js and isinstance(self.commentDt, datetime.datetime):
            self.commentDt = datetime.datetime.strptime(js['commentDt'], '%Y-%m-%d %H:%M:%S')
        if 'mentioned' in js and isinstance(js['mentioned'], SeqUserBriefWithoutAvatar):
            self.mentioned._fromJson(js['mentioned'])
        elif 'mentioned' in js and isinstance(js['mentioned'], list):
            self.mentioned._fromJson(js['mentioned'])

    def _toJson(self):
        js = dict()
        js['commentId'] = self.commentId
        js['interActiveType'] = self.interActiveType
        js['commenterInfo'] = self.commenterInfo._toJson()
        js['comment'] = self.comment
        js['commentDt'] = self.commentDt
        js['mentioned'] = self.mentioned._toJson()
        return js

MessageBlock.register(SComment)

# message.gate.gatemsg.SeqComment
class SeqComment(ListBase):
    def __init__(self, _data=None):
        super().__init__(SComment, 'SeqComment')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SComment()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SComment()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.gate.gatemsg.SMsgHint
class SMsgHint:
    __slots__ = dict()
    __slots__['hintType'] = int
    __slots__['num'] = int

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SMsgHint.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type hintType: int
    type num: int
    """
    def __init__(self):
        self.hintType = message.gate.gateconst.EHintType.AllType
        self.num = int()

    def _read(self, _is):
        self.hintType = _is.readInt()
        self.num = _is.readInt()

    def _write(self, _os):
        _os.writeInt(self.hintType)
        _os.writeInt(self.num)

    def _fromJson(self, js):
        if 'hintType' in js and isinstance(js['hintType'], int):
            self.hintType = js['hintType']
        if 'num' in js and isinstance(js['num'], int):
            self.num = js['num']

    def _toJson(self):
        js = dict()
        js['hintType'] = self.hintType
        js['num'] = self.num
        return js

MessageBlock.register(SMsgHint)

# message.gate.gatemsg.SeqMsgHint
class SeqMsgHint(ListBase):
    def __init__(self, _data=None):
        super().__init__(SMsgHint, 'SeqMsgHint')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SMsgHint()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SMsgHint()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.gate.gatemsg.SUserPostCommentHint
class SUserPostCommentHint:
    __slots__ = dict()
    __slots__['hintType'] = int
    __slots__['operUserInfo'] = SUserBrief
    __slots__['content'] = str
    __slots__['postId'] = str
    __slots__['commentId'] = str
    __slots__['operDt'] = datetime.datetime

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SUserPostCommentHint.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type hintType: int
    type operUserInfo: message.gate.gatemsg.SUserBrief
    type content: str
    type postId: str
    type commentId: str
    type operDt: datetime.datetime
    """
    def __init__(self):
        self.hintType = message.gate.gateconst.EHintType.AllType
        self.operUserInfo = SUserBrief()
        self.content = str()
        self.postId = str()
        self.commentId = str()
        self.operDt = datetime.datetime.now()

    def _read(self, _is):
        self.hintType = _is.readInt()
        self.operUserInfo._read(_is)
        self.content = _is.readString()
        self.postId = _is.readString()
        self.commentId = _is.readString()
        self.operDt = _is.readDate()

    def _write(self, _os):
        _os.writeInt(self.hintType)
        self.operUserInfo._write(_os)
        _os.writeString(self.content)
        _os.writeString(self.postId)
        _os.writeString(self.commentId)
        _os.writeDate(self.operDt)

    def _fromJson(self, js):
        if 'hintType' in js and isinstance(js['hintType'], int):
            self.hintType = js['hintType']
        if 'operUserInfo' in js and isinstance(js['operUserInfo'], SUserBrief):
            self.operUserInfo._fromJson(js['operUserInfo'])
        if 'content' in js and isinstance(js['content'], str):
            self.content = js['content']
        if 'postId' in js and isinstance(js['postId'], str):
            self.postId = js['postId']
        if 'commentId' in js and isinstance(js['commentId'], str):
            self.commentId = js['commentId']
        if 'operDt' in js and isinstance(js['operDt'], datetime.datetime):
            self.operDt = js['operDt']
        elif 'operDt' in js and isinstance(self.operDt, datetime.datetime):
            self.operDt = datetime.datetime.strptime(js['operDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['hintType'] = self.hintType
        js['operUserInfo'] = self.operUserInfo._toJson()
        js['content'] = self.content
        js['postId'] = self.postId
        js['commentId'] = self.commentId
        js['operDt'] = self.operDt
        return js

MessageBlock.register(SUserPostCommentHint)

# message.gate.gatemsg.SeqUserPostCommentHint
class SeqUserPostCommentHint(ListBase):
    def __init__(self, _data=None):
        super().__init__(SUserPostCommentHint, 'SeqUserPostCommentHint')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SUserPostCommentHint()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SUserPostCommentHint()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.gate.gatemsg.SMyFan
class SMyFan:
    __slots__ = dict()
    __slots__['fanInfo'] = SUserBrief
    __slots__['operDt'] = datetime.datetime

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SMyFan.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type fanInfo: message.gate.gatemsg.SUserBrief
    type operDt: datetime.datetime
    """
    def __init__(self):
        self.fanInfo = SUserBrief()
        self.operDt = datetime.datetime.now()

    def _read(self, _is):
        self.fanInfo._read(_is)
        self.operDt = _is.readDate()

    def _write(self, _os):
        self.fanInfo._write(_os)
        _os.writeDate(self.operDt)

    def _fromJson(self, js):
        if 'fanInfo' in js and isinstance(js['fanInfo'], SUserBrief):
            self.fanInfo._fromJson(js['fanInfo'])
        if 'operDt' in js and isinstance(js['operDt'], datetime.datetime):
            self.operDt = js['operDt']
        elif 'operDt' in js and isinstance(self.operDt, datetime.datetime):
            self.operDt = datetime.datetime.strptime(js['operDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['fanInfo'] = self.fanInfo._toJson()
        js['operDt'] = self.operDt
        return js

MessageBlock.register(SMyFan)

# message.gate.gatemsg.SeqMyFan
class SeqMyFan(ListBase):
    def __init__(self, _data=None):
        super().__init__(SMyFan, 'SeqMyFan')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SMyFan()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SMyFan()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.gate.gatemsg.SMyFocus
class SMyFocus:
    __slots__ = dict()
    __slots__['userInfo'] = SUserBrief
    __slots__['operDt'] = datetime.datetime

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SMyFocus.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userInfo: message.gate.gatemsg.SUserBrief
    type operDt: datetime.datetime
    """
    def __init__(self):
        self.userInfo = SUserBrief()
        self.operDt = datetime.datetime.now()

    def _read(self, _is):
        self.userInfo._read(_is)
        self.operDt = _is.readDate()

    def _write(self, _os):
        self.userInfo._write(_os)
        _os.writeDate(self.operDt)

    def _fromJson(self, js):
        if 'userInfo' in js and isinstance(js['userInfo'], SUserBrief):
            self.userInfo._fromJson(js['userInfo'])
        if 'operDt' in js and isinstance(js['operDt'], datetime.datetime):
            self.operDt = js['operDt']
        elif 'operDt' in js and isinstance(self.operDt, datetime.datetime):
            self.operDt = datetime.datetime.strptime(js['operDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['userInfo'] = self.userInfo._toJson()
        js['operDt'] = self.operDt
        return js

MessageBlock.register(SMyFocus)

# message.gate.gatemsg.SeqMyFocus
class SeqMyFocus(ListBase):
    def __init__(self, _data=None):
        super().__init__(SMyFocus, 'SeqMyFocus')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SMyFocus()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SMyFocus()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

