"""
* @name servant.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 10:30
*
* @desc servant.py
"""

from gamit.log.logger import Logger
from gamit.singleton.singleton import Singleton
from logic.itestimpl import ItestImpl

class ServantSetting(Singleton):
    _channelId = 0

    @classmethod
    def setChannelId(cls, cid):
        cls._channelId = cid

    @classmethod
    def getChannelId(cls):
        return cls._channelId

    @staticmethod
    def initServant(server):
        Logger.logInfo("adding servant ITest")
        server.addServant(ItestImpl("ITest"))