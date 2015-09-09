"""
@author: mahanzhou
@date: 8/6/15
@file: 
@desc:

"""

from gamit.log.logger import Logger
from gamit.message.commandhandler import CommandHandlerBase

from message.db.mongodb.posttables import TSysTopic
from social.systopicmanager import SysTopicManager

class SysTopicMessageHandler(CommandHandlerBase):

    def onMessage(self, command, toIdList, data):
        """
        :type command: int
        :type toIdList: list[int]
        :type data: TSysTopic
        """

        pass
