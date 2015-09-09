"""
* @name dbcache.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/9 19:49
*
* @desc dbcache.py

"""
from gamit.log.logger import Logger
from gamit.rmi.proxymanager import ProxyManager
from gamit.app import apptype as AppType
from logic.connection.connectioninfo import ConnectionInfo

from user.userdataloader import UserDataLoader
from resources.resourceloader import ResourceLoader

class DbCacheConnectCallback:
    isDataLoaded = False

    def __call__(self, isOpenCallback):
        if isOpenCallback:
            self.onOpen()
        else:
            self.onClose()

    def __init__(self, channel):
        self.channel = channel

    def onOpen(self):
        Logger.logInfo("ConnectionInfo", "Connected to dbcache")
        ConnectionInfo.setDbCacheOpen(True)

        if not DbCacheConnectCallback.isDataLoaded:
            UserDataLoader.loadUserInfos()
            ResourceLoader.load()

            DbCacheConnectCallback.isDataLoaded = True

    def onClose(self):
        Logger.logInfo("ConnectionInfo", "dbcache connection closed")
        ConnectionInfo.setDbCacheOpen(False)

class DbLogConnectCallback:
    def __call__(self, isOpenCallback):
        if isOpenCallback:
            self.onOpen()
        else:
            self.onClose()

    def __init__(self, channel):
        self.channel = channel

    def onOpen(self):
        Logger.logInfo("ConnectionInfo", "Connected to dbLog")
        ConnectionInfo.setDbLogOpen(True)

    def onClose(self):
        Logger.logInfo("ConnectionInfo", "dbLog connection closed")
        ConnectionInfo.setDbLogOpen(False)