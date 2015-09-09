"""
@author: mahanzhou
@date: 8/6/15
@file: 
@desc:

"""

from gamit.log.logger import Logger
from gamit.timer.timerbase import TimerBase
from gamit.timer.schedule import Scheduler
from gamit.utils.myuuid import MyUuid
from helpers.dbcachehelper import DbCacheHelper
from helpers.dbloghelper import DbLogHepler
from resources.posthelper import PostHelper
from resources.systopichelper import SysTopicHelper
from staticdata.manager.ErrorCodeManager import ErrorCodeManager
from user.userentitymanager import UserEntityManager

from resources.systopicmanager import SysTopicManager
from resources.postmanager import PostManager
from message.gate.gatemsg import SMyFan, SeqMyFan
from message.gate.gatemsg import SMyFocus, SeqMyFocus
from message.logdb.logconst import ELogPostOperType
from message.db.mongodb.usertables import TUserFan
from message.db.itablesaver import ITableSaver_Loadsystopics_Response
from message.db.itablesaver import ITableSaver_Loaduserposts_Response
from message.db.itablesaver import ITableSaver_Loaduserpostcomments_Response
from message.db.itablesaver import ITableSaver_Getfansbyuseridandpageindex_Response
from message.db.itablesaver import ITableSaver_Getfocususeidlist_Response
from message.db.itablesaver import ITableSaver_Hasfollowed_Response
from message.db.itablesaver import ITableSaver_Loadsystopiccomments_Response
from message.db.itablesaver import ITableSaver_Unfollow_Response
from message.db.itablesaver import ITableSaver_Queryuserpostupvotestatus_Response
from message.db.itablesaver import ITableSaver_Querysystopicupvotestatus_Response
from message.db.itablesaver import ITableSaver_Removeuserpostupvote_Response
from message.db.itablesaver import ITableSaver_Removesystopicupvote_Response

class ITableSaverLoadSysTopicsResponse(ITableSaver_Loadsystopics_Response, TimerBase):
    def __init__(self, numPerPage):
        ITableSaver_Loadsystopics_Response.__init__(self)
        TimerBase.__init__(self)

        self.numPerPage = numPerPage
        self.pageIndex = 0

    def onResponse(self, topicList):
        Logger.log("ITableSaverLoadSysTopicsResponse.onResponse: topics loaded: ",
                   len(topicList), ", index:", self.pageIndex)
        SysTopicManager.addSysTopics(topicList, True)

        if len(topicList) < self.numPerPage:
            return

        if SysTopicManager.isCacheFull():
            return

        self.pageIndex += 1
        DbCacheHelper.getTableSaverProxy().loadSysTopics(self, self.pageIndex, self.numPerPage)

    def onError(self, what, code):
        Logger.log("ITableSaverLoadSysTopicsResponse.onError:", what, ", code:", code)

    def onTimeout(self):
        Logger.log("ITableSaverLoadSysTopicsResponse.onTimeout.")
        Scheduler.schedule(self, None, 10, 0)

    def handleTimeout(self, data):
        Logger.log("ITableSaverLoadSysTopicsResponse.handleTimeout: try again:", self.pageIndex)
        DbCacheHelper.getTableSaverProxy().loadSysTopics(self, self.pageIndex, self.numPerPage)

class ITableSaverLoadsystopiccommentsResponse(ITableSaver_Loadsystopiccomments_Response):
    """
    :type wSysTopic: resources.systopic.WSysTopic
    :type clientRequest: message.gate.ipostoper.IPostOper_Getsystopiccomments_Request
    """
    def __init__(self, clientRequest, wSysTopic, thresDt, targetNum, interactiveType):
        super().__init__()
        self.wSysTopic = wSysTopic
        self.clientRequest = clientRequest
        self.thresDt = thresDt
        self.targetNum = targetNum
        self.interactiveType = interactiveType

    def onResponse(self, comments):
        """
        :type comments: list[message.db.mongodb.posttables.TSysTopicComment]
        """

        self.wSysTopic.setLoadingCommentStatus(False)

        self.wSysTopic.appendComments(comments)
        res = self.wSysTopic.getComments(self.thresDt, self.targetNum, self.interactiveType)
        self.clientRequest.response(res)

    def onError(self, what, code):
        self.wSysTopic.setLoadingCommentStatus(False)

        self.clientRequest.error(what, code)

    def onTimeout(self):
        self.wSysTopic.setLoadingCommentStatus(False)

        self.clientRequest.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))

class PreloadSysTopicCommentsResponse(ITableSaver_Loadsystopiccomments_Response):
    """
    :type wSysTopic: resources.systopic.WSysTopic
    """
    def __init__(self, clientRequest, userEntity,
                 wSysTopic, interactiveType, content="", mentioneds=[], returnWithCommentId=False):
        super().__init__()

        self.clientRequest = clientRequest
        self.userEntity = userEntity
        self.wSysTopic = wSysTopic
        self.interactiveType = interactiveType
        self.content = content
        self.mentioneds = mentioneds
        self.returnWithCommentId = returnWithCommentId
        
    def onResponse(self, comments):
        self.wSysTopic.setLoadingCommentStatus(False)

        self.wSysTopic.appendComments(comments)

        commentId = SysTopicHelper.addNewCommentToSysTopic(
            self.userEntity, self.wSysTopic, self.interactiveType, self.content, self.mentioneds)

        if self.returnWithCommentId:
            self.clientRequest.response(commentId)
        else:
            self.clientRequest.response()
        
    def onError(self, what, code):
        self.wSysTopic.setLoadingCommentStatus(False)

        self.clientRequest.error(what, code)
    
    def onTimeout(self):
        self.wSysTopic.setLoadingCommentStatus(False)

        self.clientRequest.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))

class ITableSaverLoaduserpostsResponse(ITableSaver_Loaduserposts_Response, TimerBase):
    def __init__(self, numPerPage):
        ITableSaver_Loaduserposts_Response.__init__(self)
        TimerBase.__init__(self)

        self.numberPerPage = numPerPage
        self.pageIndex = 0

    def onResponse(self, postList):
        Logger.log("ITableSaverLoaduserpostsResponse.onResponse: posts loaded: ",
                   len(postList), ", index:", self.pageIndex)
        PostManager.addPosts(postList)

        if len(postList) < self.numberPerPage:
            return

        if PostManager.isCacheFull():
            return

        self.pageIndex += 1
        DbCacheHelper.getTableSaverProxy().loadUserPosts(self, self.pageIndex, self.numberPerPage)

    def onError(self, what, code):
        Logger.log("ITableSaverLoaduserpostsResponse.onError:", what, ", code:", code)

    def onTimeout(self):
        Logger.log("ITableSaverLoaduserpostsResponse.onTimeout")
        Scheduler.schedule(self, None, 10, 0)

    def handleTimeout(self, data):
        Logger.log("ITableSaverLoaduserpostsResponse.handleTimeout: try again:", self.pageIndex)
        DbCacheHelper.getTableSaverProxy().loadUserPosts(self, self.pageIndex, self.numberPerPage)

class ITableSaverLoaduserpostcommentsResponse(ITableSaver_Loaduserpostcomments_Response):
    """
    :type wUserPost: resources.post.WUserPost
    :type clientResponse: message.gate.ipostoper.IPostOper_Getuserpostcomments_Request
    """
    def __init__(self, clientResponse, wUserPost, thresDt, targetNum):
        super().__init__()
        self.clientResponse = clientResponse
        self.wUserPost = wUserPost
        self.thresDt = thresDt
        self.targetNum = targetNum

    def onResponse(self, comments):
        """
        :type comments: list[message.db.mongodb.posttables.TUserPostComment]
        """
        self.wUserPost.setLoadingCommentStatus(False)

        self.wUserPost.appendComments(comments)
        data = self.wUserPost.getComments(self.thresDt, self.targetNum)
        self.clientResponse.response(data)

    def onError(self, what, code):
        self.wUserPost.setLoadingCommentStatus(False)

        self.clientResponse.error(what, code)

    def onTimeout(self):
        self.wUserPost.setLoadingCommentStatus(False)

        self.clientResponse.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))

class IPreLoadUserPostCommentsResponse(ITableSaver_Loaduserpostcomments_Response):
    """
    :type userEntity: user.userentity.UserEntity
    :type wuPost: resources.post.WUserPost
    :type clientResponse: message.gate.ipostoper.IPostOper_Upvoteuserpost_Request
    """
    def __init__(self, clientResponse, userEntity,
                 wuPost, interactiveType, content="", mentioneds=[], returnWithCommentId=False):
        super().__init__()

        self.clientResponse = clientResponse
        self.userEntity = userEntity
        self.wuPost = wuPost
        self.interactiveType = interactiveType
        self.content = content
        self.mentioneds = mentioneds
        self.returnWithCommentId = returnWithCommentId

    def onResponse(self, comments):
        """
        :type comments: list[message.db.mongodb.posttables.TUserPostComment]
        """
        self.wUserPost.setLoadingCommentStatus(False)

        self.wuPost.appendComments(comments)

        commentId = PostHelper.addNewCommentToUserPost(self.userEntity,
            self.wuPost, self.interactiveType, self.content, self.mentioneds)

        if self.returnWithCommentId:
            self.clientResponse.response(commentId)
        else:
            self.clientResponse.response()

    def onError(self, what, code):
        self.wUserPost.setLoadingCommentStatus(False)

        self.clientResponse.error(what, code)

    def onTimeout(self):
        self.wUserPost.setLoadingCommentStatus(False)

        self.clientResponse.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))

class ITableSaverGetFansByuseridAndPageIndexResponse(ITableSaver_Getfansbyuseridandpageindex_Response):
    def __init__(self, clientRequest):
        super().__init__()
        self.clientRequest = clientRequest

    def onResponse(self, fanList):
        """
        :type fanList: list[message.db.mongodb.usertables.TUserFan]
        """

        sFanList = SeqMyFan()
        for tFan in fanList:
            userEntity = UserEntityManager.findUserEntityByUserId(tFan.fanUserId)
            if not userEntity:
                Logger.log("ITableSaverGetFansByuseridAndPageIndexResponse.onResposne",
                           "UserNotFound:", tFan.fanUserId)
                continue

            sFan = SMyFan()
            sFan.fanInfo = userEntity.getUserBriefInfo()
            sFan.operDt = tFan.createDt

            sFanList.append(sFan)

        self.clientRequest.response(sFanList)

    def onError(self, what, code):
        self.clientRequest.error(what, code)

    def onTimeout(self):
        self.clientResponse.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))

class ITableSaverGetfocususeidlistResponse(ITableSaver_Getfocususeidlist_Response):
    def __init__(self, clientRequest):
        super().__init__()
        self.clientRequest = clientRequest

    def onResponse(self, fanList):
        """
        :type fanList: list[message.db.mongodb.usertables.TUserFan]
        """
        sFocusList = SeqMyFocus()

        for tFan in fanList:
            userEntity = UserEntityManager.findUserEntityByUserId(tFan.myUserId)
            if not userEntity:
                Logger.log("ITableSaverGetFansByuseridAndPageIndexResponse.onResposne",
                           "UserNotFound:", tFan.myUserId)
                continue

            sFocus = SMyFocus()
            sFocus.userInfo = userEntity.getUserBriefInfo()
            sFocus.operDt = tFan.createDt

            sFocusList.append(sFocus)

        self.clientRequest.response(sFocusList)

    def onError(self, what, code):
        self.clientRequest.error(what, code)

    def onTimeout(self):
        self.clientResponse.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))

class ITableSaverHasfollowedResponse(ITableSaver_Hasfollowed_Response):
    """
    :type myUserEntity: user.userentity.UserEntity
    :type focusUserEntity: user.userentity.UserEntity
    """
    def __init__(self, clientRequest, myUserEntity, focusUserEntity):
        super().__init__()
        self.clientRequest = clientRequest
        self.myUserEntity = myUserEntity
        self.focusUserEntity = focusUserEntity

    def onResponse(self, hasFollowed):
        if hasFollowed:
            self.clientRequest.error(ErrorCodeManager.getError("ErrorGate_hasFollowedThisUser"))
            return

        tFan = TUserFan()
        tFan.recordId = MyUuid.getUuid()
        tFan.fanUserId = self.myUserEntity.getUserId()
        tFan.myUserId = self.focusUserEntity.getUserId()
        DbCacheHelper.getITableSaverProxy().updateFanInfo(None, tFan)

        sNewFocus = SMyFocus()
        sNewFocus.userInfo = self.focusUserEntity.getUserBriefInfo()
        sNewFocus.operDt = tFan.createDt
        self.clientRequest.response(sNewFocus)

        sNewFan = SMyFan()
        sNewFan.fanInfo = self.myUserEntity.getUserBriefInfo()
        sNewFan.operDt = tFan.createDt
        self.focusUserEntity.addNewFan(sNewFan)

        self.myUserEntity.getTUserProperty().focusNum += 1
        self.focusUserEntity.getTUserProperty().fanNum += 1
        DbCacheHelper.getITableSaverProxy().updateTUserProperty(None, self.myUserEntity.getTUserProperty())
        DbCacheHelper.getITableSaverProxy().updateTUserProperty(None, self.focusUserEntity.getTUserProperty())

    def onError(self, what, code):
        self.clientRequest.error(what, code)

    def onTimeout(self):
        self.clientRequest.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))


class UnfollowAUserDbResponse(ITableSaver_Unfollow_Response):
    """
    :type clientRequest: message.gate.ipostoper.IPostOper_Unfollowauser_Request
    :type myUserEntity: user.userentity.UserEntity
    :type hisUserEntity: user.userentity.UserEntity
    """
    def __init__(self, clientRequest, myUserEntity, hisUserEntity):
        super().__init__()
        self.clientRequest = clientRequest
        self.myUserEntity = myUserEntity
        self.hisUserEntity = hisUserEntity

    def onResponse(self):
        self.clientRequest.response()

        self.myUserEntity.getTUserProperty().focusNum -= 1
        self.hisUserEntity.getTUserProperty().fanNum -= 1

        DbCacheHelper.getITableSaverProxy().updateTUserProperty(None, self.myUserEntity.getTUserProperty())
        DbCacheHelper.getITableSaverProxy().updateTUserProperty(None, self.focusUserEntity.getTUserProperty())

    def onError(self, what, code):
        self.clientRequest.error(what, code)

    def onTimeout(self):
        self.clientRequest.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))

class QueryUserPostsUpvotedStatusResponse(ITableSaver_Queryuserpostupvotestatus_Response):
    def __init__(self, clientRequest, readyStatusDict):
        super().__init__()
        self.clientRequest = clientRequest
        self.readyStatusDict = readyStatusDict

    def onResponse(self, updvoteStatusDict):
        """
        :type updvoteStatusDict: dict[str, bool]
        """
        self.readyStatusDict.update(updvoteStatusDict)
        self.clientRequest.response(self.readyStatusDict)

    def onError(self, what, code):
        self.clientRequest.error(what, code)

    def onTimeout(self):
        self.clientRequest.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))

class QuerySysTopicUpvotedStatusResponse(ITableSaver_Querysystopicupvotestatus_Response):
    def __init__(self, clientRequest, readyStatusDict):
        super().__init__()
        self.clientRequest = clientRequest
        self.readyStatusDict = readyStatusDict

    def onResponse(self, sysTopicStatusDict):
        self.readyStatusDict.update(sysTopicStatusDict)
        self.clientRequest.response(self.readyStatusDict)

    def onError(self, what, code):
        self.clientRequest.error(what, code)

    def onTimeout(self):
        self.clientRequest.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))

class RemoveUserPostUpvoteResponse(ITableSaver_Removeuserpostupvote_Response):
    """
    :type wUserPost: resources.post.WUserPost
    :type clientRequest: message.gate.ipostoper.IPostOper_Unupvoteuserpost_Request
    :type userEntity: user.userentity.UserEntity
    """
    def __init__(self, clientRequest, wUserPost, userEntity):
        self.clientRequest = clientRequest
        self.wUserPost = wUserPost
        self.userEntity = userEntity

    def onResponse(self, commentId):
        self.wUserPost.removeUpvoteRecord(commentId, self.userEntity.getUserId())
        self.wUserPost.getTUserPost().upvotedTimes -= 1
        DbCacheHelper.getITableSaverProxy().updateTUserPost(None, self.wUserPost.getTUserPost())

        self.clientRequest.response()

        DbLogHepler.logUserPostOper(self.userEntity.getLogUserInfo(),
                                    self.wUserPost.getPostId(),
                                    ELogPostOperType.Unupvote)

    def onError(self, what, code):
        self.clientRequest.error(what, code)

    def onTimeout(self):
        self.clientRequest.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))

class RemoveSysTopicUpvoteResponse(ITableSaver_Removesystopicupvote_Response):
    """
    :type wSysTopic: resources.systopic.WSysTopic
    :type clientRequest: message.gate.ipostoper.IPostOper_Unupvotesystopic_Request
    :type userEntity: user.userentity.UserEntity
    """
    def __init__(self, clientRequest, wSysTopic, userEntity):
        self.clientRequest = clientRequest
        self.wSysTopic = wSysTopic
        self.userEntity = userEntity

    def onResponse(self, commentId):
        self.wSysTopic.removeUpvoteRecord(commentId, self.userEntity.getUserId())
        self.wSysTopic.getTSysTopic().upvotedTimes -= 1
        DbCacheHelper.getITableSaverProxy().updateTSysTopic(None, self.wSysTopic.getTSysTopic())

        self.clientRequest.response()
        DbLogHepler.logSysTopicOper(self.userEntity.getLogUserInfo(),
                                    self.wSysTopic.getTopicId(),
                                    ELogPostOperType.Unupvote)

    def onError(self, what, code):
        self.clientRequest.error(what, code)

    def onTimeout(self):
        self.clientRequest.error(ErrorCodeManager.getError("ErrorGate_operTimeout"))

class ResourceLoader:
    @classmethod
    def load(cls):
        cls.loadSysTopics()
        cls.loadUserPosts()

    @classmethod
    def loadSysTopics(cls):
        numPerPage = 2000
        dbCb = ITableSaverLoadSysTopicsResponse(numPerPage)
        DbCacheHelper.getTableSaverProxy().loadSysTopics(dbCb, 0, numPerPage)

    @classmethod
    def loadUserPosts(cls):
        numPerPage = 2000
        dbCb = ITableSaverLoaduserpostsResponse(numPerPage)
        DbCacheHelper.getTableSaverProxy().loadUserPosts(dbCb, 0, numPerPage)
