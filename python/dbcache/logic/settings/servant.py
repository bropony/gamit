"""
* @name servant.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/9 19:28
*
* @desc servant.py
"""

from gamit.log.logger import Logger
from gamit.singleton.singleton import Singleton
from logic.ilogindbimpl import ILoginDbImpl
from logic.iuserdbimpl import IUserDbImpl
from logic.itablesaverimpl import ITableSaverImpl

class ServantSetting(Singleton):
    @staticmethod
    def initServant(server):
        Logger.logInfo("adding servants for DbCache")

        server.addServant(ILoginDbImpl())
        server.addServant(IUserDbImpl())
        server.addServant(ITableSaverImpl())
