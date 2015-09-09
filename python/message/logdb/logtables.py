#
# file: logtables.py
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
import message.logdb.logconst


# message.logdb.logtables.SLogUserInfo
class SLogUserInfo:
    __slots__ = dict()
    __slots__['deviceCode'] = str
    __slots__['userId'] = str
    __slots__['account'] = str
    __slots__['nickname'] = str

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SLogUserInfo.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type deviceCode: str
    type userId: str
    type account: str
    type nickname: str
    """
    def __init__(self):
        self.deviceCode = str()
        self.userId = str()
        self.account = str()
        self.nickname = str()

    def _read(self, _is):
        self.deviceCode = _is.readString()
        self.userId = _is.readString()
        self.account = _is.readString()
        self.nickname = _is.readString()

    def _write(self, _os):
        _os.writeString(self.deviceCode)
        _os.writeString(self.userId)
        _os.writeString(self.account)
        _os.writeString(self.nickname)

    def _fromJson(self, js):
        if 'deviceCode' in js and isinstance(js['deviceCode'], str):
            self.deviceCode = js['deviceCode']
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'account' in js and isinstance(js['account'], str):
            self.account = js['account']
        if 'nickname' in js and isinstance(js['nickname'], str):
            self.nickname = js['nickname']

    def _toJson(self):
        js = dict()
        js['deviceCode'] = self.deviceCode
        js['userId'] = self.userId
        js['account'] = self.account
        js['nickname'] = self.nickname
        return js

MessageBlock.register(SLogUserInfo)

# message.logdb.logtables.TLogLogin
class TLogLogin:
    __slots__ = dict()
    __slots__['userInfo'] = SLogUserInfo
    __slots__['operDt'] = datetime.datetime

    # field names
    fn_userInfo = 'userInfo'
    fn_operDt = 'operDt'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TLogLogin.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userInfo: message.logdb.logtables.SLogUserInfo
    type operDt: datetime.datetime
    """
    def __init__(self):
        self.userInfo = SLogUserInfo()
        self.operDt = datetime.datetime.now()

    def _read(self, _is):
        self.userInfo._read(_is)
        self.operDt = _is.readDate()

    def _write(self, _os):
        self.userInfo._write(_os)
        _os.writeDate(self.operDt)

    def _fromJson(self, js):
        if 'userInfo' in js and isinstance(js['userInfo'], SLogUserInfo):
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

MessageBlock.register(TLogLogin)

# message.logdb.logtables.SeqTLogLogin
class SeqTLogLogin(ListBase):
    def __init__(self, _data=None):
        super().__init__(TLogLogin, 'SeqTLogLogin')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TLogLogin()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TLogLogin()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.logdb.logtables.TLogSignup
class TLogSignup:
    __slots__ = dict()
    __slots__['userInfo'] = SLogUserInfo
    __slots__['operDt'] = datetime.datetime

    # field names
    fn_userInfo = 'userInfo'
    fn_operDt = 'operDt'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TLogSignup.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userInfo: message.logdb.logtables.SLogUserInfo
    type operDt: datetime.datetime
    """
    def __init__(self):
        self.userInfo = SLogUserInfo()
        self.operDt = datetime.datetime.now()

    def _read(self, _is):
        self.userInfo._read(_is)
        self.operDt = _is.readDate()

    def _write(self, _os):
        self.userInfo._write(_os)
        _os.writeDate(self.operDt)

    def _fromJson(self, js):
        if 'userInfo' in js and isinstance(js['userInfo'], SLogUserInfo):
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

MessageBlock.register(TLogSignup)

# message.logdb.logtables.SeqTLogSignup
class SeqTLogSignup(ListBase):
    def __init__(self, _data=None):
        super().__init__(TLogSignup, 'SeqTLogSignup')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TLogSignup()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TLogSignup()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.logdb.logtables.TLogRefreshSysTopic
class TLogRefreshSysTopic:
    __slots__ = dict()
    __slots__['userInfo'] = SLogUserInfo
    __slots__['tags'] = message.common.publicdef.SeqString
    __slots__['operDt'] = datetime.datetime

    # field names
    fn_userInfo = 'userInfo'
    fn_tags = 'tags'
    fn_operDt = 'operDt'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TLogRefreshSysTopic.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userInfo: message.logdb.logtables.SLogUserInfo
    type tags: list[str]
    type operDt: datetime.datetime
    """
    def __init__(self):
        self.userInfo = SLogUserInfo()
        self.tags = message.common.publicdef.SeqString()
        self.operDt = datetime.datetime.now()

    def _read(self, _is):
        self.userInfo._read(_is)
        self.tags._read(_is)
        self.operDt = _is.readDate()

    def _write(self, _os):
        self.userInfo._write(_os)
        self.tags._write(_os)
        _os.writeDate(self.operDt)

    def _fromJson(self, js):
        if 'userInfo' in js and isinstance(js['userInfo'], SLogUserInfo):
            self.userInfo._fromJson(js['userInfo'])
        if 'tags' in js and isinstance(js['tags'], message.common.publicdef.SeqString):
            self.tags._fromJson(js['tags'])
        elif 'tags' in js and isinstance(js['tags'], list):
            self.tags._fromJson(js['tags'])
        if 'operDt' in js and isinstance(js['operDt'], datetime.datetime):
            self.operDt = js['operDt']
        elif 'operDt' in js and isinstance(self.operDt, datetime.datetime):
            self.operDt = datetime.datetime.strptime(js['operDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['userInfo'] = self.userInfo._toJson()
        js['tags'] = self.tags._toJson()
        js['operDt'] = self.operDt
        return js

MessageBlock.register(TLogRefreshSysTopic)

# message.logdb.logtables.SeqTLogRefreshSysTopic
class SeqTLogRefreshSysTopic(ListBase):
    def __init__(self, _data=None):
        super().__init__(TLogRefreshSysTopic, 'SeqTLogRefreshSysTopic')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TLogRefreshSysTopic()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TLogRefreshSysTopic()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.logdb.logtables.TLogSysTopicOper
class TLogSysTopicOper:
    __slots__ = dict()
    __slots__['userInfo'] = SLogUserInfo
    __slots__['topicId'] = str
    __slots__['operType'] = int
    __slots__['operDt'] = datetime.datetime

    # field names
    fn_userInfo = 'userInfo'
    fn_topicId = 'topicId'
    fn_operType = 'operType'
    fn_operDt = 'operDt'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TLogSysTopicOper.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userInfo: message.logdb.logtables.SLogUserInfo
    type topicId: str
    type operType: int
    type operDt: datetime.datetime
    """
    def __init__(self):
        self.userInfo = SLogUserInfo()
        self.topicId = str()
        self.operType = message.logdb.logconst.ELogPostOperType.View
        self.operDt = datetime.datetime.now()

    def _read(self, _is):
        self.userInfo._read(_is)
        self.topicId = _is.readString()
        self.operType = _is.readInt()
        self.operDt = _is.readDate()

    def _write(self, _os):
        self.userInfo._write(_os)
        _os.writeString(self.topicId)
        _os.writeInt(self.operType)
        _os.writeDate(self.operDt)

    def _fromJson(self, js):
        if 'userInfo' in js and isinstance(js['userInfo'], SLogUserInfo):
            self.userInfo._fromJson(js['userInfo'])
        if 'topicId' in js and isinstance(js['topicId'], str):
            self.topicId = js['topicId']
        if 'operType' in js and isinstance(js['operType'], int):
            self.operType = js['operType']
        if 'operDt' in js and isinstance(js['operDt'], datetime.datetime):
            self.operDt = js['operDt']
        elif 'operDt' in js and isinstance(self.operDt, datetime.datetime):
            self.operDt = datetime.datetime.strptime(js['operDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['userInfo'] = self.userInfo._toJson()
        js['topicId'] = self.topicId
        js['operType'] = self.operType
        js['operDt'] = self.operDt
        return js

MessageBlock.register(TLogSysTopicOper)

# message.logdb.logtables.SeqTLogSysTopicOper
class SeqTLogSysTopicOper(ListBase):
    def __init__(self, _data=None):
        super().__init__(TLogSysTopicOper, 'SeqTLogSysTopicOper')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TLogSysTopicOper()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TLogSysTopicOper()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.logdb.logtables.TLogRefreshUserPost
class TLogRefreshUserPost:
    __slots__ = dict()
    __slots__['userInfo'] = SLogUserInfo
    __slots__['tags'] = message.common.publicdef.SeqString
    __slots__['operDt'] = datetime.datetime

    # field names
    fn_userInfo = 'userInfo'
    fn_tags = 'tags'
    fn_operDt = 'operDt'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TLogRefreshUserPost.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userInfo: message.logdb.logtables.SLogUserInfo
    type tags: list[str]
    type operDt: datetime.datetime
    """
    def __init__(self):
        self.userInfo = SLogUserInfo()
        self.tags = message.common.publicdef.SeqString()
        self.operDt = datetime.datetime.now()

    def _read(self, _is):
        self.userInfo._read(_is)
        self.tags._read(_is)
        self.operDt = _is.readDate()

    def _write(self, _os):
        self.userInfo._write(_os)
        self.tags._write(_os)
        _os.writeDate(self.operDt)

    def _fromJson(self, js):
        if 'userInfo' in js and isinstance(js['userInfo'], SLogUserInfo):
            self.userInfo._fromJson(js['userInfo'])
        if 'tags' in js and isinstance(js['tags'], message.common.publicdef.SeqString):
            self.tags._fromJson(js['tags'])
        elif 'tags' in js and isinstance(js['tags'], list):
            self.tags._fromJson(js['tags'])
        if 'operDt' in js and isinstance(js['operDt'], datetime.datetime):
            self.operDt = js['operDt']
        elif 'operDt' in js and isinstance(self.operDt, datetime.datetime):
            self.operDt = datetime.datetime.strptime(js['operDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['userInfo'] = self.userInfo._toJson()
        js['tags'] = self.tags._toJson()
        js['operDt'] = self.operDt
        return js

MessageBlock.register(TLogRefreshUserPost)

# message.logdb.logtables.SeqTLogRefreshUserPost
class SeqTLogRefreshUserPost(ListBase):
    def __init__(self, _data=None):
        super().__init__(TLogRefreshUserPost, 'SeqTLogRefreshUserPost')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TLogRefreshUserPost()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TLogRefreshUserPost()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.logdb.logtables.TLogUserPostOper
class TLogUserPostOper:
    __slots__ = dict()
    __slots__['userInfo'] = SLogUserInfo
    __slots__['postId'] = str
    __slots__['operType'] = int
    __slots__['operDt'] = datetime.datetime

    # field names
    fn_userInfo = 'userInfo'
    fn_postId = 'postId'
    fn_operType = 'operType'
    fn_operDt = 'operDt'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TLogUserPostOper.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type userInfo: message.logdb.logtables.SLogUserInfo
    type postId: str
    type operType: int
    type operDt: datetime.datetime
    """
    def __init__(self):
        self.userInfo = SLogUserInfo()
        self.postId = str()
        self.operType = message.logdb.logconst.ELogPostOperType.View
        self.operDt = datetime.datetime.now()

    def _read(self, _is):
        self.userInfo._read(_is)
        self.postId = _is.readString()
        self.operType = _is.readInt()
        self.operDt = _is.readDate()

    def _write(self, _os):
        self.userInfo._write(_os)
        _os.writeString(self.postId)
        _os.writeInt(self.operType)
        _os.writeDate(self.operDt)

    def _fromJson(self, js):
        if 'userInfo' in js and isinstance(js['userInfo'], SLogUserInfo):
            self.userInfo._fromJson(js['userInfo'])
        if 'postId' in js and isinstance(js['postId'], str):
            self.postId = js['postId']
        if 'operType' in js and isinstance(js['operType'], int):
            self.operType = js['operType']
        if 'operDt' in js and isinstance(js['operDt'], datetime.datetime):
            self.operDt = js['operDt']
        elif 'operDt' in js and isinstance(self.operDt, datetime.datetime):
            self.operDt = datetime.datetime.strptime(js['operDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['userInfo'] = self.userInfo._toJson()
        js['postId'] = self.postId
        js['operType'] = self.operType
        js['operDt'] = self.operDt
        return js

MessageBlock.register(TLogUserPostOper)

# message.logdb.logtables.SeqTLogUserPostOper
class SeqTLogUserPostOper(ListBase):
    def __init__(self, _data=None):
        super().__init__(TLogUserPostOper, 'SeqTLogUserPostOper')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TLogUserPostOper()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TLogUserPostOper()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

