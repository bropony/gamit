"""
* @name message.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/3 19:47
*
* @desc message.py
"""
from gamit.singleton.singleton import Singleton
from gamit.message.messagemanager import MessageManager

from logic.messagehandler.handlers import *
from message.command.innercommand import EDbUpdateCommand

class MessageSetting(Singleton):
    @staticmethod
    def initMessangeHandler():
        MessageManager.addCommandHandler(EDbUpdateCommand.NewSysTopic, SysTopicMessageHandler())

####