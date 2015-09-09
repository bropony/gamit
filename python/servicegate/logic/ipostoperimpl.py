"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:

"""
import traceback
from message.gate.ipostoper import IPostOperServant
from resources.postmanager import PostManager
from resources.post import WUserPost
from resources.systopicmanager import SysTopicManager
from helpers.dbloghelper import DbLogHepler
from helpers.dbcachehelper import DbCacheHelper
from helpers.imagehelper import ImageHelper
from user.userentitymanager import UserEntityManager
from resources.resourceloader import ITableSaverLoaduserpostcommentsResponse
from resources.resourceloader import IPreLoadUserPostCommentsResponse
from resources.resourceloader import ITableSaverGetFansByuseridAndPageIndexResponse
from resources.resourceloader import ITableSaverGetfocususeidlistResponse, ITableSaverHasfollowedResponse
from resources.resourceloader import ITableSaverLoadsystopiccommentsResponse
from resources.resourceloader import UnfollowAUserDbResponse
from resources.resourceloader import PreloadSysTopicCommentsResponse
from resources.resourceloader import QueryUserPostsUpvotedStatusResponse
from resources.resourceloader import QuerySysTopicUpvotedStatusResponse
from resources.resourceloader import RemoveUserPostUpvoteResponse
from resources.resourceloader import RemoveSysTopicUpvoteResponse
from resources.posthelper import PostHelper
from resources.systopichelper import SysTopicHelper

from gamit.utils.myuuid import MyUuid
from gamit.log.logger import Logger
from helpers.imagehelper import ImageHelper
from staticdata.manager.ErrorCodeManager import ErrorCodeManager

from message.common.publicdef import SeqString, EInteractiveType, DictStringBool
from message.logdb.logtables import SLogUserInfo
from message.logdb.logconst import ELogPostOperType
from message.db.mongodb.posttables import SeqTUserPost, TUserPost
from message.db.mongodb.posttables import SeqTSysTopic
from message.gate.gatemsg import SImageInfo, SeqImageInfo


class IPostOperImpl(IPostOperServant):
    def __init__(self):
        super().__init__()

    def getSysHints(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.ipostoper.IPostOper_Getsyshints_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        hints = userEntity.getAllHints()
        _request.response(hints)

    def getPostCommentsHints(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.ipostoper.IPostOper_Getpostcommentshints_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        hints = userEntity.getAllCommentHints()
        _request.response(hints)

    def getFansByPageIndex(self, sessionKey, pageIndex, _request):
        """
        :type sessionKey: str
        :type pageIndex: int
        :type _request: message.gate.ipostoper.IPostOper_Getfansbypageindex_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        dbCb = ITableSaverGetFansByuseridAndPageIndexResponse(_request)
        DbCacheHelper.getITableSaverProxy().getFansByUserIdAndPageIndex(dbCb, userEntity.getUserId(), pageIndex)

    def getAllMyFocuses(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.ipostoper.IPostOper_Getallmyfocuses_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        dbCb = ITableSaverGetfocususeidlistResponse(_request)
        DbCacheHelper.getITableSaverProxy().getFocusUseIdList(dbCb, userEntity.getUserId())

    def getNewFanList(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.ipostoper.IPostOper_Getnewfanlist_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        res = userEntity.getNewFans()
        _request.response(res)


    def followAUser(self, sessionKey, userId, _request):
        """
        :type sessionKey: str
        :type userId: str
        :type _request: message.gate.ipostoper.IPostOper_Followauser_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        hisEntity = UserEntityManager.findUserEntityByUserId(userId)
        if not hisEntity:
            ErrorCodeManager.raiseError("ErrorGate_noSuchUser")

        dbCb = ITableSaverHasfollowedResponse(_request, userEntity, hisEntity)
        DbCacheHelper.getITableSaverProxy().hasFollowed(dbCb, userEntity.getUserId(), userId)

    def unfollowAUser(self, sessionKey, userId, _request):
        """
        :type sessionKey: str
        :type userId: str
        :type _request: message.gate.ipostoper.IPostOper_Unfollowauser_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        hisEntity = UserEntityManager.findUserEntityByUserId(userId)
        if not hisEntity:
            ErrorCodeManager.raiseError("ErrorGate_noSuchUser")

        dbCb = UnfollowAUserDbResponse(_request, userEntity, hisEntity)
        DbCacheHelper.getITableSaverProxy().unfollow(dbCb, userEntity.getUserId(), userId)

    #
    # Sys Topic Opers begins here
    #

    def getLatestSysTopics(self, deviceCode, tag, latestTopicDt, targetNum, imgFormat, _request):
        """
        :type deviceCode: str
        :type tag: str
        :type latestTopicDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.ipostoper.IPostOper_Getlatestsystopics_Request
        """
        sysTopicList = SysTopicManager.getLatestTopic(tag, latestTopicDt, targetNum, imgFormat)
        _request.response(sysTopicList)

        # loggings
        userEntity = UserEntityManager.findUserEntityByDeviceCode(deviceCode)
        if userEntity:
            logUserInfo = userEntity.getLogUserInfo()
        else:
            logUserInfo = SLogUserInfo()
            logUserInfo.deviceCode = deviceCode

        tags = SeqString()
        tags.append(tag)
        DbLogHepler.logRefreshSysTopic(logUserInfo, tags)

    def getFormerSysTopics(self, deviceCode, tag, oldestTopicDt, targetNum, imgFormat, _request):
        """
        :type deviceCode: str
        :type tag: str
        :type oldestTopicDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.ipostoper.IPostOper_Getformersystopics_Request
        """
        sysTopicList = SysTopicManager.getOlderSysTopicInDateOrder(tag, oldestTopicDt, targetNum, imgFormat)
        _request.response(sysTopicList)

        # loggings
        userEntity = UserEntityManager.findUserEntityByDeviceCode(deviceCode)
        if userEntity:
            logUserInfo = userEntity.getLogUserInfo()
        else:
            logUserInfo = SLogUserInfo()
            logUserInfo.deviceCode = deviceCode

        tags = SeqString()
        tags.append(tag)
        DbLogHepler.logRefreshSysTopic(logUserInfo, tags)

    def getSysTopicComments(self, deviceCode, topicId, interactiveType, latestCommentDt, targetNum, _request):
        """
        :type deviceCode: str
        :type topicId: str
        :type interactiveType: int
        :type latestCommentDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.ipostoper.IPostOper_Getsystopiccomments_Request
        """

        sysTopic = SysTopicManager.getSysTopicByTopicId(topicId)
        if not sysTopic:
            ErrorCodeManager.raiseError("ErrorGate_noSuchSysTopic")

        if not sysTopic.isCommentLoaded():
            if sysTopic.isInLoadingCommentStatus():
                ErrorCodeManager.raiseError("ErrorGate_serverBusy")

            dbCb = ITableSaverLoadsystopiccommentsResponse(_request, sysTopic, latestCommentDt, targetNum, interactiveType)
            DbCacheHelper.getITableSaverProxy().loadSysTopicComments(dbCb, topicId)
            sysTopic.setLoadingCommentStatus(True)
        else:
            comments = sysTopic.getComments(latestCommentDt, targetNum, interactiveType)
            _request.response(comments)

    def getSysTopicByTopicId(self, deviceCode, topicId, imgFormat, _request):
        """
        :type deviceCode: str
        :type topicId: str
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getsystopicbytopicid_Request
        """
        sysTopic = SysTopicManager.getSysTopicByTopicId(topicId)
        if not sysTopic:
            ErrorCodeManager.raiseError("ErrorGate_noSuchSysTopic")

        _request.response(sysTopic.getClientInfo(imgFormat))

    def upvoteSysTopic(self, sessionKey, topicId, _request):
        """
        :type sessionKey: str
        :type topicId: str
        :type _request: message.gate.ipostoper.IPostOper_Upvotesystopic_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        wSysTopic = SysTopicManager.getSysTopicByTopicId(topicId)
        if not wSysTopic:
            ErrorCodeManager.raiseError("ErrorGate_noSuchSysTopic")

        if not wSysTopic.isCommentLoaded():
            if wSysTopic.isInLoadingCommentStatus():
                ErrorCodeManager.raiseError("ErrorGate_serverBusy")

            dbCb = PreloadSysTopicCommentsResponse(_request, userEntity, wSysTopic, EInteractiveType.Upvote)
            DbCacheHelper.getITableSaverProxy().loadSysTopicComments(dbCb, topicId)

            wSysTopic.setLoadingCommentStatus(True)
        else:
            SysTopicHelper.addNewCommentToSysTopic(userEntity, wSysTopic, EInteractiveType.Upvote)
            _request.response()

    def unupvoteSysTopic(self, sessionKey, topicId, _request):
        """
        :type sessionKey: str
        :type topicId: str
        :type _request: message.gate.ipostoper.IPostOper_Unupvotesystopic_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        wSysTopic = SysTopicManager.getSysTopicByTopicId(topicId)
        if not wSysTopic:
            ErrorCodeManager.raiseError("ErrorGate_noSuchSysTopic")

        dbCb = RemoveSysTopicUpvoteResponse(_request, wSysTopic, userEntity)
        DbCacheHelper.getITableSaverProxy().removeSysTopicUpvote(dbCb, topicId, userEntity.getUserId())

    def shareSysTopic(self, sessionKey, topicId, shareType, _request):
        """
        :type sessionKey: str
        :type topicId: str
        :type shareType: int
        :type _request: message.gate.ipostoper.IPostOper_Sharesystopic_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        wSysTopic = SysTopicManager.getSysTopicByTopicId(topicId)
        if not wSysTopic:
            ErrorCodeManager.raiseError("ErrorGate_noSuchSysTopic")

        if not wSysTopic.isCommentLoaded():
            if wSysTopic.isInLoadingCommentStatus():
                ErrorCodeManager.raiseError("ErrorGate_serverBusy")

            dbCb = PreloadSysTopicCommentsResponse(_request, userEntity, wSysTopic, EInteractiveType.Shared)
            DbCacheHelper.getITableSaverProxy().loadSysTopicComments(dbCb, topicId)

            wSysTopic.setLoadingCommentStatus(True)
        else:
            SysTopicHelper.addNewCommentToSysTopic(userEntity, wSysTopic, EInteractiveType.Shared)
            _request.response()

    def commentSysTopic(self, sessionKey, topicId, comments, _request):
        """
        :type sessionKey: str
        :type topicId: str
        :type comments: str
        :type _request: message.gate.ipostoper.IPostOper_Commentsystopic_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        wSysTopic = SysTopicManager.getSysTopicByTopicId(topicId)
        if not wSysTopic:
            ErrorCodeManager.raiseError("ErrorGate_noSuchSysTopic")

        if not wSysTopic.isCommentLoaded():
            if wSysTopic.isInLoadingCommentStatus():
                ErrorCodeManager.raiseError("ErrorGate_serverBusy")

            dbCb = PreloadSysTopicCommentsResponse(
                _request, userEntity, wSysTopic, EInteractiveType.Comment, comments, [], True)
            DbCacheHelper.getITableSaverProxy().loadSysTopicComments(dbCb, topicId)

            wSysTopic.setLoadingCommentStatus(True)
        else:
            commentId = SysTopicHelper.addNewCommentToSysTopic(userEntity, wSysTopic, EInteractiveType.Comment, comments)
            _request.response(commentId)

    def replySysTopicComment(self, sessionKey, topicId, dstCommentId, mentionedUserId, comments, _request):
        """
        :type sessionKey: str
        :type topicId: str
        :type dstCommentId: str
        :type mentionedUserId: str
        :type comments: str
        :type _request: message.gate.ipostoper.IPostOper_Replysystopiccomment_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        wSysTopic = SysTopicManager.getSysTopicByTopicId(topicId)
        if not wSysTopic:
            ErrorCodeManager.raiseError("ErrorGate_noSuchSysTopic")

        mentionedEntity = UserEntityManager.findUserEntityByUserId(mentionedUserId)
        if not mentionedEntity:
            ErrorCodeManager.raiseError("ErrorGate_mentionedUserNotExisted")

        if not wSysTopic.hasComment(dstCommentId):
            ErrorCodeManager.raiseError("ErrorGate_dstCommentNotExisted")

        commentId = SysTopicHelper.addNewCommentToSysTopic(
            userEntity, wSysTopic, EInteractiveType.Comment, comments, [mentionedUserId])

        _request.response(commentId)

    def querySysTopicUpvoteStatus(self, sessionKey, sysTopicIdList, _request):
        """
        :type sessionKey: str
        :type sysTopicIdList: list[str]
        :type _request: message.gate.ipostoper.IPostOper_Querysystopicupvotestatus_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        readyStatusDict = DictStringBool()
        notReadSysTopicIdList = SeqString()
        for topicId in sysTopicIdList:
            wSysPost = SysTopicManager.getSysTopicByTopicId(topicId)
            if not wSysPost:
                readyStatusDict[topicId] = False
            elif not wSysPost.isCommentLoaded():
                notReadSysTopicIdList.append(topicId)
            else:
                if wSysPost.hasUpvoted(userEntity.getUserId()):
                    readyStatusDict[topicId] = True
                else:
                    readyStatusDict[topicId] = False

        if notReadSysTopicIdList:
            dbCb = QuerySysTopicUpvotedStatusResponse(_request, readyStatusDict)
            DbCacheHelper.getITableSaverProxy().querySysTopicUpvoteStatus(dbCb, userEntity.getUserId(), notReadSysTopicIdList)
        else:
            _request.response(readyStatusDict)

    def viewSysTopic(self, deviceCode, sysTopicId, _request):
        """
        :type deviceCode: str
        :type sysTopicId: str
        :type _request: message.gate.ipostoper.IPostOper_Viewsystopic_Request
        """

        wSysTopic = SysTopicManager.getSysTopicByTopicId(sysTopicId)
        if not wSysTopic:
            ErrorCodeManager.raiseError("ErrorGate_noSuchSysTopic")

        wSysTopic.getTSysTopic().viewTimes += 1
        _request.response(wSysTopic.getTSysTopic().viewTimes)

        DbCacheHelper.getITableSaverProxy().updateTSysTopic(None, wSysTopic.getTSysTopic())

        # logging
        userEntity = UserEntityManager.findUserEntityByDeviceCode(deviceCode)
        if userEntity:
            DbLogHepler.logSysTopicOper(userEntity.getLogUserInfo(), wSysTopic.getTopicId(), ELogPostOperType.View)
        else:
            logUserInfo = SLogUserInfo()
            logUserInfo.deviceCode = deviceCode
            DbLogHepler.logSysTopicOper(logUserInfo, wSysTopic.getTopicId(), ELogPostOperType.View)

    #
    # User Post Opers begins here
    #

    def getLatestUserPosts(self, deviceCode, tag, latestPostDt, targetNum, imgFormat, _request):
        """
        :type deviceCode: str
        :type tag: str
        :type latestPostDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getlatestuserposts_Request
        """
        postList = PostManager.getNewestPosts(tag, latestPostDt, targetNum, imgFormat)
        _request.response(postList)

        # loggings
        userEntity = UserEntityManager.findUserEntityByDeviceCode(deviceCode)
        if userEntity:
            logUserInfo = userEntity.getLogUserInfo()
        else:
            logUserInfo = SLogUserInfo()
            logUserInfo.deviceCode = deviceCode

        tags = SeqString()
        tags.append(tag)
        DbLogHepler.logRefreshUserPost(logUserInfo, tags)

    def getFormerUserPosts(self, deviceCode, tag, oldestPostDt, targetNum, imgFormat, _request):
        """
        :type deviceCode: str
        :type tag: str
        :type oldestPostDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getformeruserposts_Request
        """

        postList = PostManager.findPostsByInDtOrder(tag, oldestPostDt, targetNum, imgFormat)
        _request.response(postList)

        # loggings
        userEntity = UserEntityManager.findUserEntityByDeviceCode(deviceCode)
        if userEntity:
            logUserInfo = userEntity.getLogUserInfo()
        else:
            logUserInfo = SLogUserInfo()
            logUserInfo.deviceCode = deviceCode

        tags = SeqString()
        tags.append(tag)
        DbLogHepler.logRefreshUserPost(logUserInfo, tags)

    def getUserPostByPostId(self, deviceCode, postId, imgFormat, _request):
        """
        :type deviceCode: str
        :type postId: str
        :type _request: message.gate.ipostoper.IPostOper_Getuserpostbypostid_Request
        """
        wPost = PostManager.findPostByPostId(postId)
        if not wPost:
            ErrorCodeManager.raiseError("ErrorGate_noSuchPost")

        _request.response(wPost.getClientInfo(imgFormat))

    def getUserPostComments(self, deviceCode, postId, latestCommentDt, targetNum, _request):
        """
        :type deviceCode: str
        :type topicId: str
        :type latestCommentDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.ipostoper.IPostOper_Getuserpostcomments_Request
        """
        wPost = PostManager.findPostByPostId(postId)

        if not wPost:
            ErrorCodeManager.raiseError("ErrorGate_noSuchPost")

        if not wPost.isCommentsLoaded():
            if wPost.isInLoadingCommentStatus():
                ErrorCodeManager.raiseError("ErrorGate_serverBusy")

            dbCb = ITableSaverLoaduserpostcommentsResponse(_request, wPost, latestCommentDt, targetNum)
            DbCacheHelper.getITableSaverProxy().loadUserPostComments(dbCb, postId)

            wPost.setLoadingCommentStatus(True)
            return

        commentList = wPost.getComments(latestCommentDt, targetNum)
        _request.response(commentList)

    def commitUserPost(self, sessionKey, title, content, tags, imageNum, _request):
        """
        :type sessionKey: str
        :type title: str
        :type content: str
        :type tags: list[str]
        :type imageNum: int
        :type _request: message.gate.ipostoper.IPostOper_Commituserpost_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        imageUploadTokes = SeqImageInfo()
        imageKeys = []
        for i in range(imageNum):
            imgKey = MyUuid.getUuid()
            imageKeys.append(imgKey)
            imgToken = ImageHelper.genImageUploadToken(imgKey)
            imageUploadTokes.append(imgToken)

        tUPost = TUserPost()
        tUPost.postId = MyUuid.getUuid()
        tUPost.userId = userEntity.getUserId()
        tUPost.title = title
        tUPost.content = content
        tUPost.imageKeys.extend(imageKeys)
        tUPost.tags.extend(tags)

        wUPost = WUserPost(tUPost)
        PostManager.addNewPost(tUPost)
        PostManager.addImageKeysToUpload(tUPost.postId, imageKeys)

        DbCacheHelper.getITableSaverProxy().updateTUserPost(None, wUPost.getTUserPost())

        _request.response(tUPost.postId, imageUploadTokes)

        ImageHelper.saveImages(userEntity, imageKeys)
        Logger.log("commitUserPost success")

    def didImageUpload(self, sessionKey, imageKeys, _request):
        """
        :type sessionKey: str
        :type imageKeys: list[str]
        :type _request: message.gate.ipostoper.IPostOper_Didimageupload_Request
        """
        DbCacheHelper.getITableSaverProxy().userImagesDidUpload(None, imageKeys)
        _request.response()

        postsToSave = PostManager.didImageUpload(imageKeys)
        tPostList = SeqTUserPost()
        tPostList.extend(postsToSave)
        DbCacheHelper.getITableSaverProxy().updateTUserPostBatch(None, tPostList)

    def getImageUploadTokens(self, sessionKey, imgNum, _request):
        """
        :type sessionKey: str
        :type imgNum: int
        :type _request: message.gate.ipostoper.IPostOper_Getimageuploadtokens_Request
        """
        imageUploadTokes = SeqImageInfo()
        for i in range(0, imgNum):
            imgKey = MyUuid.getUuid()
            imgToken = ImageHelper.genImageUploadToken(imgKey)
            imageUploadTokes.append(imgToken)

        _request.response(imageUploadTokes)

    def getImageDownloadTokens(self, sessionKey, imgKey, imgFormat, _request):
        """
        :type sessionKey: str
        :type imgKey: str
        :type imgFormat: str
        :type _request: message.gate.ipostoper.IPostOper_Getimagedownloadtokens_Request
        """
        imgToken = ImageHelper.genImageDownloadToken(imgKey, imgFormat)
        _request.response(imgToken)

    def upvoteUserPost(self, sessionKey, postId, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type _request: message.gate.ipostoper.IPostOper_Upvoteuserpost_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        wuPost = PostManager.findPostByPostId(postId)
        if not wuPost:
            ErrorCodeManager.raiseError("ErrorGate_noSuchPost")

        if not wuPost.isCommentsLoaded():
            if wuPost.isInLoadingCommentStatus():
                ErrorCodeManager.raiseError("ErrorGate_serverBusy")

            dbCb = IPreLoadUserPostCommentsResponse(_request, userEntity, wuPost, EInteractiveType.Upvote)
            DbCacheHelper.getITableSaverProxy().loadUserPostComments(dbCb, wuPost.getPostId())

            wuPost.setLoadingCommentStatus(True)
        else:
            if wuPost.hasUpvoted(userEntity.getUserId()):
                ErrorCodeManager.raiseError("ErrorGate_hasUpvotedUserPost")

            PostHelper.addNewCommentToUserPost(userEntity, wuPost, EInteractiveType.Upvote)
            _request.response()

    def unupvoteUserPost(self, sessionKey, postId, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type _request: message.gate.ipostoper.IPostOper_Unupvoteuserpost_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        wuPost = PostManager.findPostByPostId(postId)
        if not wuPost:
            ErrorCodeManager.raiseError("ErrorGate_noSuchPost")

        dbCb = RemoveUserPostUpvoteResponse(_request, wuPost, userEntity)
        DbCacheHelper.getITableSaverProxy().removeUserPostUpvote(dbCb, postId, userEntity.getUserId())

    def shareUserPost(self, sessionKey, postId, shareType, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type shareType: int
        :type _request: message.gate.ipostoper.IPostOper_Shareuserpost_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        wuPost = PostManager.findPostByPostId(postId)
        if not wuPost:
            ErrorCodeManager.raiseError("ErrorGate_noSuchPost")

        content = str(EInteractiveType.Shared)
        if not wuPost.isCommentsLoaded():
            if wuPost.isInLoadingCommentStatus():
                ErrorCodeManager.raiseError("ErrorGate_serverBusy")

            dbCb = IPreLoadUserPostCommentsResponse(_request, userEntity, wuPost, EInteractiveType.Shared, content)
            DbCacheHelper.getITableSaverProxy().loadUserPostComments(dbCb, wuPost.getPostId())

            wuPost.setLoadingCommentStatus(True)
        else:
            PostHelper.addNewCommentToUserPost(userEntity, wuPost, EInteractiveType.Shared, content)
            _request.response()

    def commentUserPost(self, sessionKey, postId, comments, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type comments: str
        :type _request: message.gate.ipostoper.IPostOper_Commentuserpost_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        wuPost = PostManager.findPostByPostId(postId)
        if not wuPost:
            ErrorCodeManager.raiseError("ErrorGate_noSuchPost")

        if not wuPost.isCommentsLoaded():
            if wuPost.isInLoadingCommentStatus():
                ErrorCodeManager.raiseError("ErrorGate_serverBusy")

            dbCb = IPreLoadUserPostCommentsResponse(_request,
                    userEntity, wuPost, EInteractiveType.Comment, comments, [], True)
            DbCacheHelper.getITableSaverProxy().loadUserPostComments(dbCb, wuPost.getPostId())

            wuPost.setLoadingCommentStatus(True)
        else:
            commentId = PostHelper.addNewCommentToUserPost(userEntity, wuPost, EInteractiveType.Comment, comments)
            _request.response(commentId)

    def replyUserPostComment(self, sessionKey, postId, commentId, mentionedUserId, comments, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type commentId: str
        :type mentionedUserId: str
        :type comments: str
        :type _request: message.gate.ipostoper.IPostOper_Replyuserpostcomment_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        wuPost = PostManager.findPostByPostId(postId)
        if not wuPost:
            ErrorCodeManager.raiseError("ErrorGate_noSuchPost")

        mentionedEntity = UserEntityManager.findUserEntityByUserId(mentionedUserId)
        if not mentionedEntity:
            ErrorCodeManager.raiseError("ErrorGate_mentionedUserNotExisted")

        if not wuPost.hasComment(commentId):
            ErrorCodeManager.raiseError("ErrorGate_dstCommentNotExisted")

        commentId = PostHelper.addNewCommentToUserPost(userEntity,
                        wuPost, EInteractiveType.Comment, comments, [mentionedUserId], True)

        _request.response(commentId)

    def queryUserPostUpvoteStatus(self, sessionKey, postIdList, _request):
        """
        :type sessionKey: str
        :type postIdList: list[str]
        :type _request: message.gate.ipostoper.IPostOper_Queryuserpostupvotestatus_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        notReadyPostIdList = SeqString()
        readyDict = DictStringBool()

        for postId in postIdList:
            wUserPost = PostManager.findPostByPostId(postId)
            if not wUserPost:
                Logger.log("queryUserPostUpvoteStatus. no such post:", postId)
                readyDict[postId] = False
            elif not wUserPost.isCommentsLoaded():
                notReadyPostIdList.append(postId)
            else:
                if wUserPost.hasUpvoted(userEntity.getUserId()):
                    readyDict[postId] = True
                else:
                    readyDict[postId] = False

        if notReadyPostIdList:
            dbCb = QueryUserPostsUpvotedStatusResponse(_request, readyDict)
            DbCacheHelper.getITableSaverProxy().queryUserPostUpvoteStatus(dbCb, userEntity.getUserId(), notReadyPostIdList)
        else:
            _request.response(readyDict)

    def viewUserPost(self, deviceCode, postId, _request):
        """
        :type deviceCode: str
        :type postId: str
        :type _request: message.gate.ipostoper.IPostOper_Viewuserpost_Request
        """

        wUserPost = PostManager.findPostByPostId(postId)
        if not wUserPost:
            ErrorCodeManager.raiseError("ErrorGate_noSuchPost")

        wUserPost.getTUserPost().viewTimes += 1
        DbCacheHelper.getITableSaverProxy().updateTUserPost(None, wUserPost.getTUserPost())
        _request.response(wUserPost.getTUserPost().viewTimes)

        # log
        userEntity = UserEntityManager.findUserEntityByDeviceCode(deviceCode)
        if userEntity:
            DbLogHepler.logUserPostOper(userEntity.getLogUserInfo(), ELogPostOperType.View)
        else:
            userInfo = SLogUserInfo()
            userInfo.deviceCode = deviceCode
            DbLogHepler.logUserPostOper(userInfo, ELogPostOperType.View)
