"""
@author: mahanzhou
@date: 8/24/15
@file: 
@desc:

"""

from gamit.utils.myuuid import MyUuid
from gamit.log.logger import Logger
from dbutil.dbsaver import DbSaver
from dbutil.dbloghelper import DbLogHepler
from social.systopic import WSysTopic
from message.logdb.logconst import ELogPostOperType
from message.db.mongodb.posttables import TSysTopicComment, TSysTopic
from message.gate.gateconst import EHintType
from message.gate.gatemsg import SUserPostCommentHint
from message.common.publicdef import EInteractiveType
from user.userentitymanager import UserEntityManager

class SysTopicHelper:
    @staticmethod
    def addNewCommentToSysTopic(userEntity, wSysTopic, interactiveType, content="", mentiondUsers=[]):
        """
        :type userEntity: user.userentity.UserEntity
        :type wSysTopic: WSysTopic
        :type interactiveType: int
        :type content: str
        :type mentiondUsers: list[str]
        :type replyComment: bool
        :rtype: str
        """

        tComment = TSysTopicComment()
        tComment.commentId = MyUuid.getUuid()
        tComment.interActiveType = interactiveType
        tComment.userId = userEntity.getUserId()
        tComment.topicId = wSysTopic.getTopicId()
        tComment.content = content
        tComment.mentionedUsers.extend(mentiondUsers)

        wSysTopic.addNewComment(tComment)
        DbSaver.saveTable(tComment)
        DbSaver.saveTable(wSysTopic.getTSysTopic())

        logType = 0
        if interactiveType == EInteractiveType.Comment:
            logType = ELogPostOperType.Comment

        elif interactiveType == EInteractiveType.Upvote:
            logType = ELogPostOperType.Upvote

        elif interactiveType == EInteractiveType.Shared:
            logType = ELogPostOperType.Share


        DbLogHepler.logSysTopicOper(userEntity.getLogUserInfo(), wSysTopic.getTopicId(), logType)

        return tComment.commentId
