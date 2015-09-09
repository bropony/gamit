"""
@author: mahanzhou
@date: 8/12/15
@file: 
@desc:

"""

from gamit.utils.myuuid import MyUuid
from gamit.log.logger import Logger
from helpers.dbcachehelper import DbCacheHelper
from helpers.dbloghelper import DbLogHepler
from resources.postmanager import PostManager
from resources.post import WUserPost
from message.logdb.logconst import ELogPostOperType
from message.db.mongodb.posttables import TUserPostComment, TUserPost
from message.gate.gateconst import EHintType
from message.gate.gatemsg import SUserPostCommentHint
from message.common.publicdef import EInteractiveType
from user.userentitymanager import UserEntityManager

class PostHelper:
    @staticmethod
    def addNewCommentToUserPost(userEntity, wuPost, interactiveType, content="", mentiondUsers=[], replyComment=False):
        """
        :type userEntity: user.userentity.UserEntity
        :type wuPost: WUserPost
        :type interactiveType: int
        :type content: str
        :type mentiondUsers: list[str]
        :type replyComment: bool
        :rtype: str
        """

        tComment = TUserPostComment()
        tComment.commentId = MyUuid.getUuid()
        tComment.interActiveType = interactiveType
        tComment.userId = userEntity.getUserId()
        tComment.postId = wuPost.getPostId()
        tComment.content = content
        tComment.mentionedUsers.extend(mentiondUsers)

        wuPost.addNewComment(tComment)
        DbCacheHelper.getITableSaverProxy().updateTUserPostComment(None, tComment)
        DbCacheHelper.getITableSaverProxy().updateTUserPost(None, wuPost.getTUserPost())

        hintType = 0
        logType = 0

        if interactiveType == EInteractiveType.Comment:
            if replyComment:
                hintType = EHintType.PostCommentReplied
            else:
                hintType = EHintType.PostCommented
            logType = ELogPostOperType.Comment

        elif interactiveType == EInteractiveType.Upvote:
            hintType = EHintType.PostUpvoted
            logType = ELogPostOperType.Upvote

        elif interactiveType == EInteractiveType.Shared:
            hintType = EHintType.PostReposted
            logType = ELogPostOperType.Share

        if not hintType:
            Logger.log("[PostHelper.addNewCommentToUserPost] Unknown InteractiveType:", interactiveType)
        else:
            ownerEntity = UserEntityManager.findUserEntityByUserId(wuPost.getOwnerUserId())
            if not ownerEntity:
                Logger.log("[PostHelper.addNewCommentToUserPost] UserNotFound:", wuPost.getOwnerUserId())
            else:
                cmtHit = SUserPostCommentHint()
                cmtHit.hintType = hintType
                cmtHit.operUserInfo = userEntity.getUserBriefInfo()
                cmtHit.content = content
                cmtHit.postId = wuPost.getPostId()
                cmtHit.commentId = tComment.commentId

                ownerEntity.addCommentHint(cmtHit)

        DbLogHepler.logUserPostOper(userEntity.getLogUserInfo(), wuPost.getPostId(), logType)

        return tComment.commentId
