#
# file: itablesaver.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *
from gamit.rmi.rmicore import *
from gamit.serialize.serializer import Serializer
from gamit.serialize.datatype import RmiDataType
import abc
import message.common.publicdef
import message.common.publicmsg
import message.db.mongodb.usertables
import message.db.mongodb.posttables
import message.db.systemcommand
import message.db.mongodb.utiltables


class ITableSaver_Updatetuseraddress_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Updatetuserbasic_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Updatetusersettings_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Updatetuserproperty_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Updatetfamilymember_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Updatetfamilymemberbatch_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Removefamilymembers_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Updatetsystopic_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Loadsystopics_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, topicList):
        if not isinstance(topicList, message.db.mongodb.posttables.SeqTSysTopic):
            raise Exception("topicList must be instance of message.db.mongodb.posttables.SeqTSysTopic", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        topicList._write(_os)

        self.sendout()

class ITableSaver_Updatetsystopiccomment_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Loadsystopiccomments_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, comments):
        if not isinstance(comments, message.db.mongodb.posttables.SeqTSysTopicComment):
            raise Exception("comments must be instance of message.db.mongodb.posttables.SeqTSysTopicComment", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        comments._write(_os)

        self.sendout()

class ITableSaver_Querysystopicupvotestatus_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, sysTopicStatusDict):
        if not isinstance(sysTopicStatusDict, message.common.publicdef.DictStringBool):
            raise Exception("sysTopicStatusDict must be instance of message.common.publicdef.DictStringBool", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        sysTopicStatusDict._write(_os)

        self.sendout()

class ITableSaver_Removesystopicupvote_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, commentId):
        if not isinstance(commentId, str):
            raise Exception("commentId must be instance of string", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeString(commentId)

        self.sendout()

class ITableSaver_Updatetuserpost_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Updatetuserpostbatch_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Loaduserposts_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, postList):
        if not isinstance(postList, message.db.mongodb.posttables.SeqTUserPost):
            raise Exception("postList must be instance of message.db.mongodb.posttables.SeqTUserPost", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        postList._write(_os)

        self.sendout()

class ITableSaver_Updatetuserpostcomment_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Loaduserpostcomments_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, comments):
        if not isinstance(comments, message.db.mongodb.posttables.SeqTUserPostComment):
            raise Exception("comments must be instance of message.db.mongodb.posttables.SeqTUserPostComment", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        comments._write(_os)

        self.sendout()

class ITableSaver_Queryuserpostupvotestatus_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, updvoteStatusDict):
        if not isinstance(updvoteStatusDict, message.common.publicdef.DictStringBool):
            raise Exception("updvoteStatusDict must be instance of message.common.publicdef.DictStringBool", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        updvoteStatusDict._write(_os)

        self.sendout()

class ITableSaver_Removeuserpostupvote_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, commentId):
        if not isinstance(commentId, str):
            raise Exception("commentId must be instance of string", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeString(commentId)

        self.sendout()

class ITableSaver_Saveuserimages_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Userimagesdidupload_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Updatefaninfo_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Getfansbyuseridandpageindex_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, fanList):
        if not isinstance(fanList, message.db.mongodb.usertables.SeqTUserFan):
            raise Exception("fanList must be instance of message.db.mongodb.usertables.SeqTUserFan", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        fanList._write(_os)

        self.sendout()

class ITableSaver_Getfocususeidlist_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, fanList):
        if not isinstance(fanList, message.db.mongodb.usertables.SeqTUserFan):
            raise Exception("fanList must be instance of message.db.mongodb.usertables.SeqTUserFan", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        fanList._write(_os)

        self.sendout()

class ITableSaver_Hasfollowed_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, hasFollowed):
        if not isinstance(hasFollowed, bool):
            raise Exception("hasFollowed must be instance of bool", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeBool(hasFollowed)

        self.sendout()

class ITableSaver_Unfollow_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ITableSaver_Updatetuseraddress_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Updatetuserbasic_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Updatetusersettings_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Updatetuserproperty_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Updatetfamilymember_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Updatetfamilymemberbatch_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Removefamilymembers_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Updatetsystopic_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Loadsystopics_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        topicList = message.db.mongodb.posttables.SeqTSysTopic()
        topicList._read(_is)

        self.onResponse(topicList)

    @abc.abstractmethod
    def onResponse(self, topicList):
        """
        :type topicList: list[message.db.mongodb.posttables.TSysTopic]
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Updatetsystopiccomment_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Loadsystopiccomments_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        comments = message.db.mongodb.posttables.SeqTSysTopicComment()
        comments._read(_is)

        self.onResponse(comments)

    @abc.abstractmethod
    def onResponse(self, comments):
        """
        :type comments: list[message.db.mongodb.posttables.TSysTopicComment]
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Querysystopicupvotestatus_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        sysTopicStatusDict = message.common.publicdef.DictStringBool()
        sysTopicStatusDict._read(_is)

        self.onResponse(sysTopicStatusDict)

    @abc.abstractmethod
    def onResponse(self, sysTopicStatusDict):
        """
        :type sysTopicStatusDict: dict[str, bool]
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Removesystopicupvote_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        commentId = str()
        commentId = _is.readString()

        self.onResponse(commentId)

    @abc.abstractmethod
    def onResponse(self, commentId):
        """
        :type commentId: str
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Updatetuserpost_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Updatetuserpostbatch_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Loaduserposts_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        postList = message.db.mongodb.posttables.SeqTUserPost()
        postList._read(_is)

        self.onResponse(postList)

    @abc.abstractmethod
    def onResponse(self, postList):
        """
        :type postList: list[message.db.mongodb.posttables.TUserPost]
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Updatetuserpostcomment_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Loaduserpostcomments_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        comments = message.db.mongodb.posttables.SeqTUserPostComment()
        comments._read(_is)

        self.onResponse(comments)

    @abc.abstractmethod
    def onResponse(self, comments):
        """
        :type comments: list[message.db.mongodb.posttables.TUserPostComment]
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Queryuserpostupvotestatus_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        updvoteStatusDict = message.common.publicdef.DictStringBool()
        updvoteStatusDict._read(_is)

        self.onResponse(updvoteStatusDict)

    @abc.abstractmethod
    def onResponse(self, updvoteStatusDict):
        """
        :type updvoteStatusDict: dict[str, bool]
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Removeuserpostupvote_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        commentId = str()
        commentId = _is.readString()

        self.onResponse(commentId)

    @abc.abstractmethod
    def onResponse(self, commentId):
        """
        :type commentId: str
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Saveuserimages_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Userimagesdidupload_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Updatefaninfo_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Getfansbyuseridandpageindex_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        fanList = message.db.mongodb.usertables.SeqTUserFan()
        fanList._read(_is)

        self.onResponse(fanList)

    @abc.abstractmethod
    def onResponse(self, fanList):
        """
        :type fanList: list[message.db.mongodb.usertables.TUserFan]
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Getfocususeidlist_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        fanList = message.db.mongodb.usertables.SeqTUserFan()
        fanList._read(_is)

        self.onResponse(fanList)

    @abc.abstractmethod
    def onResponse(self, fanList):
        """
        :type fanList: list[message.db.mongodb.usertables.TUserFan]
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Hasfollowed_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        hasFollowed = bool()
        hasFollowed = _is.readBool()

        self.onResponse(hasFollowed)

    @abc.abstractmethod
    def onResponse(self, hasFollowed):
        """
        :type hasFollowed: bool
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaver_Unfollow_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITableSaverServant(RmiServant):
    def __init__(self, name='ITableSaver'):
        super().__init__(name)
        self.methodMap['updateTUserAddress'] = self._updateTUserAddress
        self.methodMap['updateTUserBasic'] = self._updateTUserBasic
        self.methodMap['updateTUserSettings'] = self._updateTUserSettings
        self.methodMap['updateTUserProperty'] = self._updateTUserProperty
        self.methodMap['updateTFamilyMember'] = self._updateTFamilyMember
        self.methodMap['updateTFamilyMemberBatch'] = self._updateTFamilyMemberBatch
        self.methodMap['removeFamilyMembers'] = self._removeFamilyMembers
        self.methodMap['updateTSysTopic'] = self._updateTSysTopic
        self.methodMap['loadSysTopics'] = self._loadSysTopics
        self.methodMap['updateTSysTopicComment'] = self._updateTSysTopicComment
        self.methodMap['loadSysTopicComments'] = self._loadSysTopicComments
        self.methodMap['querySysTopicUpvoteStatus'] = self._querySysTopicUpvoteStatus
        self.methodMap['removeSysTopicUpvote'] = self._removeSysTopicUpvote
        self.methodMap['updateTUserPost'] = self._updateTUserPost
        self.methodMap['updateTUserPostBatch'] = self._updateTUserPostBatch
        self.methodMap['loadUserPosts'] = self._loadUserPosts
        self.methodMap['updateTUserPostComment'] = self._updateTUserPostComment
        self.methodMap['loadUserPostComments'] = self._loadUserPostComments
        self.methodMap['queryUserPostUpvoteStatus'] = self._queryUserPostUpvoteStatus
        self.methodMap['removeUserPostUpvote'] = self._removeUserPostUpvote
        self.methodMap['saveUserImages'] = self._saveUserImages
        self.methodMap['userImagesDidUpload'] = self._userImagesDidUpload
        self.methodMap['updateFanInfo'] = self._updateFanInfo
        self.methodMap['getFansByUserIdAndPageIndex'] = self._getFansByUserIdAndPageIndex
        self.methodMap['getFocusUseIdList'] = self._getFocusUseIdList
        self.methodMap['hasFollowed'] = self._hasFollowed
        self.methodMap['unfollow'] = self._unfollow

    def _updateTUserAddress(self, _connId, _msgId, _is):
        userAddresss = message.db.mongodb.usertables.TUserAddress()
        userAddresss._read(_is)
        _request = ITableSaver_Updatetuseraddress_Request(_connId, _msgId, self)
        self.updateTUserAddress(userAddresss, _request)

    def _updateTUserBasic(self, _connId, _msgId, _is):
        userBasic = message.db.mongodb.usertables.TUserBasic()
        userBasic._read(_is)
        _request = ITableSaver_Updatetuserbasic_Request(_connId, _msgId, self)
        self.updateTUserBasic(userBasic, _request)

    def _updateTUserSettings(self, _connId, _msgId, _is):
        userSettings = message.db.mongodb.usertables.TUserSettings()
        userSettings._read(_is)
        _request = ITableSaver_Updatetusersettings_Request(_connId, _msgId, self)
        self.updateTUserSettings(userSettings, _request)

    def _updateTUserProperty(self, _connId, _msgId, _is):
        userProperty = message.db.mongodb.usertables.TUserProperty()
        userProperty._read(_is)
        _request = ITableSaver_Updatetuserproperty_Request(_connId, _msgId, self)
        self.updateTUserProperty(userProperty, _request)

    def _updateTFamilyMember(self, _connId, _msgId, _is):
        familyMember = message.db.mongodb.usertables.TFamilyMember()
        familyMember._read(_is)
        _request = ITableSaver_Updatetfamilymember_Request(_connId, _msgId, self)
        self.updateTFamilyMember(familyMember, _request)

    def _updateTFamilyMemberBatch(self, _connId, _msgId, _is):
        familyMembers = message.db.mongodb.usertables.SeqTFamilyMember()
        familyMembers._read(_is)
        _request = ITableSaver_Updatetfamilymemberbatch_Request(_connId, _msgId, self)
        self.updateTFamilyMemberBatch(familyMembers, _request)

    def _removeFamilyMembers(self, _connId, _msgId, _is):
        userId = str()
        userId = _is.readString()
        indexes = message.common.publicdef.SeqInt()
        indexes._read(_is)
        _request = ITableSaver_Removefamilymembers_Request(_connId, _msgId, self)
        self.removeFamilyMembers(userId, indexes, _request)

    def _updateTSysTopic(self, _connId, _msgId, _is):
        sysTopic = message.db.mongodb.posttables.TSysTopic()
        sysTopic._read(_is)
        _request = ITableSaver_Updatetsystopic_Request(_connId, _msgId, self)
        self.updateTSysTopic(sysTopic, _request)

    def _loadSysTopics(self, _connId, _msgId, _is):
        pageIndex = int()
        pageIndex = _is.readInt()
        numPerPage = int()
        numPerPage = _is.readInt()
        _request = ITableSaver_Loadsystopics_Request(_connId, _msgId, self)
        self.loadSysTopics(pageIndex, numPerPage, _request)

    def _updateTSysTopicComment(self, _connId, _msgId, _is):
        comments = message.db.mongodb.posttables.TSysTopicComment()
        comments._read(_is)
        _request = ITableSaver_Updatetsystopiccomment_Request(_connId, _msgId, self)
        self.updateTSysTopicComment(comments, _request)

    def _loadSysTopicComments(self, _connId, _msgId, _is):
        topicId = str()
        topicId = _is.readString()
        _request = ITableSaver_Loadsystopiccomments_Request(_connId, _msgId, self)
        self.loadSysTopicComments(topicId, _request)

    def _querySysTopicUpvoteStatus(self, _connId, _msgId, _is):
        userId = str()
        userId = _is.readString()
        sysTopicIdList = message.common.publicdef.SeqString()
        sysTopicIdList._read(_is)
        _request = ITableSaver_Querysystopicupvotestatus_Request(_connId, _msgId, self)
        self.querySysTopicUpvoteStatus(userId, sysTopicIdList, _request)

    def _removeSysTopicUpvote(self, _connId, _msgId, _is):
        topicId = str()
        topicId = _is.readString()
        userId = str()
        userId = _is.readString()
        _request = ITableSaver_Removesystopicupvote_Request(_connId, _msgId, self)
        self.removeSysTopicUpvote(topicId, userId, _request)

    def _updateTUserPost(self, _connId, _msgId, _is):
        userPost = message.db.mongodb.posttables.TUserPost()
        userPost._read(_is)
        _request = ITableSaver_Updatetuserpost_Request(_connId, _msgId, self)
        self.updateTUserPost(userPost, _request)

    def _updateTUserPostBatch(self, _connId, _msgId, _is):
        userPostList = message.db.mongodb.posttables.SeqTUserPost()
        userPostList._read(_is)
        _request = ITableSaver_Updatetuserpostbatch_Request(_connId, _msgId, self)
        self.updateTUserPostBatch(userPostList, _request)

    def _loadUserPosts(self, _connId, _msgId, _is):
        pageIndex = int()
        pageIndex = _is.readInt()
        numPerPage = int()
        numPerPage = _is.readInt()
        _request = ITableSaver_Loaduserposts_Request(_connId, _msgId, self)
        self.loadUserPosts(pageIndex, numPerPage, _request)

    def _updateTUserPostComment(self, _connId, _msgId, _is):
        comments = message.db.mongodb.posttables.TUserPostComment()
        comments._read(_is)
        _request = ITableSaver_Updatetuserpostcomment_Request(_connId, _msgId, self)
        self.updateTUserPostComment(comments, _request)

    def _loadUserPostComments(self, _connId, _msgId, _is):
        postId = str()
        postId = _is.readString()
        _request = ITableSaver_Loaduserpostcomments_Request(_connId, _msgId, self)
        self.loadUserPostComments(postId, _request)

    def _queryUserPostUpvoteStatus(self, _connId, _msgId, _is):
        userId = str()
        userId = _is.readString()
        postIdList = message.common.publicdef.SeqString()
        postIdList._read(_is)
        _request = ITableSaver_Queryuserpostupvotestatus_Request(_connId, _msgId, self)
        self.queryUserPostUpvoteStatus(userId, postIdList, _request)

    def _removeUserPostUpvote(self, _connId, _msgId, _is):
        postId = str()
        postId = _is.readString()
        userId = str()
        userId = _is.readString()
        _request = ITableSaver_Removeuserpostupvote_Request(_connId, _msgId, self)
        self.removeUserPostUpvote(postId, userId, _request)

    def _saveUserImages(self, _connId, _msgId, _is):
        userImages = message.db.mongodb.usertables.SeqTUserImage()
        userImages._read(_is)
        _request = ITableSaver_Saveuserimages_Request(_connId, _msgId, self)
        self.saveUserImages(userImages, _request)

    def _userImagesDidUpload(self, _connId, _msgId, _is):
        imageKeys = message.common.publicdef.SeqString()
        imageKeys._read(_is)
        _request = ITableSaver_Userimagesdidupload_Request(_connId, _msgId, self)
        self.userImagesDidUpload(imageKeys, _request)

    def _updateFanInfo(self, _connId, _msgId, _is):
        fanInfo = message.db.mongodb.usertables.TUserFan()
        fanInfo._read(_is)
        _request = ITableSaver_Updatefaninfo_Request(_connId, _msgId, self)
        self.updateFanInfo(fanInfo, _request)

    def _getFansByUserIdAndPageIndex(self, _connId, _msgId, _is):
        userId = str()
        userId = _is.readString()
        pageIdx = int()
        pageIdx = _is.readInt()
        _request = ITableSaver_Getfansbyuseridandpageindex_Request(_connId, _msgId, self)
        self.getFansByUserIdAndPageIndex(userId, pageIdx, _request)

    def _getFocusUseIdList(self, _connId, _msgId, _is):
        userId = str()
        userId = _is.readString()
        _request = ITableSaver_Getfocususeidlist_Request(_connId, _msgId, self)
        self.getFocusUseIdList(userId, _request)

    def _hasFollowed(self, _connId, _msgId, _is):
        myUserId = str()
        myUserId = _is.readString()
        focusUserId = str()
        focusUserId = _is.readString()
        _request = ITableSaver_Hasfollowed_Request(_connId, _msgId, self)
        self.hasFollowed(myUserId, focusUserId, _request)

    def _unfollow(self, _connId, _msgId, _is):
        myUserId = str()
        myUserId = _is.readString()
        hisUserId = str()
        hisUserId = _is.readString()
        _request = ITableSaver_Unfollow_Request(_connId, _msgId, self)
        self.unfollow(myUserId, hisUserId, _request)


    @abc.abstractmethod
    def updateTUserAddress(self, userAddresss, _request):
        """
        :type userAddresss: message.db.mongodb.usertables.TUserAddress
        :type _request: message.db.itablesaver.ITableSaver_Updatetuseraddress_Request
        """
        pass

    @abc.abstractmethod
    def updateTUserBasic(self, userBasic, _request):
        """
        :type userBasic: message.db.mongodb.usertables.TUserBasic
        :type _request: message.db.itablesaver.ITableSaver_Updatetuserbasic_Request
        """
        pass

    @abc.abstractmethod
    def updateTUserSettings(self, userSettings, _request):
        """
        :type userSettings: message.db.mongodb.usertables.TUserSettings
        :type _request: message.db.itablesaver.ITableSaver_Updatetusersettings_Request
        """
        pass

    @abc.abstractmethod
    def updateTUserProperty(self, userProperty, _request):
        """
        :type userProperty: message.db.mongodb.usertables.TUserProperty
        :type _request: message.db.itablesaver.ITableSaver_Updatetuserproperty_Request
        """
        pass

    @abc.abstractmethod
    def updateTFamilyMember(self, familyMember, _request):
        """
        :type familyMember: message.db.mongodb.usertables.TFamilyMember
        :type _request: message.db.itablesaver.ITableSaver_Updatetfamilymember_Request
        """
        pass

    @abc.abstractmethod
    def updateTFamilyMemberBatch(self, familyMembers, _request):
        """
        :type familyMembers: list[message.db.mongodb.usertables.TFamilyMember]
        :type _request: message.db.itablesaver.ITableSaver_Updatetfamilymemberbatch_Request
        """
        pass

    @abc.abstractmethod
    def removeFamilyMembers(self, userId, indexes, _request):
        """
        :type userId: str
        :type indexes: list[int]
        :type _request: message.db.itablesaver.ITableSaver_Removefamilymembers_Request
        """
        pass

    @abc.abstractmethod
    def updateTSysTopic(self, sysTopic, _request):
        """
        :type sysTopic: message.db.mongodb.posttables.TSysTopic
        :type _request: message.db.itablesaver.ITableSaver_Updatetsystopic_Request
        """
        pass

    @abc.abstractmethod
    def loadSysTopics(self, pageIndex, numPerPage, _request):
        """
        :type pageIndex: int
        :type numPerPage: int
        :type _request: message.db.itablesaver.ITableSaver_Loadsystopics_Request
        """
        pass

    @abc.abstractmethod
    def updateTSysTopicComment(self, comments, _request):
        """
        :type comments: message.db.mongodb.posttables.TSysTopicComment
        :type _request: message.db.itablesaver.ITableSaver_Updatetsystopiccomment_Request
        """
        pass

    @abc.abstractmethod
    def loadSysTopicComments(self, topicId, _request):
        """
        :type topicId: str
        :type _request: message.db.itablesaver.ITableSaver_Loadsystopiccomments_Request
        """
        pass

    @abc.abstractmethod
    def querySysTopicUpvoteStatus(self, userId, sysTopicIdList, _request):
        """
        :type userId: str
        :type sysTopicIdList: list[str]
        :type _request: message.db.itablesaver.ITableSaver_Querysystopicupvotestatus_Request
        """
        pass

    @abc.abstractmethod
    def removeSysTopicUpvote(self, topicId, userId, _request):
        """
        :type topicId: str
        :type userId: str
        :type _request: message.db.itablesaver.ITableSaver_Removesystopicupvote_Request
        """
        pass

    @abc.abstractmethod
    def updateTUserPost(self, userPost, _request):
        """
        :type userPost: message.db.mongodb.posttables.TUserPost
        :type _request: message.db.itablesaver.ITableSaver_Updatetuserpost_Request
        """
        pass

    @abc.abstractmethod
    def updateTUserPostBatch(self, userPostList, _request):
        """
        :type userPostList: list[message.db.mongodb.posttables.TUserPost]
        :type _request: message.db.itablesaver.ITableSaver_Updatetuserpostbatch_Request
        """
        pass

    @abc.abstractmethod
    def loadUserPosts(self, pageIndex, numPerPage, _request):
        """
        :type pageIndex: int
        :type numPerPage: int
        :type _request: message.db.itablesaver.ITableSaver_Loaduserposts_Request
        """
        pass

    @abc.abstractmethod
    def updateTUserPostComment(self, comments, _request):
        """
        :type comments: message.db.mongodb.posttables.TUserPostComment
        :type _request: message.db.itablesaver.ITableSaver_Updatetuserpostcomment_Request
        """
        pass

    @abc.abstractmethod
    def loadUserPostComments(self, postId, _request):
        """
        :type postId: str
        :type _request: message.db.itablesaver.ITableSaver_Loaduserpostcomments_Request
        """
        pass

    @abc.abstractmethod
    def queryUserPostUpvoteStatus(self, userId, postIdList, _request):
        """
        :type userId: str
        :type postIdList: list[str]
        :type _request: message.db.itablesaver.ITableSaver_Queryuserpostupvotestatus_Request
        """
        pass

    @abc.abstractmethod
    def removeUserPostUpvote(self, postId, userId, _request):
        """
        :type postId: str
        :type userId: str
        :type _request: message.db.itablesaver.ITableSaver_Removeuserpostupvote_Request
        """
        pass

    @abc.abstractmethod
    def saveUserImages(self, userImages, _request):
        """
        :type userImages: list[message.db.mongodb.usertables.TUserImage]
        :type _request: message.db.itablesaver.ITableSaver_Saveuserimages_Request
        """
        pass

    @abc.abstractmethod
    def userImagesDidUpload(self, imageKeys, _request):
        """
        :type imageKeys: list[str]
        :type _request: message.db.itablesaver.ITableSaver_Userimagesdidupload_Request
        """
        pass

    @abc.abstractmethod
    def updateFanInfo(self, fanInfo, _request):
        """
        :type fanInfo: message.db.mongodb.usertables.TUserFan
        :type _request: message.db.itablesaver.ITableSaver_Updatefaninfo_Request
        """
        pass

    @abc.abstractmethod
    def getFansByUserIdAndPageIndex(self, userId, pageIdx, _request):
        """
        :type userId: str
        :type pageIdx: int
        :type _request: message.db.itablesaver.ITableSaver_Getfansbyuseridandpageindex_Request
        """
        pass

    @abc.abstractmethod
    def getFocusUseIdList(self, userId, _request):
        """
        :type userId: str
        :type _request: message.db.itablesaver.ITableSaver_Getfocususeidlist_Request
        """
        pass

    @abc.abstractmethod
    def hasFollowed(self, myUserId, focusUserId, _request):
        """
        :type myUserId: str
        :type focusUserId: str
        :type _request: message.db.itablesaver.ITableSaver_Hasfollowed_Request
        """
        pass

    @abc.abstractmethod
    def unfollow(self, myUserId, hisUserId, _request):
        """
        :type myUserId: str
        :type hisUserId: str
        :type _request: message.db.itablesaver.ITableSaver_Unfollow_Request
        """
        pass

# message.db.itablesaver.ITableSaverProxy
class ITableSaverProxy(RmiProxy):
    def __init__(self, name='ITableSaver'):
        super().__init__(name)

    def updateTUserAddress(self, _response, userAddresss):
        """
        :type _response: ITableSaver_Updatetuseraddress_Response
        :type userAddresss: message.db.mongodb.usertables.TUserAddress
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateTUserAddress')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        userAddresss._write(_os)
        self.invoke(_os, _response)

    def updateTUserBasic(self, _response, userBasic):
        """
        :type _response: ITableSaver_Updatetuserbasic_Response
        :type userBasic: message.db.mongodb.usertables.TUserBasic
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateTUserBasic')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        userBasic._write(_os)
        self.invoke(_os, _response)

    def updateTUserSettings(self, _response, userSettings):
        """
        :type _response: ITableSaver_Updatetusersettings_Response
        :type userSettings: message.db.mongodb.usertables.TUserSettings
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateTUserSettings')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        userSettings._write(_os)
        self.invoke(_os, _response)

    def updateTUserProperty(self, _response, userProperty):
        """
        :type _response: ITableSaver_Updatetuserproperty_Response
        :type userProperty: message.db.mongodb.usertables.TUserProperty
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateTUserProperty')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        userProperty._write(_os)
        self.invoke(_os, _response)

    def updateTFamilyMember(self, _response, familyMember):
        """
        :type _response: ITableSaver_Updatetfamilymember_Response
        :type familyMember: message.db.mongodb.usertables.TFamilyMember
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateTFamilyMember')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        familyMember._write(_os)
        self.invoke(_os, _response)

    def updateTFamilyMemberBatch(self, _response, familyMembers):
        """
        :type _response: ITableSaver_Updatetfamilymemberbatch_Response
        :type familyMembers: list[message.db.mongodb.usertables.TFamilyMember]
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateTFamilyMemberBatch')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        familyMembers._write(_os)
        self.invoke(_os, _response)

    def removeFamilyMembers(self, _response, userId, indexes):
        """
        :type _response: ITableSaver_Removefamilymembers_Response
        :type userId: str
        :type indexes: list[int]
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('removeFamilyMembers')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(userId)
        indexes._write(_os)
        self.invoke(_os, _response)

    def updateTSysTopic(self, _response, sysTopic):
        """
        :type _response: ITableSaver_Updatetsystopic_Response
        :type sysTopic: message.db.mongodb.posttables.TSysTopic
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateTSysTopic')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        sysTopic._write(_os)
        self.invoke(_os, _response)

    def loadSysTopics(self, _response, pageIndex, numPerPage):
        """
        :type _response: ITableSaver_Loadsystopics_Response
        :type pageIndex: int
        :type numPerPage: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('loadSysTopics')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeInt(pageIndex)
        _os.writeInt(numPerPage)
        self.invoke(_os, _response)

    def updateTSysTopicComment(self, _response, comments):
        """
        :type _response: ITableSaver_Updatetsystopiccomment_Response
        :type comments: message.db.mongodb.posttables.TSysTopicComment
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateTSysTopicComment')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        comments._write(_os)
        self.invoke(_os, _response)

    def loadSysTopicComments(self, _response, topicId):
        """
        :type _response: ITableSaver_Loadsystopiccomments_Response
        :type topicId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('loadSysTopicComments')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(topicId)
        self.invoke(_os, _response)

    def querySysTopicUpvoteStatus(self, _response, userId, sysTopicIdList):
        """
        :type _response: ITableSaver_Querysystopicupvotestatus_Response
        :type userId: str
        :type sysTopicIdList: list[str]
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('querySysTopicUpvoteStatus')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(userId)
        sysTopicIdList._write(_os)
        self.invoke(_os, _response)

    def removeSysTopicUpvote(self, _response, topicId, userId):
        """
        :type _response: ITableSaver_Removesystopicupvote_Response
        :type topicId: str
        :type userId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('removeSysTopicUpvote')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(topicId)
        _os.writeString(userId)
        self.invoke(_os, _response)

    def updateTUserPost(self, _response, userPost):
        """
        :type _response: ITableSaver_Updatetuserpost_Response
        :type userPost: message.db.mongodb.posttables.TUserPost
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateTUserPost')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        userPost._write(_os)
        self.invoke(_os, _response)

    def updateTUserPostBatch(self, _response, userPostList):
        """
        :type _response: ITableSaver_Updatetuserpostbatch_Response
        :type userPostList: list[message.db.mongodb.posttables.TUserPost]
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateTUserPostBatch')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        userPostList._write(_os)
        self.invoke(_os, _response)

    def loadUserPosts(self, _response, pageIndex, numPerPage):
        """
        :type _response: ITableSaver_Loaduserposts_Response
        :type pageIndex: int
        :type numPerPage: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('loadUserPosts')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeInt(pageIndex)
        _os.writeInt(numPerPage)
        self.invoke(_os, _response)

    def updateTUserPostComment(self, _response, comments):
        """
        :type _response: ITableSaver_Updatetuserpostcomment_Response
        :type comments: message.db.mongodb.posttables.TUserPostComment
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateTUserPostComment')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        comments._write(_os)
        self.invoke(_os, _response)

    def loadUserPostComments(self, _response, postId):
        """
        :type _response: ITableSaver_Loaduserpostcomments_Response
        :type postId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('loadUserPostComments')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(postId)
        self.invoke(_os, _response)

    def queryUserPostUpvoteStatus(self, _response, userId, postIdList):
        """
        :type _response: ITableSaver_Queryuserpostupvotestatus_Response
        :type userId: str
        :type postIdList: list[str]
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('queryUserPostUpvoteStatus')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(userId)
        postIdList._write(_os)
        self.invoke(_os, _response)

    def removeUserPostUpvote(self, _response, postId, userId):
        """
        :type _response: ITableSaver_Removeuserpostupvote_Response
        :type postId: str
        :type userId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('removeUserPostUpvote')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(postId)
        _os.writeString(userId)
        self.invoke(_os, _response)

    def saveUserImages(self, _response, userImages):
        """
        :type _response: ITableSaver_Saveuserimages_Response
        :type userImages: list[message.db.mongodb.usertables.TUserImage]
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('saveUserImages')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        userImages._write(_os)
        self.invoke(_os, _response)

    def userImagesDidUpload(self, _response, imageKeys):
        """
        :type _response: ITableSaver_Userimagesdidupload_Response
        :type imageKeys: list[str]
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('userImagesDidUpload')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        imageKeys._write(_os)
        self.invoke(_os, _response)

    def updateFanInfo(self, _response, fanInfo):
        """
        :type _response: ITableSaver_Updatefaninfo_Response
        :type fanInfo: message.db.mongodb.usertables.TUserFan
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateFanInfo')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        fanInfo._write(_os)
        self.invoke(_os, _response)

    def getFansByUserIdAndPageIndex(self, _response, userId, pageIdx):
        """
        :type _response: ITableSaver_Getfansbyuseridandpageindex_Response
        :type userId: str
        :type pageIdx: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getFansByUserIdAndPageIndex')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(userId)
        _os.writeInt(pageIdx)
        self.invoke(_os, _response)

    def getFocusUseIdList(self, _response, userId):
        """
        :type _response: ITableSaver_Getfocususeidlist_Response
        :type userId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getFocusUseIdList')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(userId)
        self.invoke(_os, _response)

    def hasFollowed(self, _response, myUserId, focusUserId):
        """
        :type _response: ITableSaver_Hasfollowed_Response
        :type myUserId: str
        :type focusUserId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('hasFollowed')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(myUserId)
        _os.writeString(focusUserId)
        self.invoke(_os, _response)

    def unfollow(self, _response, myUserId, hisUserId):
        """
        :type _response: ITableSaver_Unfollow_Response
        :type myUserId: str
        :type hisUserId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('unfollow')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(myUserId)
        _os.writeString(hisUserId)
        self.invoke(_os, _response)


