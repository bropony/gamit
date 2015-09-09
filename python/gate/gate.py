"""
* @name gate.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/3 10:26
*
* @desc gate.py
"""

import sys
import os
import os.path

# add parent dir to searching paths
main_dir, _ = os.path.split(__file__)
parent_dir, _ = os.path.split(main_dir)
sys.path.append(parent_dir)

# imports
import staticdata.dataloader
from staticdata.serverconfig import ServerConfigManager
from gamit.log.logger import Logger
from gamit.utils.imagetoken import ImageToken
from gamit.utils.sms import SMSManager
from gamit.timer.schedule import Scheduler
from gamit.mongodb.database import MongoDatabase
from application import Application

from optparse import OptionParser
from user.userentitymanager import UserEntityManager
from social.systopicmanager import SysTopicManager
from social.postmanager import PostManager
from background.loader import SystemCommandLoder

def loadEveryThing():
    """
    # load anything necessary before the server starts
    """
    UserEntityManager.loadAllUserBasics()
    UserEntityManager.loadAllUserBasics()
    SysTopicManager.loadSysTopics()
    PostManager.loadPosts()

def main():
    optParser = OptionParser()
    optParser.add_option("-c", "--channel-id", type="int", dest="channelId")
    options, args = optParser.parse_args()
    channelId = options.channelId or 0

    #load server configs
    ServerConfigManager.loadConfig()

    # start logger
    logDirName = "log/gate"
    if channelId > 0:
        logDirName = "{}-{}".format(logDirName, channelId)

    loggerDir = os.path.join(os.getcwd(), logDirName)
    Logger.startLogging(loggerDir, ServerConfigManager.isDebug)

    Logger.logInfo("loading configs...")
    staticdata.dataloader.loadConfigs()

    Logger.logInfo("Loading ImageToken Configs...")
    ImageToken.loadConfig()

    Logger.logInfo("Loading SMS Configs...")
    SMSManager.loadConfig()

    Logger.logInfo("Init db connection")
    connConfig = os.path.join(parent_dir, "config/dbcache_connection_config.xml")
    tableConfig = os.path.join(parent_dir, "staticdata/dbconfig/main_db_config.xml")
    if not MongoDatabase.loadConfig(connConfig, tableConfig):
        Logger.logInfo("DbCache", "Load MongoDatata Config Failed")
        return

    app = Application("Gate", channelId)

    Logger.logInfo("initiating app...")
    if app.init():
        Logger.logInfo("starting mongodb")
        if not MongoDatabase.start():
            Logger.logInfo("Starting mongoDb Failed")
            return

        Logger.logInfo("starting scheduler...")
        Scheduler.start()

        # load everty thing
        loadEveryThing()

        # sys command load
        Logger.logInfo("starting system command loader...")
        SystemCommandLoder.start()

        Logger.logInfo("starting app...")
        app.start()
    else:
        raise Exception("Initiating Application Failed.")

    Logger.logInfo("stopping app...")
    app.stop()

if __name__ == "__main__":
    main()
