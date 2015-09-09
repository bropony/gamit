"""
@author: mahanzhou
@date: 8/6/15
@file: 
@desc:

"""
from gamit.log.logger import Logger
from gamit.utils.myuuid import MyUuid
from gamit.mongodb.database import MongoDatabase

from message.db.systemcommand import ESysCommandType
from message.db.mongodb.posttables import TSysTopic
import json

from social.systopicmanager import SysTopicManager

class __SystemCommandDigester:

    def digest(self, systemCommand):
        """
        :type systemCommand: message.db.mongodb.utiltables.TSystemCommand
        :rtype: bool
        """
        operStatus = False

        if systemCommand.commandType == ESysCommandType.AddSysTopic:
            operStatus = self.__addSysTopic(systemCommand)
        elif systemCommand.commandType == ESysCommandType.AddCommercialAd:
            pass
        else:
            Logger.logInfo("__SystemCommandDigester.digest: undigested command type:", systemCommand.commandType)

        return operStatus

    def __addSysTopic(self, scmd):
        """
        :type scmd: message.db.mongodb.utiltables.TSystemCommand
        :rtype: bool
        """

        jsTopic = json.loads(scmd.stringVal, "UTF8")

        tsysTopic = TSysTopic()
        tsysTopic._fromJson(jsTopic)

        tsysTopic.topicId = MyUuid.getUuid()

        tb = MongoDatabase.findTableByMessageType(TSysTopic)
        if not tb:
            Logger.logInfo("__SystemCommandDigester.__addSysTopic. Table not found: ", TSysTopic.__name__)
            return

        tb.save(tsysTopic)

        SysTopicManager.addNewSysTopics([tsysTopic])

        return True


SystemCommandDigester = __SystemCommandDigester()
