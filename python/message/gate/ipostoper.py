#
# file: ipostoper.py
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
import message.gate.gateconst
import message.gate.gatemsg


class IPostOper_Getsyshints_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, msgHintList):
        if not isinstance(msgHintList, message.gate.gatemsg.SeqMsgHint):
            raise Exception("msgHintList must be instance of message.gate.gatemsg.SeqMsgHint", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        msgHintList._write(_os)

        self.sendout()

class IPostOper_Getpostcommentshints_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, postCommentHint):
        if not isinstance(postCommentHint, message.gate.gatemsg.SeqUserPostCommentHint):
            raise Exception("postCommentHint must be instance of message.gate.gatemsg.SeqUserPostCommentHint", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        postCommentHint._write(_os)

        self.sendout()

class IPostOper_Getfansbypageindex_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, myFanList):
        if not isinstance(myFanList, message.gate.gatemsg.SeqMyFan):
            raise Exception("myFanList must be instance of message.gate.gatemsg.SeqMyFan", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        myFanList._write(_os)

        self.sendout()

class IPostOper_Getallmyfocuses_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, myFocusList):
        if not isinstance(myFocusList, message.gate.gatemsg.SeqMyFocus):
            raise Exception("myFocusList must be instance of message.gate.gatemsg.SeqMyFocus", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        myFocusList._write(_os)

        self.sendout()

class IPostOper_Getnewfanlist_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, newFanList):
        if not isinstance(newFanList, message.gate.gatemsg.SeqMyFan):
            raise Exception("newFanList must be instance of message.gate.gatemsg.SeqMyFan", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        newFanList._write(_os)

        self.sendout()

class IPostOper_Followauser_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, newFocus):
        if not isinstance(newFocus, message.gate.gatemsg.SMyFocus):
            raise Exception("newFocus must be instance of message.gate.gatemsg.SMyFocus", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        newFocus._write(_os)

        self.sendout()

class IPostOper_Unfollowauser_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IPostOper_Getlatestsystopics_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, sysTopicList):
        if not isinstance(sysTopicList, message.gate.gatemsg.SeqSysTopic):
            raise Exception("sysTopicList must be instance of message.gate.gatemsg.SeqSysTopic", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        sysTopicList._write(_os)

        self.sendout()

class IPostOper_Getformersystopics_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, sysTopicList):
        if not isinstance(sysTopicList, message.gate.gatemsg.SeqSysTopic):
            raise Exception("sysTopicList must be instance of message.gate.gatemsg.SeqSysTopic", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        sysTopicList._write(_os)

        self.sendout()

class IPostOper_Getsystopiccomments_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, commentList):
        if not isinstance(commentList, message.gate.gatemsg.SeqComment):
            raise Exception("commentList must be instance of message.gate.gatemsg.SeqComment", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        commentList._write(_os)

        self.sendout()

class IPostOper_Getsystopicbytopicid_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, sysTopic):
        if not isinstance(sysTopic, message.gate.gatemsg.SSysTopic):
            raise Exception("sysTopic must be instance of message.gate.gatemsg.SSysTopic", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        sysTopic._write(_os)

        self.sendout()

class IPostOper_Upvotesystopic_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IPostOper_Unupvotesystopic_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IPostOper_Sharesystopic_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IPostOper_Commentsystopic_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, newCommentId):
        if not isinstance(newCommentId, str):
            raise Exception("newCommentId must be instance of string", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeString(newCommentId)

        self.sendout()

class IPostOper_Replysystopiccomment_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, newCommentId):
        if not isinstance(newCommentId, str):
            raise Exception("newCommentId must be instance of string", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeString(newCommentId)

        self.sendout()

class IPostOper_Querysystopicupvotestatus_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, sysTopicUpvoteStatusDict):
        if not isinstance(sysTopicUpvoteStatusDict, message.common.publicdef.DictStringBool):
            raise Exception("sysTopicUpvoteStatusDict must be instance of message.common.publicdef.DictStringBool", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        sysTopicUpvoteStatusDict._write(_os)

        self.sendout()

class IPostOper_Viewsystopic_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, totalViewTimes):
        if not isinstance(totalViewTimes, int):
            raise Exception("totalViewTimes must be instance of int", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeInt(totalViewTimes)

        self.sendout()

class IPostOper_Getlatestuserposts_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, userPostList):
        if not isinstance(userPostList, message.gate.gatemsg.SeqUserPost):
            raise Exception("userPostList must be instance of message.gate.gatemsg.SeqUserPost", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        userPostList._write(_os)

        self.sendout()

class IPostOper_Getformeruserposts_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, userPostList):
        if not isinstance(userPostList, message.gate.gatemsg.SeqUserPost):
            raise Exception("userPostList must be instance of message.gate.gatemsg.SeqUserPost", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        userPostList._write(_os)

        self.sendout()

class IPostOper_Getuserpostbypostid_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, userPost):
        if not isinstance(userPost, message.gate.gatemsg.SUserPost):
            raise Exception("userPost must be instance of message.gate.gatemsg.SUserPost", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        userPost._write(_os)

        self.sendout()

class IPostOper_Getuserpostcomments_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, commentList):
        if not isinstance(commentList, message.gate.gatemsg.SeqComment):
            raise Exception("commentList must be instance of message.gate.gatemsg.SeqComment", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        commentList._write(_os)

        self.sendout()

class IPostOper_Commituserpost_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, postId, imageInfos):
        if not isinstance(postId, str):
            raise Exception("postId must be instance of string", 0)

        if not isinstance(imageInfos, message.gate.gatemsg.SeqImageInfo):
            raise Exception("imageInfos must be instance of message.gate.gatemsg.SeqImageInfo", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeString(postId)
        imageInfos._write(_os)

        self.sendout()

class IPostOper_Didimageupload_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IPostOper_Getimageuploadtokens_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, imageInfos):
        if not isinstance(imageInfos, message.gate.gatemsg.SeqImageInfo):
            raise Exception("imageInfos must be instance of message.gate.gatemsg.SeqImageInfo", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        imageInfos._write(_os)

        self.sendout()

class IPostOper_Getimagedownloadtokens_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, imgDowloadToken):
        if not isinstance(imgDowloadToken, message.gate.gatemsg.SImageInfo):
            raise Exception("imgDowloadToken must be instance of message.gate.gatemsg.SImageInfo", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        imgDowloadToken._write(_os)

        self.sendout()

class IPostOper_Upvoteuserpost_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IPostOper_Unupvoteuserpost_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IPostOper_Shareuserpost_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IPostOper_Commentuserpost_Request(RmiRequestBase):
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

class IPostOper_Replyuserpostcomment_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, newCommentId):
        if not isinstance(newCommentId, str):
            raise Exception("newCommentId must be instance of string", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeString(newCommentId)

        self.sendout()

class IPostOper_Queryuserpostupvotestatus_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, postUpvatedStatusDict):
        if not isinstance(postUpvatedStatusDict, message.common.publicdef.DictStringBool):
            raise Exception("postUpvatedStatusDict must be instance of message.common.publicdef.DictStringBool", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        postUpvatedStatusDict._write(_os)

        self.sendout()

class IPostOper_Viewuserpost_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, totalViewTimes):
        if not isinstance(totalViewTimes, int):
            raise Exception("totalViewTimes must be instance of int", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeInt(totalViewTimes)

        self.sendout()

class IPostOper_Getmyuserbydatethreshold_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, userPostList):
        if not isinstance(userPostList, message.gate.gatemsg.SeqUserPost):
            raise Exception("userPostList must be instance of message.gate.gatemsg.SeqUserPost", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        userPostList._write(_os)

        self.sendout()

class IPostOper_Deleteuserpost_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IPostOper_Getsyshints_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        msgHintList = message.gate.gatemsg.SeqMsgHint()
        msgHintList._read(_is)

        self.onResponse(msgHintList)

    @abc.abstractmethod
    def onResponse(self, msgHintList):
        """
        :type msgHintList: list[message.gate.gatemsg.SMsgHint]
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


class IPostOper_Getpostcommentshints_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        postCommentHint = message.gate.gatemsg.SeqUserPostCommentHint()
        postCommentHint._read(_is)

        self.onResponse(postCommentHint)

    @abc.abstractmethod
    def onResponse(self, postCommentHint):
        """
        :type postCommentHint: list[message.gate.gatemsg.SUserPostCommentHint]
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


class IPostOper_Getfansbypageindex_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        myFanList = message.gate.gatemsg.SeqMyFan()
        myFanList._read(_is)

        self.onResponse(myFanList)

    @abc.abstractmethod
    def onResponse(self, myFanList):
        """
        :type myFanList: list[message.gate.gatemsg.SMyFan]
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


class IPostOper_Getallmyfocuses_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        myFocusList = message.gate.gatemsg.SeqMyFocus()
        myFocusList._read(_is)

        self.onResponse(myFocusList)

    @abc.abstractmethod
    def onResponse(self, myFocusList):
        """
        :type myFocusList: list[message.gate.gatemsg.SMyFocus]
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


class IPostOper_Getnewfanlist_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        newFanList = message.gate.gatemsg.SeqMyFan()
        newFanList._read(_is)

        self.onResponse(newFanList)

    @abc.abstractmethod
    def onResponse(self, newFanList):
        """
        :type newFanList: list[message.gate.gatemsg.SMyFan]
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


class IPostOper_Followauser_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        newFocus = message.gate.gatemsg.SMyFocus()
        newFocus._read(_is)

        self.onResponse(newFocus)

    @abc.abstractmethod
    def onResponse(self, newFocus):
        """
        :type newFocus: message.gate.gatemsg.SMyFocus
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


class IPostOper_Unfollowauser_Response(RmiResponseBase):
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


class IPostOper_Getlatestsystopics_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        sysTopicList = message.gate.gatemsg.SeqSysTopic()
        sysTopicList._read(_is)

        self.onResponse(sysTopicList)

    @abc.abstractmethod
    def onResponse(self, sysTopicList):
        """
        :type sysTopicList: list[message.gate.gatemsg.SSysTopic]
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


class IPostOper_Getformersystopics_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        sysTopicList = message.gate.gatemsg.SeqSysTopic()
        sysTopicList._read(_is)

        self.onResponse(sysTopicList)

    @abc.abstractmethod
    def onResponse(self, sysTopicList):
        """
        :type sysTopicList: list[message.gate.gatemsg.SSysTopic]
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


class IPostOper_Getsystopiccomments_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        commentList = message.gate.gatemsg.SeqComment()
        commentList._read(_is)

        self.onResponse(commentList)

    @abc.abstractmethod
    def onResponse(self, commentList):
        """
        :type commentList: list[message.gate.gatemsg.SComment]
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


class IPostOper_Getsystopicbytopicid_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        sysTopic = message.gate.gatemsg.SSysTopic()
        sysTopic._read(_is)

        self.onResponse(sysTopic)

    @abc.abstractmethod
    def onResponse(self, sysTopic):
        """
        :type sysTopic: message.gate.gatemsg.SSysTopic
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


class IPostOper_Upvotesystopic_Response(RmiResponseBase):
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


class IPostOper_Unupvotesystopic_Response(RmiResponseBase):
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


class IPostOper_Sharesystopic_Response(RmiResponseBase):
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


class IPostOper_Commentsystopic_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        newCommentId = str()
        newCommentId = _is.readString()

        self.onResponse(newCommentId)

    @abc.abstractmethod
    def onResponse(self, newCommentId):
        """
        :type newCommentId: str
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


class IPostOper_Replysystopiccomment_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        newCommentId = str()
        newCommentId = _is.readString()

        self.onResponse(newCommentId)

    @abc.abstractmethod
    def onResponse(self, newCommentId):
        """
        :type newCommentId: str
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


class IPostOper_Querysystopicupvotestatus_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        sysTopicUpvoteStatusDict = message.common.publicdef.DictStringBool()
        sysTopicUpvoteStatusDict._read(_is)

        self.onResponse(sysTopicUpvoteStatusDict)

    @abc.abstractmethod
    def onResponse(self, sysTopicUpvoteStatusDict):
        """
        :type sysTopicUpvoteStatusDict: dict[str, bool]
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


class IPostOper_Viewsystopic_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        totalViewTimes = int()
        totalViewTimes = _is.readInt()

        self.onResponse(totalViewTimes)

    @abc.abstractmethod
    def onResponse(self, totalViewTimes):
        """
        :type totalViewTimes: int
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


class IPostOper_Getlatestuserposts_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        userPostList = message.gate.gatemsg.SeqUserPost()
        userPostList._read(_is)

        self.onResponse(userPostList)

    @abc.abstractmethod
    def onResponse(self, userPostList):
        """
        :type userPostList: list[message.gate.gatemsg.SUserPost]
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


class IPostOper_Getformeruserposts_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        userPostList = message.gate.gatemsg.SeqUserPost()
        userPostList._read(_is)

        self.onResponse(userPostList)

    @abc.abstractmethod
    def onResponse(self, userPostList):
        """
        :type userPostList: list[message.gate.gatemsg.SUserPost]
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


class IPostOper_Getuserpostbypostid_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        userPost = message.gate.gatemsg.SUserPost()
        userPost._read(_is)

        self.onResponse(userPost)

    @abc.abstractmethod
    def onResponse(self, userPost):
        """
        :type userPost: message.gate.gatemsg.SUserPost
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


class IPostOper_Getuserpostcomments_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        commentList = message.gate.gatemsg.SeqComment()
        commentList._read(_is)

        self.onResponse(commentList)

    @abc.abstractmethod
    def onResponse(self, commentList):
        """
        :type commentList: list[message.gate.gatemsg.SComment]
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


class IPostOper_Commituserpost_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        postId = str()
        postId = _is.readString()
        imageInfos = message.gate.gatemsg.SeqImageInfo()
        imageInfos._read(_is)

        self.onResponse(postId, imageInfos)

    @abc.abstractmethod
    def onResponse(self, postId, imageInfos):
        """
        :type postId: str
        :type imageInfos: list[message.gate.gatemsg.SImageInfo]
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


class IPostOper_Didimageupload_Response(RmiResponseBase):
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


class IPostOper_Getimageuploadtokens_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        imageInfos = message.gate.gatemsg.SeqImageInfo()
        imageInfos._read(_is)

        self.onResponse(imageInfos)

    @abc.abstractmethod
    def onResponse(self, imageInfos):
        """
        :type imageInfos: list[message.gate.gatemsg.SImageInfo]
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


class IPostOper_Getimagedownloadtokens_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        imgDowloadToken = message.gate.gatemsg.SImageInfo()
        imgDowloadToken._read(_is)

        self.onResponse(imgDowloadToken)

    @abc.abstractmethod
    def onResponse(self, imgDowloadToken):
        """
        :type imgDowloadToken: message.gate.gatemsg.SImageInfo
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


class IPostOper_Upvoteuserpost_Response(RmiResponseBase):
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


class IPostOper_Unupvoteuserpost_Response(RmiResponseBase):
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


class IPostOper_Shareuserpost_Response(RmiResponseBase):
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


class IPostOper_Commentuserpost_Response(RmiResponseBase):
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


class IPostOper_Replyuserpostcomment_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        newCommentId = str()
        newCommentId = _is.readString()

        self.onResponse(newCommentId)

    @abc.abstractmethod
    def onResponse(self, newCommentId):
        """
        :type newCommentId: str
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


class IPostOper_Queryuserpostupvotestatus_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        postUpvatedStatusDict = message.common.publicdef.DictStringBool()
        postUpvatedStatusDict._read(_is)

        self.onResponse(postUpvatedStatusDict)

    @abc.abstractmethod
    def onResponse(self, postUpvatedStatusDict):
        """
        :type postUpvatedStatusDict: dict[str, bool]
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


class IPostOper_Viewuserpost_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        totalViewTimes = int()
        totalViewTimes = _is.readInt()

        self.onResponse(totalViewTimes)

    @abc.abstractmethod
    def onResponse(self, totalViewTimes):
        """
        :type totalViewTimes: int
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


class IPostOper_Getmyuserbydatethreshold_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        userPostList = message.gate.gatemsg.SeqUserPost()
        userPostList._read(_is)

        self.onResponse(userPostList)

    @abc.abstractmethod
    def onResponse(self, userPostList):
        """
        :type userPostList: list[message.gate.gatemsg.SUserPost]
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


class IPostOper_Deleteuserpost_Response(RmiResponseBase):
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


class IPostOperServant(RmiServant):
    def __init__(self, name='IPostOper'):
        super().__init__(name)
        self.methodMap['getSysHints'] = self._getSysHints
        self.methodMap['getPostCommentsHints'] = self._getPostCommentsHints
        self.methodMap['getFansByPageIndex'] = self._getFansByPageIndex
        self.methodMap['getAllMyFocuses'] = self._getAllMyFocuses
        self.methodMap['getNewFanList'] = self._getNewFanList
        self.methodMap['followAUser'] = self._followAUser
        self.methodMap['unfollowAUser'] = self._unfollowAUser
        self.methodMap['getLatestSysTopics'] = self._getLatestSysTopics
        self.methodMap['getFormerSysTopics'] = self._getFormerSysTopics
        self.methodMap['getSysTopicComments'] = self._getSysTopicComments
        self.methodMap['getSysTopicByTopicId'] = self._getSysTopicByTopicId
        self.methodMap['upvoteSysTopic'] = self._upvoteSysTopic
        self.methodMap['unupvoteSysTopic'] = self._unupvoteSysTopic
        self.methodMap['shareSysTopic'] = self._shareSysTopic
        self.methodMap['commentSysTopic'] = self._commentSysTopic
        self.methodMap['replySysTopicComment'] = self._replySysTopicComment
        self.methodMap['querySysTopicUpvoteStatus'] = self._querySysTopicUpvoteStatus
        self.methodMap['viewSysTopic'] = self._viewSysTopic
        self.methodMap['getLatestUserPosts'] = self._getLatestUserPosts
        self.methodMap['getFormerUserPosts'] = self._getFormerUserPosts
        self.methodMap['getUserPostByPostId'] = self._getUserPostByPostId
        self.methodMap['getUserPostComments'] = self._getUserPostComments
        self.methodMap['commitUserPost'] = self._commitUserPost
        self.methodMap['didImageUpload'] = self._didImageUpload
        self.methodMap['getImageUploadTokens'] = self._getImageUploadTokens
        self.methodMap['getImageDownloadTokens'] = self._getImageDownloadTokens
        self.methodMap['upvoteUserPost'] = self._upvoteUserPost
        self.methodMap['unupvoteUserPost'] = self._unupvoteUserPost
        self.methodMap['shareUserPost'] = self._shareUserPost
        self.methodMap['commentUserPost'] = self._commentUserPost
        self.methodMap['replyUserPostComment'] = self._replyUserPostComment
        self.methodMap['queryUserPostUpvoteStatus'] = self._queryUserPostUpvoteStatus
        self.methodMap['viewUserPost'] = self._viewUserPost
        self.methodMap['getMyUserByDateThreshold'] = self._getMyUserByDateThreshold
        self.methodMap['deleteUserPost'] = self._deleteUserPost

    def _getSysHints(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        _request = IPostOper_Getsyshints_Request(_connId, _msgId, self)
        self.getSysHints(sessionKey, _request)

    def _getPostCommentsHints(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        _request = IPostOper_Getpostcommentshints_Request(_connId, _msgId, self)
        self.getPostCommentsHints(sessionKey, _request)

    def _getFansByPageIndex(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        pageIndex = int()
        pageIndex = _is.readInt()
        _request = IPostOper_Getfansbypageindex_Request(_connId, _msgId, self)
        self.getFansByPageIndex(sessionKey, pageIndex, _request)

    def _getAllMyFocuses(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        _request = IPostOper_Getallmyfocuses_Request(_connId, _msgId, self)
        self.getAllMyFocuses(sessionKey, _request)

    def _getNewFanList(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        _request = IPostOper_Getnewfanlist_Request(_connId, _msgId, self)
        self.getNewFanList(sessionKey, _request)

    def _followAUser(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        userId = str()
        userId = _is.readString()
        _request = IPostOper_Followauser_Request(_connId, _msgId, self)
        self.followAUser(sessionKey, userId, _request)

    def _unfollowAUser(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        userId = str()
        userId = _is.readString()
        _request = IPostOper_Unfollowauser_Request(_connId, _msgId, self)
        self.unfollowAUser(sessionKey, userId, _request)

    def _getLatestSysTopics(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        tagId = str()
        tagId = _is.readString()
        latestTopicDt = datetime.datetime.now()
        latestTopicDt = _is.readDate()
        targetNum = int()
        targetNum = _is.readInt()
        imgFormat = str()
        imgFormat = _is.readString()
        _request = IPostOper_Getlatestsystopics_Request(_connId, _msgId, self)
        self.getLatestSysTopics(deviceCode, tagId, latestTopicDt, targetNum, imgFormat, _request)

    def _getFormerSysTopics(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        tagId = str()
        tagId = _is.readString()
        oldestTopicDt = datetime.datetime.now()
        oldestTopicDt = _is.readDate()
        targetNum = int()
        targetNum = _is.readInt()
        imgFormat = str()
        imgFormat = _is.readString()
        _request = IPostOper_Getformersystopics_Request(_connId, _msgId, self)
        self.getFormerSysTopics(deviceCode, tagId, oldestTopicDt, targetNum, imgFormat, _request)

    def _getSysTopicComments(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        topicId = str()
        topicId = _is.readString()
        interactiveType = message.common.publicdef.EInteractiveType.Upvote
        interactiveType = _is.readInt()
        latestCommentDt = datetime.datetime.now()
        latestCommentDt = _is.readDate()
        targetNum = int()
        targetNum = _is.readInt()
        _request = IPostOper_Getsystopiccomments_Request(_connId, _msgId, self)
        self.getSysTopicComments(deviceCode, topicId, interactiveType, latestCommentDt, targetNum, _request)

    def _getSysTopicByTopicId(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        topicId = str()
        topicId = _is.readString()
        imgFormat = str()
        imgFormat = _is.readString()
        _request = IPostOper_Getsystopicbytopicid_Request(_connId, _msgId, self)
        self.getSysTopicByTopicId(deviceCode, topicId, imgFormat, _request)

    def _upvoteSysTopic(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        topicId = str()
        topicId = _is.readString()
        _request = IPostOper_Upvotesystopic_Request(_connId, _msgId, self)
        self.upvoteSysTopic(sessionKey, topicId, _request)

    def _unupvoteSysTopic(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        topicId = str()
        topicId = _is.readString()
        _request = IPostOper_Unupvotesystopic_Request(_connId, _msgId, self)
        self.unupvoteSysTopic(sessionKey, topicId, _request)

    def _shareSysTopic(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        topicId = str()
        topicId = _is.readString()
        shareType = message.gate.gateconst.EShareType.WeChat
        shareType = _is.readInt()
        _request = IPostOper_Sharesystopic_Request(_connId, _msgId, self)
        self.shareSysTopic(sessionKey, topicId, shareType, _request)

    def _commentSysTopic(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        topicId = str()
        topicId = _is.readString()
        comments = str()
        comments = _is.readString()
        _request = IPostOper_Commentsystopic_Request(_connId, _msgId, self)
        self.commentSysTopic(sessionKey, topicId, comments, _request)

    def _replySysTopicComment(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        topicId = str()
        topicId = _is.readString()
        dstCommentId = str()
        dstCommentId = _is.readString()
        mentionedUserId = str()
        mentionedUserId = _is.readString()
        comments = str()
        comments = _is.readString()
        _request = IPostOper_Replysystopiccomment_Request(_connId, _msgId, self)
        self.replySysTopicComment(sessionKey, topicId, dstCommentId, mentionedUserId, comments, _request)

    def _querySysTopicUpvoteStatus(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        sysTopicIdList = message.common.publicdef.SeqString()
        sysTopicIdList._read(_is)
        _request = IPostOper_Querysystopicupvotestatus_Request(_connId, _msgId, self)
        self.querySysTopicUpvoteStatus(sessionKey, sysTopicIdList, _request)

    def _viewSysTopic(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        sysTopicId = str()
        sysTopicId = _is.readString()
        _request = IPostOper_Viewsystopic_Request(_connId, _msgId, self)
        self.viewSysTopic(deviceCode, sysTopicId, _request)

    def _getLatestUserPosts(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        tag = str()
        tag = _is.readString()
        latestPostDt = datetime.datetime.now()
        latestPostDt = _is.readDate()
        targetNum = int()
        targetNum = _is.readInt()
        imgFormat = str()
        imgFormat = _is.readString()
        _request = IPostOper_Getlatestuserposts_Request(_connId, _msgId, self)
        self.getLatestUserPosts(deviceCode, tag, latestPostDt, targetNum, imgFormat, _request)

    def _getFormerUserPosts(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        tag = str()
        tag = _is.readString()
        oldestPostDt = datetime.datetime.now()
        oldestPostDt = _is.readDate()
        targetNum = int()
        targetNum = _is.readInt()
        imgFormat = str()
        imgFormat = _is.readString()
        _request = IPostOper_Getformeruserposts_Request(_connId, _msgId, self)
        self.getFormerUserPosts(deviceCode, tag, oldestPostDt, targetNum, imgFormat, _request)

    def _getUserPostByPostId(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        postId = str()
        postId = _is.readString()
        imgFormat = str()
        imgFormat = _is.readString()
        _request = IPostOper_Getuserpostbypostid_Request(_connId, _msgId, self)
        self.getUserPostByPostId(deviceCode, postId, imgFormat, _request)

    def _getUserPostComments(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        postId = str()
        postId = _is.readString()
        latestCommentDt = datetime.datetime.now()
        latestCommentDt = _is.readDate()
        targetNum = int()
        targetNum = _is.readInt()
        _request = IPostOper_Getuserpostcomments_Request(_connId, _msgId, self)
        self.getUserPostComments(deviceCode, postId, latestCommentDt, targetNum, _request)

    def _commitUserPost(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        title = str()
        title = _is.readString()
        content = str()
        content = _is.readString()
        tags = message.common.publicdef.SeqString()
        tags._read(_is)
        imageNum = int()
        imageNum = _is.readInt()
        _request = IPostOper_Commituserpost_Request(_connId, _msgId, self)
        self.commitUserPost(sessionKey, title, content, tags, imageNum, _request)

    def _didImageUpload(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        imageKeys = message.common.publicdef.SeqString()
        imageKeys._read(_is)
        _request = IPostOper_Didimageupload_Request(_connId, _msgId, self)
        self.didImageUpload(sessionKey, imageKeys, _request)

    def _getImageUploadTokens(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        imgNum = int()
        imgNum = _is.readInt()
        _request = IPostOper_Getimageuploadtokens_Request(_connId, _msgId, self)
        self.getImageUploadTokens(sessionKey, imgNum, _request)

    def _getImageDownloadTokens(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        imgKey = str()
        imgKey = _is.readString()
        imgFormat = str()
        imgFormat = _is.readString()
        _request = IPostOper_Getimagedownloadtokens_Request(_connId, _msgId, self)
        self.getImageDownloadTokens(sessionKey, imgKey, imgFormat, _request)

    def _upvoteUserPost(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        postId = str()
        postId = _is.readString()
        _request = IPostOper_Upvoteuserpost_Request(_connId, _msgId, self)
        self.upvoteUserPost(sessionKey, postId, _request)

    def _unupvoteUserPost(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        postId = str()
        postId = _is.readString()
        _request = IPostOper_Unupvoteuserpost_Request(_connId, _msgId, self)
        self.unupvoteUserPost(sessionKey, postId, _request)

    def _shareUserPost(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        postId = str()
        postId = _is.readString()
        shareType = message.gate.gateconst.EShareType.WeChat
        shareType = _is.readInt()
        _request = IPostOper_Shareuserpost_Request(_connId, _msgId, self)
        self.shareUserPost(sessionKey, postId, shareType, _request)

    def _commentUserPost(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        postId = str()
        postId = _is.readString()
        comments = str()
        comments = _is.readString()
        _request = IPostOper_Commentuserpost_Request(_connId, _msgId, self)
        self.commentUserPost(sessionKey, postId, comments, _request)

    def _replyUserPostComment(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        postId = str()
        postId = _is.readString()
        dstCommentId = str()
        dstCommentId = _is.readString()
        mentionedUserId = str()
        mentionedUserId = _is.readString()
        comments = str()
        comments = _is.readString()
        _request = IPostOper_Replyuserpostcomment_Request(_connId, _msgId, self)
        self.replyUserPostComment(sessionKey, postId, dstCommentId, mentionedUserId, comments, _request)

    def _queryUserPostUpvoteStatus(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        postIdList = message.common.publicdef.SeqString()
        postIdList._read(_is)
        _request = IPostOper_Queryuserpostupvotestatus_Request(_connId, _msgId, self)
        self.queryUserPostUpvoteStatus(sessionKey, postIdList, _request)

    def _viewUserPost(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        postId = str()
        postId = _is.readString()
        _request = IPostOper_Viewuserpost_Request(_connId, _msgId, self)
        self.viewUserPost(deviceCode, postId, _request)

    def _getMyUserByDateThreshold(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        thresholdDate = datetime.datetime.now()
        thresholdDate = _is.readDate()
        imgFormat = str()
        imgFormat = _is.readString()
        _request = IPostOper_Getmyuserbydatethreshold_Request(_connId, _msgId, self)
        self.getMyUserByDateThreshold(sessionKey, thresholdDate, imgFormat, _request)

    def _deleteUserPost(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        postId = str()
        postId = _is.readString()
        _request = IPostOper_Deleteuserpost_Request(_connId, _msgId, self)
        self.deleteUserPost(sessionKey, postId, _request)


    @abc.abstractmethod
    def getSysHints(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.ipostoper.IPostOper_Getsyshints_Request
        """
        pass

    @abc.abstractmethod
    def getPostCommentsHints(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.ipostoper.IPostOper_Getpostcommentshints_Request
        """
        pass

    @abc.abstractmethod
    def getFansByPageIndex(self, sessionKey, pageIndex, _request):
        """
        :type sessionKey: str
        :type pageIndex: int
        :type _request: message.gate.ipostoper.IPostOper_Getfansbypageindex_Request
        """
        pass

    @abc.abstractmethod
    def getAllMyFocuses(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.ipostoper.IPostOper_Getallmyfocuses_Request
        """
        pass

    @abc.abstractmethod
    def getNewFanList(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.ipostoper.IPostOper_Getnewfanlist_Request
        """
        pass

    @abc.abstractmethod
    def followAUser(self, sessionKey, userId, _request):
        """
        :type sessionKey: str
        :type userId: str
        :type _request: message.gate.ipostoper.IPostOper_Followauser_Request
        """
        pass

    @abc.abstractmethod
    def unfollowAUser(self, sessionKey, userId, _request):
        """
        :type sessionKey: str
        :type userId: str
        :type _request: message.gate.ipostoper.IPostOper_Unfollowauser_Request
        """
        pass

    @abc.abstractmethod
    def getLatestSysTopics(self, deviceCode, tagId, latestTopicDt, targetNum, imgFormat, _request):
        """
        :type deviceCode: str
        :type tagId: str
        :type latestTopicDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getlatestsystopics_Request
        """
        pass

    @abc.abstractmethod
    def getFormerSysTopics(self, deviceCode, tagId, oldestTopicDt, targetNum, imgFormat, _request):
        """
        :type deviceCode: str
        :type tagId: str
        :type oldestTopicDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getformersystopics_Request
        """
        pass

    @abc.abstractmethod
    def getSysTopicComments(self, deviceCode, topicId, interactiveType, latestCommentDt, targetNum, _request):
        """
        :type deviceCode: str
        :type topicId: str
        :type interactiveType: int
        :type latestCommentDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.ipostoper.IPostOper_Getsystopiccomments_Request
        """
        pass

    @abc.abstractmethod
    def getSysTopicByTopicId(self, deviceCode, topicId, imgFormat, _request):
        """
        :type deviceCode: str
        :type topicId: str
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getsystopicbytopicid_Request
        """
        pass

    @abc.abstractmethod
    def upvoteSysTopic(self, sessionKey, topicId, _request):
        """
        :type sessionKey: str
        :type topicId: str
        :type _request: message.gate.ipostoper.IPostOper_Upvotesystopic_Request
        """
        pass

    @abc.abstractmethod
    def unupvoteSysTopic(self, sessionKey, topicId, _request):
        """
        :type sessionKey: str
        :type topicId: str
        :type _request: message.gate.ipostoper.IPostOper_Unupvotesystopic_Request
        """
        pass

    @abc.abstractmethod
    def shareSysTopic(self, sessionKey, topicId, shareType, _request):
        """
        :type sessionKey: str
        :type topicId: str
        :type shareType: int
        :type _request: message.gate.ipostoper.IPostOper_Sharesystopic_Request
        """
        pass

    @abc.abstractmethod
    def commentSysTopic(self, sessionKey, topicId, comments, _request):
        """
        :type sessionKey: str
        :type topicId: str
        :type comments: str
        :type _request: message.gate.ipostoper.IPostOper_Commentsystopic_Request
        """
        pass

    @abc.abstractmethod
    def replySysTopicComment(self, sessionKey, topicId, dstCommentId, mentionedUserId, comments, _request):
        """
        :type sessionKey: str
        :type topicId: str
        :type dstCommentId: str
        :type mentionedUserId: str
        :type comments: str
        :type _request: message.gate.ipostoper.IPostOper_Replysystopiccomment_Request
        """
        pass

    @abc.abstractmethod
    def querySysTopicUpvoteStatus(self, sessionKey, sysTopicIdList, _request):
        """
        :type sessionKey: str
        :type sysTopicIdList: list[str]
        :type _request: message.gate.ipostoper.IPostOper_Querysystopicupvotestatus_Request
        """
        pass

    @abc.abstractmethod
    def viewSysTopic(self, deviceCode, sysTopicId, _request):
        """
        :type deviceCode: str
        :type sysTopicId: str
        :type _request: message.gate.ipostoper.IPostOper_Viewsystopic_Request
        """
        pass

    @abc.abstractmethod
    def getLatestUserPosts(self, deviceCode, tag, latestPostDt, targetNum, imgFormat, _request):
        """
        :type deviceCode: str
        :type tag: str
        :type latestPostDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getlatestuserposts_Request
        """
        pass

    @abc.abstractmethod
    def getFormerUserPosts(self, deviceCode, tag, oldestPostDt, targetNum, imgFormat, _request):
        """
        :type deviceCode: str
        :type tag: str
        :type oldestPostDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getformeruserposts_Request
        """
        pass

    @abc.abstractmethod
    def getUserPostByPostId(self, deviceCode, postId, imgFormat, _request):
        """
        :type deviceCode: str
        :type postId: str
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getuserpostbypostid_Request
        """
        pass

    @abc.abstractmethod
    def getUserPostComments(self, deviceCode, postId, latestCommentDt, targetNum, _request):
        """
        :type deviceCode: str
        :type postId: str
        :type latestCommentDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.ipostoper.IPostOper_Getuserpostcomments_Request
        """
        pass

    @abc.abstractmethod
    def commitUserPost(self, sessionKey, title, content, tags, imageNum, _request):
        """
        :type sessionKey: str
        :type title: str
        :type content: str
        :type tags: list[str]
        :type imageNum: int
        :type _request: message.gate.ipostoper.IPostOper_Commituserpost_Request
        """
        pass

    @abc.abstractmethod
    def didImageUpload(self, sessionKey, imageKeys, _request):
        """
        :type sessionKey: str
        :type imageKeys: list[str]
        :type _request: message.gate.ipostoper.IPostOper_Didimageupload_Request
        """
        pass

    @abc.abstractmethod
    def getImageUploadTokens(self, sessionKey, imgNum, _request):
        """
        :type sessionKey: str
        :type imgNum: int
        :type _request: message.gate.ipostoper.IPostOper_Getimageuploadtokens_Request
        """
        pass

    @abc.abstractmethod
    def getImageDownloadTokens(self, sessionKey, imgKey, imgFormat, _request):
        """
        :type sessionKey: str
        :type imgKey: str
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getimagedownloadtokens_Request
        """
        pass

    @abc.abstractmethod
    def upvoteUserPost(self, sessionKey, postId, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type _request: message.gate.ipostoper.IPostOper_Upvoteuserpost_Request
        """
        pass

    @abc.abstractmethod
    def unupvoteUserPost(self, sessionKey, postId, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type _request: message.gate.ipostoper.IPostOper_Unupvoteuserpost_Request
        """
        pass

    @abc.abstractmethod
    def shareUserPost(self, sessionKey, postId, shareType, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type shareType: int
        :type _request: message.gate.ipostoper.IPostOper_Shareuserpost_Request
        """
        pass

    @abc.abstractmethod
    def commentUserPost(self, sessionKey, postId, comments, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type comments: str
        :type _request: message.gate.ipostoper.IPostOper_Commentuserpost_Request
        """
        pass

    @abc.abstractmethod
    def replyUserPostComment(self, sessionKey, postId, dstCommentId, mentionedUserId, comments, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type dstCommentId: str
        :type mentionedUserId: str
        :type comments: str
        :type _request: message.gate.ipostoper.IPostOper_Replyuserpostcomment_Request
        """
        pass

    @abc.abstractmethod
    def queryUserPostUpvoteStatus(self, sessionKey, postIdList, _request):
        """
        :type sessionKey: str
        :type postIdList: list[str]
        :type _request: message.gate.ipostoper.IPostOper_Queryuserpostupvotestatus_Request
        """
        pass

    @abc.abstractmethod
    def viewUserPost(self, deviceCode, postId, _request):
        """
        :type deviceCode: str
        :type postId: str
        :type _request: message.gate.ipostoper.IPostOper_Viewuserpost_Request
        """
        pass

    @abc.abstractmethod
    def getMyUserByDateThreshold(self, sessionKey, thresholdDate, imgFormat, _request):
        """
        :type sessionKey: str
        :type thresholdDate: datetime.datetime
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getmyuserbydatethreshold_Request
        """
        pass

    @abc.abstractmethod
    def deleteUserPost(self, sessionKey, postId, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type _request: message.gate.ipostoper.IPostOper_Deleteuserpost_Request
        """
        pass

# message.gate.ipostoper.IPostOperProxy
class IPostOperProxy(RmiProxy):
    def __init__(self, name='IPostOper'):
        super().__init__(name)

    def getSysHints(self, _response, sessionKey):
        """
        :type _response: IPostOper_Getsyshints_Response
        :type sessionKey: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getSysHints')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        self.invoke(_os, _response)

    def getPostCommentsHints(self, _response, sessionKey):
        """
        :type _response: IPostOper_Getpostcommentshints_Response
        :type sessionKey: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getPostCommentsHints')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        self.invoke(_os, _response)

    def getFansByPageIndex(self, _response, sessionKey, pageIndex):
        """
        :type _response: IPostOper_Getfansbypageindex_Response
        :type sessionKey: str
        :type pageIndex: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getFansByPageIndex')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeInt(pageIndex)
        self.invoke(_os, _response)

    def getAllMyFocuses(self, _response, sessionKey):
        """
        :type _response: IPostOper_Getallmyfocuses_Response
        :type sessionKey: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getAllMyFocuses')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        self.invoke(_os, _response)

    def getNewFanList(self, _response, sessionKey):
        """
        :type _response: IPostOper_Getnewfanlist_Response
        :type sessionKey: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getNewFanList')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        self.invoke(_os, _response)

    def followAUser(self, _response, sessionKey, userId):
        """
        :type _response: IPostOper_Followauser_Response
        :type sessionKey: str
        :type userId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('followAUser')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(userId)
        self.invoke(_os, _response)

    def unfollowAUser(self, _response, sessionKey, userId):
        """
        :type _response: IPostOper_Unfollowauser_Response
        :type sessionKey: str
        :type userId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('unfollowAUser')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(userId)
        self.invoke(_os, _response)

    def getLatestSysTopics(self, _response, deviceCode, tagId, latestTopicDt, targetNum, imgFormat):
        """
        :type _response: IPostOper_Getlatestsystopics_Response
        :type deviceCode: str
        :type tagId: str
        :type latestTopicDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getLatestSysTopics')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(tagId)
        _os.writeDate(latestTopicDt)
        _os.writeInt(targetNum)
        _os.writeString(imgFormat)
        self.invoke(_os, _response)

    def getFormerSysTopics(self, _response, deviceCode, tagId, oldestTopicDt, targetNum, imgFormat):
        """
        :type _response: IPostOper_Getformersystopics_Response
        :type deviceCode: str
        :type tagId: str
        :type oldestTopicDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getFormerSysTopics')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(tagId)
        _os.writeDate(oldestTopicDt)
        _os.writeInt(targetNum)
        _os.writeString(imgFormat)
        self.invoke(_os, _response)

    def getSysTopicComments(self, _response, deviceCode, topicId, interactiveType, latestCommentDt, targetNum):
        """
        :type _response: IPostOper_Getsystopiccomments_Response
        :type deviceCode: str
        :type topicId: str
        :type interactiveType: int
        :type latestCommentDt: datetime.datetime
        :type targetNum: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getSysTopicComments')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(topicId)
        _os.writeInt(interactiveType)
        _os.writeDate(latestCommentDt)
        _os.writeInt(targetNum)
        self.invoke(_os, _response)

    def getSysTopicByTopicId(self, _response, deviceCode, topicId, imgFormat):
        """
        :type _response: IPostOper_Getsystopicbytopicid_Response
        :type deviceCode: str
        :type topicId: str
        :type imgFormat: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getSysTopicByTopicId')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(topicId)
        _os.writeString(imgFormat)
        self.invoke(_os, _response)

    def upvoteSysTopic(self, _response, sessionKey, topicId):
        """
        :type _response: IPostOper_Upvotesystopic_Response
        :type sessionKey: str
        :type topicId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('upvoteSysTopic')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(topicId)
        self.invoke(_os, _response)

    def unupvoteSysTopic(self, _response, sessionKey, topicId):
        """
        :type _response: IPostOper_Unupvotesystopic_Response
        :type sessionKey: str
        :type topicId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('unupvoteSysTopic')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(topicId)
        self.invoke(_os, _response)

    def shareSysTopic(self, _response, sessionKey, topicId, shareType):
        """
        :type _response: IPostOper_Sharesystopic_Response
        :type sessionKey: str
        :type topicId: str
        :type shareType: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('shareSysTopic')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(topicId)
        _os.writeInt(shareType)
        self.invoke(_os, _response)

    def commentSysTopic(self, _response, sessionKey, topicId, comments):
        """
        :type _response: IPostOper_Commentsystopic_Response
        :type sessionKey: str
        :type topicId: str
        :type comments: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('commentSysTopic')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(topicId)
        _os.writeString(comments)
        self.invoke(_os, _response)

    def replySysTopicComment(self, _response, sessionKey, topicId, dstCommentId, mentionedUserId, comments):
        """
        :type _response: IPostOper_Replysystopiccomment_Response
        :type sessionKey: str
        :type topicId: str
        :type dstCommentId: str
        :type mentionedUserId: str
        :type comments: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('replySysTopicComment')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(topicId)
        _os.writeString(dstCommentId)
        _os.writeString(mentionedUserId)
        _os.writeString(comments)
        self.invoke(_os, _response)

    def querySysTopicUpvoteStatus(self, _response, sessionKey, sysTopicIdList):
        """
        :type _response: IPostOper_Querysystopicupvotestatus_Response
        :type sessionKey: str
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

        _os.writeString(sessionKey)
        sysTopicIdList._write(_os)
        self.invoke(_os, _response)

    def viewSysTopic(self, _response, deviceCode, sysTopicId):
        """
        :type _response: IPostOper_Viewsystopic_Response
        :type deviceCode: str
        :type sysTopicId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('viewSysTopic')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(sysTopicId)
        self.invoke(_os, _response)

    def getLatestUserPosts(self, _response, deviceCode, tag, latestPostDt, targetNum, imgFormat):
        """
        :type _response: IPostOper_Getlatestuserposts_Response
        :type deviceCode: str
        :type tag: str
        :type latestPostDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getLatestUserPosts')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(tag)
        _os.writeDate(latestPostDt)
        _os.writeInt(targetNum)
        _os.writeString(imgFormat)
        self.invoke(_os, _response)

    def getFormerUserPosts(self, _response, deviceCode, tag, oldestPostDt, targetNum, imgFormat):
        """
        :type _response: IPostOper_Getformeruserposts_Response
        :type deviceCode: str
        :type tag: str
        :type oldestPostDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getFormerUserPosts')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(tag)
        _os.writeDate(oldestPostDt)
        _os.writeInt(targetNum)
        _os.writeString(imgFormat)
        self.invoke(_os, _response)

    def getUserPostByPostId(self, _response, deviceCode, postId, imgFormat):
        """
        :type _response: IPostOper_Getuserpostbypostid_Response
        :type deviceCode: str
        :type postId: str
        :type imgFormat: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getUserPostByPostId')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(postId)
        _os.writeString(imgFormat)
        self.invoke(_os, _response)

    def getUserPostComments(self, _response, deviceCode, postId, latestCommentDt, targetNum):
        """
        :type _response: IPostOper_Getuserpostcomments_Response
        :type deviceCode: str
        :type postId: str
        :type latestCommentDt: datetime.datetime
        :type targetNum: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getUserPostComments')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(postId)
        _os.writeDate(latestCommentDt)
        _os.writeInt(targetNum)
        self.invoke(_os, _response)

    def commitUserPost(self, _response, sessionKey, title, content, tags, imageNum):
        """
        :type _response: IPostOper_Commituserpost_Response
        :type sessionKey: str
        :type title: str
        :type content: str
        :type tags: list[str]
        :type imageNum: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('commitUserPost')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(title)
        _os.writeString(content)
        tags._write(_os)
        _os.writeInt(imageNum)
        self.invoke(_os, _response)

    def didImageUpload(self, _response, sessionKey, imageKeys):
        """
        :type _response: IPostOper_Didimageupload_Response
        :type sessionKey: str
        :type imageKeys: list[str]
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('didImageUpload')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        imageKeys._write(_os)
        self.invoke(_os, _response)

    def getImageUploadTokens(self, _response, sessionKey, imgNum):
        """
        :type _response: IPostOper_Getimageuploadtokens_Response
        :type sessionKey: str
        :type imgNum: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getImageUploadTokens')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeInt(imgNum)
        self.invoke(_os, _response)

    def getImageDownloadTokens(self, _response, sessionKey, imgKey, imgFormat):
        """
        :type _response: IPostOper_Getimagedownloadtokens_Response
        :type sessionKey: str
        :type imgKey: str
        :type imgFormat: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getImageDownloadTokens')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(imgKey)
        _os.writeString(imgFormat)
        self.invoke(_os, _response)

    def upvoteUserPost(self, _response, sessionKey, postId):
        """
        :type _response: IPostOper_Upvoteuserpost_Response
        :type sessionKey: str
        :type postId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('upvoteUserPost')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(postId)
        self.invoke(_os, _response)

    def unupvoteUserPost(self, _response, sessionKey, postId):
        """
        :type _response: IPostOper_Unupvoteuserpost_Response
        :type sessionKey: str
        :type postId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('unupvoteUserPost')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(postId)
        self.invoke(_os, _response)

    def shareUserPost(self, _response, sessionKey, postId, shareType):
        """
        :type _response: IPostOper_Shareuserpost_Response
        :type sessionKey: str
        :type postId: str
        :type shareType: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('shareUserPost')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(postId)
        _os.writeInt(shareType)
        self.invoke(_os, _response)

    def commentUserPost(self, _response, sessionKey, postId, comments):
        """
        :type _response: IPostOper_Commentuserpost_Response
        :type sessionKey: str
        :type postId: str
        :type comments: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('commentUserPost')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(postId)
        _os.writeString(comments)
        self.invoke(_os, _response)

    def replyUserPostComment(self, _response, sessionKey, postId, dstCommentId, mentionedUserId, comments):
        """
        :type _response: IPostOper_Replyuserpostcomment_Response
        :type sessionKey: str
        :type postId: str
        :type dstCommentId: str
        :type mentionedUserId: str
        :type comments: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('replyUserPostComment')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(postId)
        _os.writeString(dstCommentId)
        _os.writeString(mentionedUserId)
        _os.writeString(comments)
        self.invoke(_os, _response)

    def queryUserPostUpvoteStatus(self, _response, sessionKey, postIdList):
        """
        :type _response: IPostOper_Queryuserpostupvotestatus_Response
        :type sessionKey: str
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

        _os.writeString(sessionKey)
        postIdList._write(_os)
        self.invoke(_os, _response)

    def viewUserPost(self, _response, deviceCode, postId):
        """
        :type _response: IPostOper_Viewuserpost_Response
        :type deviceCode: str
        :type postId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('viewUserPost')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(postId)
        self.invoke(_os, _response)

    def getMyUserByDateThreshold(self, _response, sessionKey, thresholdDate, imgFormat):
        """
        :type _response: IPostOper_Getmyuserbydatethreshold_Response
        :type sessionKey: str
        :type thresholdDate: datetime.datetime
        :type imgFormat: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getMyUserByDateThreshold')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeDate(thresholdDate)
        _os.writeString(imgFormat)
        self.invoke(_os, _response)

    def deleteUserPost(self, _response, sessionKey, postId):
        """
        :type _response: IPostOper_Deleteuserpost_Response
        :type sessionKey: str
        :type postId: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('deleteUserPost')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(postId)
        self.invoke(_os, _response)


