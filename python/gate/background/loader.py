"""
@author: mahanzhou
@date: 8/6/15
@file: 
@desc:

"""

import datetime

from gamit.timer.timerbase import TimerBase
from gamit.timer.schedule import Scheduler
from gamit.mongodb.database import MongoDatabase
from gamit.log.logger import Logger

from message.db.mongodb.utiltables import TSystemCommand, TSystemCommandLog
from background.digester import SystemCommandDigester

class __SystemCommandLoder(TimerBase):
    def __init__(self):
        super().__init__()

    def handleTimeout(self, data):
        tbSystemCommand = MongoDatabase.findTableByMessageType(TSystemCommand)
        if not tbSystemCommand:
            Logger.log("Table {} not found".format(TSystemCommand.__name__))

        tbSystemCommandLog = MongoDatabase.findTableByMessageType(TSystemCommandLog)
        if not tbSystemCommandLog:
            Logger.log("Table {} not found".format(TSystemCommandLog.__name__))

        operDt = datetime.datetime.now()

        sysCommands = tbSystemCommand.findMany({})
        for scmd in sysCommands:
            if SystemCommandDigester.digest(scmd):
                self.saveDigestLog(scmd, operDt, tbSystemCommandLog)
            else:
                Logger.log("Operation Error: ", scmd._toJson())

        tbSystemCommand.deleteAll()

    def saveDigestLog(self, sysCommand, logDt, logTb):
        """
        :type sysCommand: TSystemCommand
        :param logDt: datetime.datetime
        """

        tLog = TSystemCommandLog()
        tLog.commandType = sysCommand.commandType
        tLog.priority = sysCommand.priority
        tLog.numericVal = sysCommand.numericVal
        tLog.stringVal = sysCommand.stringVal
        tLog.jsExtraInfo = sysCommand.jsExtraInfo
        tLog.processedDt = logDt

        logTb.save(tLog)

    def start(self):
        Scheduler.schedule(self, None, 10, 60)

SystemCommandLoder = __SystemCommandLoder()
