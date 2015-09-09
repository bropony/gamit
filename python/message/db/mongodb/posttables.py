#
# file: posttables.py
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


# message.db.mongodb.posttables.TSysTopic
class TSysTopic:
    __slots__ = dict()
    __slots__['topicId'] = str
    __slots__['topicType'] = int
    __slots__['publisherId'] = str
    __slots__['title'] = str
    __slots__['content'] = str
    __slots__['createDt'] = datetime.datetime
    __slots__['imageKeys'] = message.common.publicdef.SeqString
    __slots__['tags'] = message.common.publicdef.SeqString
    __slots__['sharedTimes'] = int
    __slots__['commentedTimes'] = int
    __slots__['upvotedTimes'] = int
    __slots__['viewTimes'] = int

    # field names
    fn_topicId = 'topicId'
    fn_topicType = 'topicType'
    fn_publisherId = 'publisherId'
    fn_title = 'title'
    fn_content = 'content'
    fn_createDt = 'createDt'
    fn_imageKeys = 'imageKeys'
    fn_tags = 'tags'
    fn_sharedTimes = 'sharedTimes'
    fn_commentedTimes = 'commentedTimes'
    fn_upvotedTimes = 'upvotedTimes'
    fn_viewTimes = 'viewTimes'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TSysTopic.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type topicId: str
    type topicType: int
    type publisherId: str
    type title: str
    type content: str
    type createDt: datetime.datetime
    type imageKeys: list[str]
    type tags: list[str]
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
        self.createDt = datetime.datetime.now()
        self.imageKeys = message.common.publicdef.SeqString()
        self.tags = message.common.publicdef.SeqString()
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
        self.createDt = _is.readDate()
        self.imageKeys._read(_is)
        self.tags._read(_is)
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
        _os.writeDate(self.createDt)
        self.imageKeys._write(_os)
        self.tags._write(_os)
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
        if 'createDt' in js and isinstance(js['createDt'], datetime.datetime):
            self.createDt = js['createDt']
        elif 'createDt' in js and isinstance(self.createDt, datetime.datetime):
            self.createDt = datetime.datetime.strptime(js['createDt'], '%Y-%m-%d %H:%M:%S')
        if 'imageKeys' in js and isinstance(js['imageKeys'], message.common.publicdef.SeqString):
            self.imageKeys._fromJson(js['imageKeys'])
        elif 'imageKeys' in js and isinstance(js['imageKeys'], list):
            self.imageKeys._fromJson(js['imageKeys'])
        if 'tags' in js and isinstance(js['tags'], message.common.publicdef.SeqString):
            self.tags._fromJson(js['tags'])
        elif 'tags' in js and isinstance(js['tags'], list):
            self.tags._fromJson(js['tags'])
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
        js['createDt'] = self.createDt
        js['imageKeys'] = self.imageKeys._toJson()
        js['tags'] = self.tags._toJson()
        js['sharedTimes'] = self.sharedTimes
        js['commentedTimes'] = self.commentedTimes
        js['upvotedTimes'] = self.upvotedTimes
        js['viewTimes'] = self.viewTimes
        return js

MessageBlock.register(TSysTopic)

# message.db.mongodb.posttables.SeqTSysTopic
class SeqTSysTopic(ListBase):
    def __init__(self, _data=None):
        super().__init__(TSysTopic, 'SeqTSysTopic')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TSysTopic()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TSysTopic()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.db.mongodb.posttables.TSysTopicComment
class TSysTopicComment:
    __slots__ = dict()
    __slots__['commentId'] = str
    __slots__['interActiveType'] = int
    __slots__['userId'] = str
    __slots__['topicId'] = str
    __slots__['content'] = str
    __slots__['mentionedUsers'] = message.common.publicdef.SeqString
    __slots__['createDt'] = datetime.datetime

    # field names
    fn_commentId = 'commentId'
    fn_interActiveType = 'interActiveType'
    fn_userId = 'userId'
    fn_topicId = 'topicId'
    fn_content = 'content'
    fn_mentionedUsers = 'mentionedUsers'
    fn_createDt = 'createDt'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TSysTopicComment.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type commentId: str
    type interActiveType: int
    type userId: str
    type topicId: str
    type content: str
    type mentionedUsers: list[str]
    type createDt: datetime.datetime
    """
    def __init__(self):
        self.commentId = str()
        self.interActiveType = message.common.publicdef.EInteractiveType.Upvote
        self.userId = str()
        self.topicId = str()
        self.content = str()
        self.mentionedUsers = message.common.publicdef.SeqString()
        self.createDt = datetime.datetime.now()

    def _read(self, _is):
        self.commentId = _is.readString()
        self.interActiveType = _is.readInt()
        self.userId = _is.readString()
        self.topicId = _is.readString()
        self.content = _is.readString()
        self.mentionedUsers._read(_is)
        self.createDt = _is.readDate()

    def _write(self, _os):
        _os.writeString(self.commentId)
        _os.writeInt(self.interActiveType)
        _os.writeString(self.userId)
        _os.writeString(self.topicId)
        _os.writeString(self.content)
        self.mentionedUsers._write(_os)
        _os.writeDate(self.createDt)

    def _fromJson(self, js):
        if 'commentId' in js and isinstance(js['commentId'], str):
            self.commentId = js['commentId']
        if 'interActiveType' in js and isinstance(js['interActiveType'], int):
            self.interActiveType = js['interActiveType']
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'topicId' in js and isinstance(js['topicId'], str):
            self.topicId = js['topicId']
        if 'content' in js and isinstance(js['content'], str):
            self.content = js['content']
        if 'mentionedUsers' in js and isinstance(js['mentionedUsers'], message.common.publicdef.SeqString):
            self.mentionedUsers._fromJson(js['mentionedUsers'])
        elif 'mentionedUsers' in js and isinstance(js['mentionedUsers'], list):
            self.mentionedUsers._fromJson(js['mentionedUsers'])
        if 'createDt' in js and isinstance(js['createDt'], datetime.datetime):
            self.createDt = js['createDt']
        elif 'createDt' in js and isinstance(self.createDt, datetime.datetime):
            self.createDt = datetime.datetime.strptime(js['createDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['commentId'] = self.commentId
        js['interActiveType'] = self.interActiveType
        js['userId'] = self.userId
        js['topicId'] = self.topicId
        js['content'] = self.content
        js['mentionedUsers'] = self.mentionedUsers._toJson()
        js['createDt'] = self.createDt
        return js

MessageBlock.register(TSysTopicComment)

# message.db.mongodb.posttables.SeqTSysTopicComment
class SeqTSysTopicComment(ListBase):
    def __init__(self, _data=None):
        super().__init__(TSysTopicComment, 'SeqTSysTopicComment')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TSysTopicComment()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TSysTopicComment()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.db.mongodb.posttables.TUserPost
class TUserPost:
    __slots__ = dict()
    __slots__['postId'] = str
    __slots__['userId'] = str
    __slots__['imgageUploadedNum'] = int
    __slots__['title'] = str
    __slots__['content'] = str
    __slots__['imageKeys'] = message.common.publicdef.SeqString
    __slots__['tags'] = message.common.publicdef.SeqString
    __slots__['createDt'] = datetime.datetime
    __slots__['sharedTimes'] = int
    __slots__['commentedTimes'] = int
    __slots__['upvotedTimes'] = int
    __slots__['viewTimes'] = int

    # field names
    fn_postId = 'postId'
    fn_userId = 'userId'
    fn_imgageUploadedNum = 'imgageUploadedNum'
    fn_title = 'title'
    fn_content = 'content'
    fn_imageKeys = 'imageKeys'
    fn_tags = 'tags'
    fn_createDt = 'createDt'
    fn_sharedTimes = 'sharedTimes'
    fn_commentedTimes = 'commentedTimes'
    fn_upvotedTimes = 'upvotedTimes'
    fn_viewTimes = 'viewTimes'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TUserPost.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type postId: str
    type userId: str
    type imgageUploadedNum: int
    type title: str
    type content: str
    type imageKeys: list[str]
    type tags: list[str]
    type createDt: datetime.datetime
    type sharedTimes: int
    type commentedTimes: int
    type upvotedTimes: int
    type viewTimes: int
    """
    def __init__(self):
        self.postId = str()
        self.userId = str()
        self.imgageUploadedNum = int()
        self.title = str()
        self.content = str()
        self.imageKeys = message.common.publicdef.SeqString()
        self.tags = message.common.publicdef.SeqString()
        self.createDt = datetime.datetime.now()
        self.sharedTimes = int()
        self.commentedTimes = int()
        self.upvotedTimes = int()
        self.viewTimes = int()

    def _read(self, _is):
        self.postId = _is.readString()
        self.userId = _is.readString()
        self.imgageUploadedNum = _is.readInt()
        self.title = _is.readString()
        self.content = _is.readString()
        self.imageKeys._read(_is)
        self.tags._read(_is)
        self.createDt = _is.readDate()
        self.sharedTimes = _is.readInt()
        self.commentedTimes = _is.readInt()
        self.upvotedTimes = _is.readInt()
        self.viewTimes = _is.readInt()

    def _write(self, _os):
        _os.writeString(self.postId)
        _os.writeString(self.userId)
        _os.writeInt(self.imgageUploadedNum)
        _os.writeString(self.title)
        _os.writeString(self.content)
        self.imageKeys._write(_os)
        self.tags._write(_os)
        _os.writeDate(self.createDt)
        _os.writeInt(self.sharedTimes)
        _os.writeInt(self.commentedTimes)
        _os.writeInt(self.upvotedTimes)
        _os.writeInt(self.viewTimes)

    def _fromJson(self, js):
        if 'postId' in js and isinstance(js['postId'], str):
            self.postId = js['postId']
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'imgageUploadedNum' in js and isinstance(js['imgageUploadedNum'], int):
            self.imgageUploadedNum = js['imgageUploadedNum']
        if 'title' in js and isinstance(js['title'], str):
            self.title = js['title']
        if 'content' in js and isinstance(js['content'], str):
            self.content = js['content']
        if 'imageKeys' in js and isinstance(js['imageKeys'], message.common.publicdef.SeqString):
            self.imageKeys._fromJson(js['imageKeys'])
        elif 'imageKeys' in js and isinstance(js['imageKeys'], list):
            self.imageKeys._fromJson(js['imageKeys'])
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
        js['userId'] = self.userId
        js['imgageUploadedNum'] = self.imgageUploadedNum
        js['title'] = self.title
        js['content'] = self.content
        js['imageKeys'] = self.imageKeys._toJson()
        js['tags'] = self.tags._toJson()
        js['createDt'] = self.createDt
        js['sharedTimes'] = self.sharedTimes
        js['commentedTimes'] = self.commentedTimes
        js['upvotedTimes'] = self.upvotedTimes
        js['viewTimes'] = self.viewTimes
        return js

MessageBlock.register(TUserPost)

# message.db.mongodb.posttables.SeqTUserPost
class SeqTUserPost(ListBase):
    def __init__(self, _data=None):
        super().__init__(TUserPost, 'SeqTUserPost')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TUserPost()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TUserPost()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.db.mongodb.posttables.TUserPostComment
class TUserPostComment:
    __slots__ = dict()
    __slots__['commentId'] = str
    __slots__['interActiveType'] = int
    __slots__['userId'] = str
    __slots__['postId'] = str
    __slots__['content'] = str
    __slots__['mentionedUsers'] = message.common.publicdef.SeqString
    __slots__['createDt'] = datetime.datetime

    # field names
    fn_commentId = 'commentId'
    fn_interActiveType = 'interActiveType'
    fn_userId = 'userId'
    fn_postId = 'postId'
    fn_content = 'content'
    fn_mentionedUsers = 'mentionedUsers'
    fn_createDt = 'createDt'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TUserPostComment.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type commentId: str
    type interActiveType: int
    type userId: str
    type postId: str
    type content: str
    type mentionedUsers: list[str]
    type createDt: datetime.datetime
    """
    def __init__(self):
        self.commentId = str()
        self.interActiveType = message.common.publicdef.EInteractiveType.Upvote
        self.userId = str()
        self.postId = str()
        self.content = str()
        self.mentionedUsers = message.common.publicdef.SeqString()
        self.createDt = datetime.datetime.now()

    def _read(self, _is):
        self.commentId = _is.readString()
        self.interActiveType = _is.readInt()
        self.userId = _is.readString()
        self.postId = _is.readString()
        self.content = _is.readString()
        self.mentionedUsers._read(_is)
        self.createDt = _is.readDate()

    def _write(self, _os):
        _os.writeString(self.commentId)
        _os.writeInt(self.interActiveType)
        _os.writeString(self.userId)
        _os.writeString(self.postId)
        _os.writeString(self.content)
        self.mentionedUsers._write(_os)
        _os.writeDate(self.createDt)

    def _fromJson(self, js):
        if 'commentId' in js and isinstance(js['commentId'], str):
            self.commentId = js['commentId']
        if 'interActiveType' in js and isinstance(js['interActiveType'], int):
            self.interActiveType = js['interActiveType']
        if 'userId' in js and isinstance(js['userId'], str):
            self.userId = js['userId']
        if 'postId' in js and isinstance(js['postId'], str):
            self.postId = js['postId']
        if 'content' in js and isinstance(js['content'], str):
            self.content = js['content']
        if 'mentionedUsers' in js and isinstance(js['mentionedUsers'], message.common.publicdef.SeqString):
            self.mentionedUsers._fromJson(js['mentionedUsers'])
        elif 'mentionedUsers' in js and isinstance(js['mentionedUsers'], list):
            self.mentionedUsers._fromJson(js['mentionedUsers'])
        if 'createDt' in js and isinstance(js['createDt'], datetime.datetime):
            self.createDt = js['createDt']
        elif 'createDt' in js and isinstance(self.createDt, datetime.datetime):
            self.createDt = datetime.datetime.strptime(js['createDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['commentId'] = self.commentId
        js['interActiveType'] = self.interActiveType
        js['userId'] = self.userId
        js['postId'] = self.postId
        js['content'] = self.content
        js['mentionedUsers'] = self.mentionedUsers._toJson()
        js['createDt'] = self.createDt
        return js

MessageBlock.register(TUserPostComment)

# message.db.mongodb.posttables.SeqTUserPostComment
class SeqTUserPostComment(ListBase):
    def __init__(self, _data=None):
        super().__init__(TUserPostComment, 'SeqTUserPostComment')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TUserPostComment()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TUserPostComment()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

