__author__ = 'mahanzhou'

from gamit.log.logger import Logger
from message.db.itablesaver import ITableSaverServant
from gamit.mongodb.database import MongoDatabase
from staticdata.manager.ErrorCodeManager import ErrorCodeManager
from helpers.dboperhelper import DbOperHelper

from message.common.publicdef import SeqString, DictStringBool, EInteractiveType
from message.db.mongodb.usertables import TFamilyMember
from message.db.mongodb.posttables import TSysTopic, SeqTSysTopic
from message.db.mongodb.posttables import TSysTopicComment, SeqTSysTopicComment
from message.db.mongodb.posttables import TUserPost, SeqTUserPost
from message.db.mongodb.posttables import TUserPostComment, SeqTUserPostComment
from message.db.mongodb.usertables import TUserImage, SeqTUserImage
from message.db.mongodb.usertables import TUserFan, SeqTUserFan

class ITableSaverImpl(ITableSaverServant):
    def updateTUserAddress(self, userAddresss, _request):
        """
        :type userAddresss: message.db.mongodb.usertables.TUserAddress
        :type _request: message.db.itablesaver.ITableSaver_Updatetuseraddress_Request
        """
        DbOperHelper.generalUpdate(userAddresss, _request)

    def updateTUserBasic(self, userBasic, _request):
        """
        :type userBasic: message.db.mongodb.usertables.TUserBasic
        :type _request: ITableSaver_Updatetuserbasic_Request
        """

        DbOperHelper.generalUpdate(userBasic, _request)

    def updateTUserSettings(self, userSettings, _request):
        """
        :type userSettings: message.db.mongodb.usertables.TUserSettings
        :type _request: ITableSaver_Updatetusersettings_Request
        """

        DbOperHelper.generalUpdate(userSettings, _request)


    def updateTFamilyMember(self, familyMember, _request):
        """
        :type familyMember: message.db.mongodb.usertables.TFamilyMember
        :type _request: ITableSaver_Updatetfamilymember_Request
        """

        DbOperHelper.generalUpdate(familyMember, _request)

    def updateTFamilyMemberBatch(self, familyMembers, _request):
        """
        :type familyMembers: list[message.db.mongodb.usertables.TFamilyMember]
        :type _request: ITableSaver_Updatetfamilymemberbatch_Request
        """

        tb = MongoDatabase.findTableByMessageType(TFamilyMember)

        if tb:
            tb.update(familyMembers)
        else:
            error = ErrorCodeManager.getError("ErrorDb_TableNotFound")
            _request.error(error.what, error.code)
            return

        _request.response()

    def removeFamilyMembers(self, userId, indexes, _request):
        """
        :type userId: str
        :type indexes: list[int]
        :type _request: ITableSaver_Removefamilymembers_Request
        """

        tb = MongoDatabase.findTableByMessageType(TFamilyMember)

        if not tb:
            error = ErrorCodeManager.getError("ErrorDb_TableNotFound")
            _request.error(error.what, error.code)
            return

        for index in indexes:
            query = {TFamilyMember.fn_userId: userId, TFamilyMember.fn_index: index}
            tb.delete(query, True)

        _request.response()

    def updateTSysTopic(self, sysTopic, _request):
        """
        :type sysTopic: message.db.mongodb.posttables.TSysTopic
        :type _request: message.db.itablesaver.ITableSaver_Updatetsystopic_Request
        """
        DbOperHelper.generalUpdate(sysTopic, _request)

    def loadSysTopics(self, pageIndex, numPerPage, _request):
        """
        :type pageIndex: int
        :type numPerPage: int
        :type _request: message.db.itablesaver.ITableSaver_Loadsystopics_Request
        """
        Logger.log("Loading SysTopics request...")

        tb = MongoDatabase.findTableByMessageType(TSysTopic)
        if not tb:
            error = ErrorCodeManager.getError("ErrorDb_TableNotFound")
            _request.error(error.what, error.code)
            return

        skips = pageIndex * numPerPage
        res = tb.findManyWithQuey({}, limit=numPerPage, skip=skips, sort=[("_id", -1)])
        topicList = SeqTSysTopic()
        topicList.extend(res)
        _request.response(topicList)

    def updateTSysTopicComment(self, comments, _request):
        """
        :type comments: message.db.mongodb.posttables.TSysTopicComment
        :type _request: message.db.itablesaver.ITableSaver_Updatetsystopiccomment_Request
        """
        DbOperHelper.generalUpdate(comments, _request)

    def loadSysTopicComments(self, topicId, _request):
        """
        :type topicId: str
        :type _request: message.db.itablesaver.ITableSaver_Loadsystopiccomments_Request
        """
        tb = MongoDatabase.findTableByMessageType(TSysTopicComment)
        if not tb:
            return DbOperHelper.generalError(_request, "ErrorDb_TableNotFound")

        res = tb.findManyWithQuey({TSysTopicComment.fn_topicId: topicId}, limit=10000, sort=[("_id", -1)])
        commentList = SeqTSysTopicComment()
        commentList.extend(res)

        _request.response(commentList)

    def querySysTopicUpvoteStatus(self, userId, sysTopicIdList, _request):
        """
        :type userId: str
        :type sysTopicIdList: list[str]
        :type _request: message.db.itablesaver.ITableSaver_Querysystopicupvatestatus_Request
        """
        tb = MongoDatabase.findTableByMessageType(TSysTopicComment)
        if not tb:
            return DbOperHelper.generalError(_request, "ErrorDb_TableNotFound")

        resDict = DictStringBool()
        for topicId in sysTopicIdList:
            found = tb.findOneWithQuery({TSysTopicComment.fn_topicId: topicId,
                                         TSysTopicComment.fn_userId: userId,
                                         TSysTopicComment.fn_interActiveType: EInteractiveType.Upvote})
            if found:
                resDict[topicId] = True
            else:
                resDict[topicId] = False

        _request.response(resDict)

    def removeSysTopicUpvote(self, topicId, userId, _request):
        """
        :type topicId: str
        :type userId: str
        :type _request: message.db.itablesaver.ITableSaver_Removesystopicupvote_Request
        """
        tb = MongoDatabase.findTableByMessageType(TSysTopicComment)
        if not tb:
            return DbOperHelper.generalError(_request, "ErrorDb_TableNotFound")

        commentFound = tb.findOneWithQuery({TSysTopicComment.fn_topicId: topicId,
                                            TSysTopicComment.fn_userId: userId,
                                            TSysTopicComment.fn_interActiveType: EInteractiveType.Upvote})
        if not commentFound:
            return DbOperHelper.generalError(_request, "ErrorGate_noSuchUpvote")

        tb.delete({TSysTopicComment.fn_commentId: commentFound.commentId})
        _request.response(commentFound.commentId)

    def updateTUserPost(self, userPost, _request):
        """
        :type userPost: message.db.mongodb.posttables.TUserPost
        :type _request: message.db.itablesaver.ITableSaver_Updatetuserpost_Request
        """
        DbOperHelper.generalUpdate(userPost, _request)

    def updateTUserPostBatch(self, userPostList, _request):
        """
        :type userPostList: list[message.db.mongodb.posttables.TUserPost]
        :type _request: message.db.itablesaver.ITableSaver_Updatetuserpostbatch_Request
        """
        for userPost in userPostList:
            DbOperHelper.generalUpdate(userPostList)

        _request.response()

    def loadUserPosts(self, pageIndex, numPerPage, _request):
        """
        :type pageIndex: int
        :type numPerPage: int
        :type _request: message.db.itablesaver.ITableSaver_Loaduserposts_Request
        """
        tb = MongoDatabase.findTableByMessageType(TUserPost)
        if not tb:
            return DbOperHelper.generalError(_request, "ErrorDb_TableNotFound")

        skips = pageIndex * numPerPage
        data = tb.findManyWithQuey({}, limit=numPerPage, skip=skips, sort=[("_id", -1)])
        userPostList = SeqTUserPost()
        userPostList.extend(data)
        _request.response(userPostList)

    def updateTUserPostComment(self, comments, _request):
        """
        :type comments: message.db.mongodb.posttables.TUserPostComment
        :type _request: message.db.itablesaver.ITableSaver_Updatetuserpostcomment_Request
        """
        DbOperHelper.generalUpdate(comments, _request)

    def loadUserPostComments(self, postId, _request):
        """
        :type postId: str
        :type _request: message.db.itablesaver.ITableSaver_Loaduserpostcomments_Request
        """
        tb = MongoDatabase.findTableByMessageType(TUserPostComment)
        if not tb:
            return DbOperHelper.generalError(_request, "ErrorDb_TableNotFound")

        data = tb.findManyWithQuey({TUserPostComment.fn_postId: postId}, sort=[("_id", -1)])
        commontList = SeqTUserPostComment()
        commontList.extend(data)
        _request.response(commontList)

    def queryUserPostUpvoteStatus(self, userId, postIdList, _request):
        """
        :type userId: str
        :type postIdList: list[str]
        :type _request: message.db.itablesaver.ITableSaver_Queryuserpostupvotestatus_Request
        """
        statusDict = DictStringBool()
        tb = MongoDatabase.findTableByMessageType(TUserPostComment)
        if not tb:
            return DbOperHelper.generalError(_request, "ErrorDb_TableNotFound")

        for postId in postIdList:
            query = tb.findOneWithQuery({TUserPostComment.fn_postId: postId,
                                         TUserPostComment.fn_userId: userId,
                                         TUserPostComment.fn_interActiveType: EInteractiveType.Upvote})
            if query:
                statusDict[postId] = True
            else:
                statusDict[postId] = False

        _request.response(statusDict)

    def removeUserPostUpvote(self, postId, userId, _request):
        """
        :type postId: str
        :type userId: str
        :type _request: message.db.itablesaver.ITableSaver_Removeuserpostupvote_Request
        """
        tb = MongoDatabase.findTableByMessageType(TUserPostComment)
        if not tb:
            return DbOperHelper.generalError(_request, "ErrorDb_TableNotFound")

        commentFound = tb.findOneWithQuery({TUserPostComment.fn_postId: postId,
                                            TUserPostComment.fn_userId: userId,
                                            TUserPostComment.fn_interActiveType: EInteractiveType.Upvote})

        if not commentFound:
            return DbOperHelper.generalError(_request, "ErrorGate_noSuchUpvote")

        commentId = commentFound.commentId
        tb.delete({TUserPostComment.fn_commentId: commentId})
        _request.response(commentId)

    def saveUserImages(self, userImages, _request):
        """
        :type userImages: list[message.db.mongodb.usertables.TUserImage]
        :type _request: message.db.itablesaver.ITableSaver_Saveuserimages_Request
        """
        tb = MongoDatabase.findTableByMessageType(TUserImage)
        if not tb:
            Logger.log("Table {} not found".format(TUserImage.__name__))
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        tb.save(userImages)
        _request.response()

    def userImagesDidUpload(self, imageKeys, _request):
        """
        :type imageKeys: list[str]
        :type _request: message.db.itablesaver.ITableSaver_Userimagesdidupload_Request
        """
        tb = MongoDatabase.findTableByMessageType(TUserImage)
        if not tb:
            Logger.log("Table {} not found".format(TUserImage.__name__))
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        for imgKey in imageKeys:
            tb.updateWithQuery({tb.key: imgKey}, {"$set":{"isUploaded": True}}, upsert=False, update_one=True)

        _request.response()

    def updateFanInfo(self, fanInfo, _request):
        """
        :type fanInfo: message.db.mongodb.usertables.TUserFan
        :type _request: message.db.itablesaver.ITableSaver_Updatefaninfo_Request
        """
        DbOperHelper.generalUpdate(fanInfo, _request)

    def getFansByUserIdAndPageIndex(self, userId, pageIdx, _request):
        """
        :type userId: str
        :type pageIdx: int
        :type _request: message.db.itablesaver.ITableSaver_Getfansbyuseridandpageindex_Request
        """
        numPerPage = 100
        tb = MongoDatabase.findTableByMessageType(TUserFan)
        if not tb:
            Logger.log("Table {} not found".format(TUserFan.__name__))
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        skips = numPerPage * pageIdx
        res = tb.findManyWithQuey({TUserFan.fn_myUserId: userId}, limit=numPerPage, skip=skips, sort=[("_id", -1)])

        data = SeqTUserFan()
        data.extend(res)

        _request.response(data)

    def getFocusUseIdList(self, userId, _request):
        """
        :type userId: str
        :type _request: message.db.itablesaver.ITableSaver_Getfocususeidlist_Request
        """
        tb = MongoDatabase.findTableByMessageType(TUserFan)
        if not tb:
            Logger.log("Table {} not found".format(TUserFan.__name__))
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        res = tb.findManyWithQuey({TUserFan.fn_fanUserId: userId})
        data = SeqTUserFan()
        data.extend(res)

        _request.response(data)

        Logger.log("getFocusUseIdList:", _request._os.getBuffer())

    def hasFollowed(self, myUserId, focusUserId, _request):
        """
        :type myUserId: str
        :type focusUserId: str
        :type _request: message.db.itablesaver.ITableSaver_Hasfollowed_Request
        """
        tb = MongoDatabase.findTableByMessageType(TUserFan)
        if not tb:
            Logger.log("Table {} not found".format(TUserFan.__name__))
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        res = tb.findOneWithQuery({TUserFan.fn_fanUserId: myUserId, TUserFan.fn_myUserId: focusUserId})
        if res:
            _request.response(True)
        else:
            _request.response(False)

    def unfollow(self, myUserId, hisUserId, _request):
        """
        :type myUserId: str
        :type hisUserId: str
        :type _request: message.db.itablesaver.ITableSaver_Unfollow_Request
        """

        tb = MongoDatabase.findTableByMessageType(TUserFan)
        if not tb:
            Logger.log("Table {} not found".format(TUserFan.__name__))
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        res = tb.findOneWithQuery({"fanUserId": myUserId, "myUserId": hisUserId})
        if not res:
            ErrorCodeManager.raiseError("ErrorGate_didNotFollowThisUser")

        tb.delete({TUserFan.fn_recordId: res.recordId}, delete_one=True)

        _request.response()
