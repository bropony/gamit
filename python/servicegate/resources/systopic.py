"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:

"""

from message.gate.gatemsg import SSysTopic, SComment, SeqComment
from message.db.mongodb.posttables import TSysTopicComment, SeqTSysTopicComment
from helpers.imagehelper import ImageHelper
from message.common.publicdef import EInteractiveType
from user.userentitymanager import UserEntityManager
import datetime

class WSysTopic:
    """
    :type tSysTopic: message.db.mongodb.posttables.TSysTopic
    :type comments: list[message.db.mongodb.posttables.TSysTopicComment]
    :type latestUpvoteList: list[message.db.mongodb.posttables.TSysTopicComment]
    """
    def __init__(self, tSysTopic):
        self.tSysTopic = tSysTopic

        self.comments = SeqTSysTopicComment()
        self.upvoteUserSet = set()

        self.latestUpvoteList = SeqTSysTopicComment()
        self.cachedUpvoteSize = 10

        self.inLoadingCommentsStatus = False

    def setLoadingCommentStatus(self, isLoading):
        self.inLoadingCommentsStatus = isLoading

    def isInLoadingCommentStatus(self):
        return self.inLoadingCommentsStatus

    def getTSysTopic(self):
        """
        :rtype: message.db.mongodb.posttables.TSysTopic
        """
        return self.tSysTopic

    def getCreateDt(self):
        """
        :rtype: datetime.datetime
        """

        return self.tSysTopic.createDt

    def getTopicId(self):
        """
        :rtype: str
        """

        return self.tSysTopic.topicId

    def getClientInfo(self, imgFormat):
        """
        :rtype: SSysTopic
        """

        clientInfo = SSysTopic()
        clientInfo.topicId = self.tSysTopic.topicId
        clientInfo.title = self.tSysTopic.title
        clientInfo.content = self.tSysTopic.content
        clientInfo.tags.extend(self.tSysTopic.tags)
        clientInfo.createDt = self.tSysTopic.createDt
        clientInfo.sharedTimes = self.tSysTopic.sharedTimes
        clientInfo.commentedTimes = self.tSysTopic.commentedTimes
        clientInfo.upvotedTimes = self.tSysTopic.upvotedTimes
        clientInfo.viewTimes = self.tSysTopic.viewTimes

        for imgKey in self.tSysTopic.imageKeys:
            imgInfo = ImageHelper.genImageDownloadToken(imgKey, imgFormat)
            clientInfo.images.append(imgInfo)

        return clientInfo

    def isCommentLoaded(self):
        """
        :rtype: bool
        """
        totalComments = self.tSysTopic.commentedTimes + self.tSysTopic.sharedTimes + self.tSysTopic.upvotedTimes
        if 0 == totalComments:
            return True

        if not self.comments:
            return False

        return True

    def appendComments(self, tCommentList):
        """
        :type tCommentList: list[TSysTopicComment]
        """

        self.comments.extend(tCommentList)

        for tcmd in tCommentList:
            if tcmd.interActiveType == EInteractiveType.Upvote:
                self.upvoteUserSet.add(tcmd.userId)

                if len(self.latestUpvoteList) < self.cachedUpvoteSize:
                    self.latestUpvoteList.append(tcmd)

    def addNewComment(self, tComment):
        """
        :type tComment: TSysTopicComment
        """
        self.comments.insert(0, tComment)

        if tComment.interActiveType == EInteractiveType.Comment:
            self.tSysTopic.commentedTimes += 1
        elif tComment.interActiveType == EInteractiveType.Upvote:
            self.tSysTopic.upvotedTimes += 1
            self.upvoteUserSet.add(tComment.userId)
            self.latestUpvoteList.insert(0, tComment)
            if len(self.latestUpvoteList) > self.cachedUpvoteSize:
                del self.latestUpvoteList[-1]

        elif tComment.interActiveType == EInteractiveType.Shared:
            self.tSysTopic.sharedTimes += 1

    def removeComment(self, commentId):
        for idx in range(len(self.comments)):
            if self.comments[idx].commentId == commentId:
                del self.comments[idx]
                break

    def removeUpvoteRecord(self, commentId, userId):
        self.removeComment(commentId)
        if userId in self.upvoteUserSet:
            self.upvoteUserSet.remove(userId)

        for idx in range(len(self.latestUpvoteList)):
            if self.latestUpvoteList[idx].commentId == commentId:
                del self.latestUpvoteList[idx]
                break

    def hasUpvoted(self, userId):
        """
        :type userId: str
        :rtype: bool
        """

        if userId in self.upvoteUserSet:
            return True

        return False

    def cmtTabel2Struct(self, tcmt, scmt):
        """
        :type tcmt: TSysTopicComment
        :type scmt: SComment
        """
        scmt.commentI = tcmt.commentId
        scmt.comment = tcmt.content
        scmt.interActiveType = tcmt.interActiveType
        scmt.commentDt = tcmt.createDt

        userEntity = UserEntityManager.findUserEntityByUserId(tcmt.userId)
        if userEntity:
            scmt.commenterInfo = userEntity.getUserBriefInfo()
        else:
            scmt.commenterInfo.userId = tcmt.userId

        for userId in tcmt.mentionedUsers:
            userEntity = UserEntityManager.findUserEntityByUserId(userId)
            if userEntity:
                scmt.mentioned.append(userEntity.getUserBriefWithoutAvatar())

    def getComments(self, thresDt, targetNum, interactiveType):
        """
        :type thresDt: datetime.datetime
        :type targetNum: int
        :rtype: SeqComment
        """

        now = datetime.datetime.now()
        res = SeqComment()

        # comments
        if interactiveType == EInteractiveType.Comment:
            for cmt in self.comments:
                if cmt.interActiveType != EInteractiveType.Comment:
                    continue

                if (thresDt < now) and (thresDt <= cmt.createDt):
                    continue

                sComment = SComment()
                self.cmtTabel2Struct(cmt, sComment)

                res.append(sComment)
                if len(res) >= targetNum:
                    break
        # upvotes
        elif interactiveType == EInteractiveType.Upvote:
            for cmt in self.latestUpvoteList:
                sComment = SComment()
                self.cmtTabel2Struct(cmt, sComment)

                res.append(sComment)

        return res
