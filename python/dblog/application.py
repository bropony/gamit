"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:

"""

from staticdata.serverconfig import ServerConfigManager
import gamit.app.apptype as AppType
from gamit.log.logger import Logger
from gamit.app.application import ApplicationBase
from gamit.message.messagemanager import MessageManager
from gamit.timer.schedule import Scheduler
from gamit.rmi.sessionmanager import SessionManager


# settings
from logic.settings.servant import *

class Application(ApplicationBase):
    def __init__(self, name=None, channelId=0):
        super().__init__(name, channelId)

    # serve as a servant (server side logic)
    def initServant(self):
        channel = ServerConfigManager.getChannelByType(AppType.DBLOG)
        if not channel:
            Logger.logInfo("DBLOG channel not configured.")
            return False

        rmiServer = self.createRmiServer(channel, ServerConfigManager.isDebug)
        ServantSetting.initServant(rmiServer)
        return True

    def initMessageManager(self):
        return True

    def initProxies(self):
        # nothing to be done
        return True

# end of Application