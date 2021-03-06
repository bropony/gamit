"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:

"""

import os
import sys

# add parent dir to searching paths
main_dir, _ = os.path.split(__file__)
parent_dir, _ = os.path.split(main_dir)
sys.path.append(parent_dir)

import staticdata.dataloader
from staticdata.serverconfig import ServerConfigManager
from gamit.log.logger import Logger
from gamit.mongodb.database import MongoDatabase

from application import Application

def main():
    #load server configs
    ServerConfigManager.loadConfig()

    # start logger
    loggerDir = os.path.join(os.getcwd(), "log/DbLog")
    Logger.startLogging(loggerDir, ServerConfigManager.isDebug)

    Logger.logInfo("loading configs...")
    if not staticdata.dataloader.loadConfigs():
        return

    Logger.logInfo("Init db connection")
    connConfig = os.path.join(parent_dir, "config/dblog_connection_config.xml")
    tableConfig = os.path.join(parent_dir, "staticdata/dbconfig/log_db_config.xml")
    if not MongoDatabase.loadConfig(connConfig, tableConfig):
        Logger.logInfo("DbCache", "Load MongoDatata Config Failed")
        return

    app = Application("DbCache")

    Logger.logInfo("initiating app...")
    if app.init():
        Logger.logInfo("starting mongodb")
        if not MongoDatabase.start():
            Logger.logInfo("Starting mongoDb Failed")
            return

        Logger.logInfo("starting app...")
        app.start()
    else:
        raise Exception("Initiating Application Failed.")

    Logger.logInfo("stopping app...")
    app.stop()

if __name__ == "__main__":
    main()