"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:

"""

from gamit.log.logger import Logger
from gamit.singleton.singleton import Singleton

from logic.iloguseroperimpl import ILogUserOperImpl

class ServantSetting(Singleton):
    @staticmethod
    def initServant(server):
        Logger.logInfo("adding servants for DbLog")
        server.addServant(ILogUserOperImpl())
