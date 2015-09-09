"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:

"""
import traceback
from message.gate.ipostoper import IPostOperServant
from social.postmanager import PostManager
from social.post import WUserPost
from social.posthelper import PostHelper
from social.systopicmanager import SysTopicManager
from social.systopichelper import SysTopicHelper
from dbutil.dbloghelper import DbLogHepler
from dbutil.dbsaver import DbSaver
from helpers.imagehelper import ImageHelper
from user.userentitymanager import UserEntityManager
from gamit.utils.myuuid import MyUuid
from gamit.log.logger import Logger
from gamit.mongodb.database import MongoDatabase
from staticdata.manager.ErrorCodeManager import ErrorCodeManager
from staticdata.manager.TopicTagConfigManager import TopicTagConfigManager

from message.common.publicdef import SeqString, EInteractiveType, DictStringBool
from message.logdb.logtables import SLogUserInfo
from message.logdb.logconst import ELogPostOperType
from message.gate.gatemsg import SImageInfo, SeqImageInfo
from message.db.mongodb.posttables import *
from message.db.mongodb.usertables import *
from message.gate.gatemsg import SMyFan, SeqMyFan, SMyFocus, SeqMyFocus

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

        numPerPage = 100
        tb = MongoDatabase.findTableByMessageType(TUserFan)
        if not tb:
            Logger.log("Table {} not found".format(TUserFan.__name__))
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        skips = numPerPage * pageIndex
        tFanList = tb.findManyWithQuey({TUserFan.fn_myUserId: userEntity.getUserId()},
                                  limit=numPerPage, skip=skips, sort=MongoDatabase.SortByIdDesc)

        sFanList = SeqMyFan()
        for tFan in tFanList:
            userEntity = UserEntityManager.findUserEntityByUserId(tFan.fanUserId)
            if not userEntity:
                Logger.log("getFansByPageIndex",
                           "UserNotFound:", tFan.fanUserId)
                continue

            sFan = SMyFan()
            sFan.fanInfo = userEntity.getUserBriefInfo()
            sFan.operDt = tFan.createDt

            sFanList.append(sFan)

        _request.response(sFanList)

    def getAllMyFocuses(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.ipostoper.IPostOper_Getallmyfocuses_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        tb = MongoDatabase.findTableByMessageType(TUserFan)
        if not tb:
            Logger.log("Table {} not found".format(TUserFan.__name__))
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        tFocusList = tb.findManyWithQuey({TUserFan.fn_fanUserId: userEntity.getUserId()})

        sFocusList = SeqMyFocus()

        for tFan in tFocusList:
            userEntity = UserEntityManager.findUserEntityByUserId(tFan.myUserId)
            if not userEntity:
                Logger.log("getAllMyFocuses",
                           "UserNotFound:", tFan.myUserId)
                continue

            sFocus = SMyFocus()
            sFocus.userInfo = userEntity.getUserBriefInfo()
            sFocus.operDt = tFan.createDt

            sFocusList.append(sFocus)

        _request.response(sFocusList)

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

        tb = MongoDatabase.findTableByMessageType(TUserFan)
        if not tb:
            Logger.log("Table {} not found".format(TUserFan.__name__))
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        res = tb.findOneWithQuery({TUserFan.fn_fanUserId: userEntity.getUserId(),
                                   TUserFan.fn_myUserId: hisEntity.getUserId()})

        if res:
            ErrorCodeManager.raiseError("ErrorGate_hasFollowedThisUser")

        tFan = TUserFan()
        tFan.recordId = MyUuid.getUuid()
        tFan.fanUserId = userEntity.getUserId()
        tFan.myUserId = hisEntity.getUserId()
        DbSaver.saveTable(tFan)

        sNewFocus = SMyFocus()
        sNewFocus.userInfo = hisEntity.getUserBriefInfo()
        sNewFocus.operDt = tFan.createDt

        # response
        _request.response(sNewFocus)

        sNewFan = SMyFan()
        sNewFan.fanInfo = userEntity.getUserBriefInfo()
        sNewFan.operDt = tFan.createDt
        hisEntity.addNewFan(sNewFan)

        userEntity.getTUserProperty().focusNum += 1
        hisEntity.getTUserProperty().fanNum += 1

        DbSaver.saveTable(userEntity.getTUserProperty())
        DbSaver.saveTable(hisEntity.getTUserProperty())

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

        tb = MongoDatabase.findTableByMessageType(TUserFan)
        if not tb:
            Logger.log("Table {} not found".format(TUserFan.__name__))
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        fanFound = tb.findOneWithQuery({TUserFan.fn_fanUserId: userEntity.getUserId(), TUserFan.fn_myUserId: userId})
        if not fanFound:
            ErrorCodeManager.raiseError("ErrorGate_didNotFollowThisUser")

        tb.delete({TUserFan.fn_recordId: fanFound.recordId}, delete_one=True)

        _request.response()

        userEntity.getTUserProperty().focusNum -= 1
        hisEntity.getTUserProperty().fanNum -= 1

        DbSaver.saveTable(userEntity.getTUserProperty())
        DbSaver.saveTable(hisEntity.getTUserProperty())

    #
    # Sys Topic Opers begins here
    #

    def getLatestSysTopics(self, deviceCode, tagId, latestTopicDt, targetNum, imgFormat, _request):
        """
        :type deviceCode: str
        :type tagId: str
        :type latestTopicDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.ipostoper.IPostOper_Getlatestsystopics_Request
        """

        tag = TopicTagConfigManager.getTagNameByTagId(tagId)

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

    def getFormerSysTopics(self, deviceCode, tagId, oldestTopicDt, targetNum, imgFormat, _request):
        """
        :type deviceCode: str
        :type tagId: str
        :type oldestTopicDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.ipostoper.IPostOper_Getformersystopics_Request
        """

        tag = TopicTagConfigManager.getTagNameByTagId(tagId)

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

        commentId = wSysTopic.removeUpvoteRecordByUserId(userEntity.getUserId())
        if not commentId:
            ErrorCodeManager.raiseError("ErrorGate_noSuchUpvote")

        wSysTopic.getTSysTopic().upvotedTimes -= 1
        DbSaver.saveTable(wSysTopic.getTSysTopic())

        DbSaver.deleteFromTable(TSysTopicComment, {TSysTopicComment.fn_commentId: commentId})

        _request.response()

        DbLogHepler.logSysTopicOper(userEntity.getLogUserInfo(),
                                    wSysTopic.getTopicId(),
                                    ELogPostOperType.Unupvote)

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
        for topicId in sysTopicIdList:
            wSysPost = SysTopicManager.getSysTopicByTopicId(topicId)
            if not wSysPost:
                readyStatusDict[topicId] = False
            else:
                if wSysPost.hasUpvoted(userEntity.getUserId()):
                    readyStatusDict[topicId] = True
                else:
                    readyStatusDict[topicId] = False

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

        DbSaver.saveTable(wSysTopic.getTSysTopic())

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

        postList = PostManager.getOlderPosts(tag, oldestPostDt, targetNum, imgFormat)
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

        DbSaver.saveTable(wUPost.getTUserPost())

        _request.response(tUPost.postId, imageUploadTokes)

        ImageHelper.saveImages(userEntity, imageKeys)
        Logger.log("commitUserPost success")

    def didImageUpload(self, sessionKey, imageKeys, _request):
        """
        :type sessionKey: str
        :type imageKeys: list[str]
        :type _request: message.gate.ipostoper.IPostOper_Didimageupload_Request
        """
        ImageHelper.imageUploaded(imageKeys)
        _request.response()

        postsToSave = PostManager.didImageUpload(imageKeys)
        DbSaver.saveTableBatch(postsToSave)

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

        commentId = wuPost.removeUpvoteRecordByUserId(userEntity.getUserId())

        if not commentId:
            ErrorCodeManager.raiseError("ErrorGate_noSuchUpvote")

        DbSaver.deleteFromTable(TUserPostComment, {TUserPostComment.fn_commentId: commentId})

        wuPost.getTUserPost().upvotedTimes -= 1
        DbSaver.saveTable(wuPost.getTUserPost())

        _request.response()

        DbLogHepler.logUserPostOper(userEntity.getLogUserInfo(),
                                    wuPost.getPostId(),
                                    ELogPostOperType.Unupvote)

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

        readyDict = DictStringBool()

        for postId in postIdList:
            wUserPost = PostManager.findPostByPostId(postId)
            if not wUserPost:
                Logger.log("queryUserPostUpvoteStatus. no such post:", postId)
                readyDict[postId] = False
            else:
                if wUserPost.hasUpvoted(userEntity.getUserId()):
                    readyDict[postId] = True
                else:
                    readyDict[postId] = False

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
        DbSaver.saveTable(wUserPost.getTUserPost())
        _request.response(wUserPost.getTUserPost().viewTimes)

        # log
        userEntity = UserEntityManager.findUserEntityByDeviceCode(deviceCode)
        if userEntity:
            DbLogHepler.logUserPostOper(userEntity.getLogUserInfo(), postId, ELogPostOperType.View)
        else:
            userInfo = SLogUserInfo()
            userInfo.deviceCode = deviceCode
            DbLogHepler.logUserPostOper(userInfo, postId, ELogPostOperType.View)

    def getMyUserByDateThreshold(self, sessionKey, thresholdDate, imgFormat, _request):
        """
        :type sessionKey: str
        :type thresholdDate: datetime.datetime
        :type _request: message.gate.ipostoper.IPostOper_Getmyuserpostlistbypageindex_Request
        :type imgFormat: str
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        res = PostManager.getUserPostListByUserId(userEntity.getUserId(),
                                                  thresholdDate,
                                                  20,
                                                  imgFormat,
                                                  userEntity.getTUserProperty().postNum)

        res.sort(key=lambda post: -post.createDt.now.timestamp())

        _request.response(res)

    def deleteUserPost(self, sessionKey, postId, _request):
        """
        :type sessionKey: str
        :type postId: str
        :type _request: message.gate.ipostoper.IPostOper_Deleteuserpost_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        wuPost = PostManager.findPostByPostId(postId)
        if not wuPost:
            ErrorCodeManager.raiseError("ErrorGate_noSuchPost")

        PostManager.deleteUserPost(postId)

        DbSaver.deleteFromTable(TUserPost, {TUserPost.fn_postId: postId})

        _request.response()
