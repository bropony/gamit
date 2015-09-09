"""
* @name servant.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 10:30
*
* @desc servant.py
"""

from staticdata.serverconfig import ServerConfigManager
from gamit.log.logger import Logger
from gamit.singleton.singleton import Singleton
from logic.itestimpl import ITestImpl
from logic.iloginimpl import ILoginImpl
from logic.iuserinfoimpl import IUserInfoImpl
from logic.ipostoperimpl import IPostOperImpl
from logic.itaileroperimpl import ITailerOperImpl

from user.userentitymanager import UserEntityManager

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
        """
        :type server: gamit.rmi.rmiserver.RmiServer
        """
        # add client connection close callback
        server.setClientConnectionCloseCallback(UserEntityManager)

        # register callbacks
        Logger.logInfo("adding servants for ServiceGate")
        if ServerConfigManager.isTestInterfaceEnabled:
            server.addServant(ITestImpl())

        server.addServant(IUserInfoImpl())
        server.addServant(ILoginImpl())
        server.addServant(IPostOperImpl())
        server.addServant(ITailerOperImpl())
