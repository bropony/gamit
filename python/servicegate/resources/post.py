"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:

"""
from user.userentitymanager import UserEntityManager
from gamit.log.logger import Logger
from helpers.imagehelper import ImageHelper

from message.db.mongodb.posttables import TUserPost
from message.db.mongodb.posttables import TUserPostComment, SeqTUserPostComment
from message.gate.gatemsg import SUserPost, SeqUserPost, SComment, SeqComment
from message.gate.gatemsg import SImageInfo, SUserBriefWithoutAvatar
from message.common.publicdef import EInteractiveType
import datetime

class WUserPost:
    """
    :type tUserPost: TUserPost
    :type comments: list[TUserPostComment]
    """
    def __init__(self, tUserPost):
        if not isinstance(tUserPost, TUserPost):
            raise Exception("WUserPost.__init__", "TypeError")

        self.tUserPost = tUserPost

        self.upvoteUserSet = set()
        self.comments = SeqTUserPostComment()

        self.inLoadingCommentsStatus = False

    def setLoadingCommentStatus(self, isLoading):
        self.inLoadingCommentsStatus = isLoading

    def isInLoadingCommentStatus(self):
        return self.inLoadingCommentsStatus

    def getCreateDt(self):
        """
        :rtype: datetime.datetime
        """
        return self.tUserPost.createDt

    def getTUserPost(self):
        return self.tUserPost

    def appendComments(self, comments):
        """
        :type comments: list[TUserPostComment]
        :return:
        """
        self.comments.extend(comments)

        for cmt in comments:
            if cmt.interActiveType == EInteractiveType.Upvote:
                self.upvoteUserSet.add(cmt.userId)

    def getClientInfo(self, imgFormat=""):
        """
        :rtype: SUserPost
        """

        clientInfo = SUserPost()
        clientInfo.postId = self.tUserPost.postId
        clientInfo.title = self.tUserPost.title
        clientInfo.content = self.tUserPost.content
        clientInfo.createDt = self.tUserPost.createDt
        clientInfo.sharedTimes = self.tUserPost.sharedTimes
        clientInfo.commentedTimes = self.tUserPost.commentedTimes
        clientInfo.upvotedTimes = self.tUserPost.upvotedTimes
        clientInfo.viewTimes = self.tUserPost.viewTimes

        userEntity = UserEntityManager.findUserEntityByUserId(self.tUserPost.userId)
        if userEntity:
            clientInfo.userInfo = userEntity.getUserBriefInfo()
        else:
            Logger.log("WUserPost.getClientInfo", "UserInfoNotFoundForPost:", self.tUserPost.postId)

        for imgKey in self.tUserPost.imageKeys:
            imgInfo = ImageHelper.genImageDownloadToken(imgKey, imgFormat)
            clientInfo.images.append(imgInfo)

        return clientInfo

    def addNewComment(self, comment):
        """
        :type comment: TUserPostComment
        """
        self.comments.insert(0, comment)

        if comment.interActiveType == EInteractiveType.Comment:
            self.tUserPost.commentedTimes += 1
        elif comment.interActiveType == EInteractiveType.Upvote:
            self.tUserPost.upvotedTimes += 1
            self.upvoteUserSet.add(comment.userId)
        elif comment.interActiveType == EInteractiveType.Shared:
            self.tUserPost.sharedTimes += 1

    def removeComment(self, commentId):
        for idx in range(len(self.comments)):
            if self.comments[idx].commentId == commentId:
                del self.comments[idx]
                break

    def removeUpvoteRecord(self, commentId, userId):
        self.removeComment(commentId)

        if userId in self.upvoteUserSet:
            self.upvoteUserSet.remove(userId)

    def hasUpvoted(self, userId):
        """
        :rtype: bool
        """

        if userId in self.upvoteUserSet:
            return True

        return False

    def isCommentsLoaded(self):
        """
        :rtype: bool
        """

        if not self.tUserPost.commentedTimes:
            return True

        if not self.comments:
            return False

        return True

    def hasComment(self, commentId):
        """
        :type commentId: str
        :rtype: bool
        """
        for cmt in self.comments:
            if cmt.commentId == commentId:
                return True

        return False

    def getPostId(self):
        return self.tUserPost.postId

    def getOwnerUserId(self):
        return self.tUserPost.userId

    def getComments(self, dtThres, targetNum):
        """
        :rtype: list[SComment]
        """
        res = SeqComment()
        now = datetime.datetime.now()

        for cmt in self.comments:
            if cmt.interActiveType != EInteractiveType.Comment:
                continue

            if (dtThres < now) and (dtThres <= cmt.createDt):
                continue

            sComment = SComment()
            sComment.comment = cmt.commentId
            sComment.interActiveType = cmt.interActiveType
            sComment.comment = cmt.content
            sComment.commentDt = cmt.createDt

            userEntity = UserEntityManager.findUserEntityByUserId(cmt.userId)
            if userEntity:
                sComment.commenterInfo = userEntity.getUserBriefInfo()
            else:
                sComment.commenterInfo.userId = cmt.userId

            for userId in cmt.mentionedUsers:
                userEntity = UserEntityManager.findUserEntityByUserId(userId)
                if userEntity:
                    sComment.mentioned.append(userEntity.getUserBriefWithoutAvatar())

            res.append(sComment)

            if len(res) >= targetNum:
                break

        return res

    def areAllImagesUploaded(self):
        if len(self.getTUserPost().imageKeys) <= self.getTUserPost().imgageUploadedNum:
            return True
        else:
            return False
