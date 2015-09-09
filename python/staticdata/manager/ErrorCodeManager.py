"""
* @name ErrorCodeManager.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/11 14:48
*
* @desc ErrorCodeManager.py
"""

from gamit.log.logger import Logger
from staticdata.loader.manager import *
from message.db.configs.TErrorConfig import SeqTErrorConfig

class __ErrorCodeManager(ManagerBase):
    def __init__(self):
        super().__init__(SeqTErrorConfig)

    def loadConfig(self, filepath):
        configs = loadfile(filepath, self.loader)
        self.data = {}

        for config in configs:
            self.data[config.errorName] = config

        return True

    def findErrorConfig(self, errorName):
        """
        :rtype message.db.configs.TErrorConfig.TErrorConfig
        """
        return self.data.get(errorName)

    def raiseError(self, errorName):
        if errorName not in self.data:
            Logger.log("Unknown Error: " + errorName)
            raise Exception(errorName, 0)

        config = self.data[errorName]
        raise Exception(config.errorStr, config.errorCode)

    def getError(self, errorName):
        """
        :rtype Exception
        """
        if errorName not in self.data:
            return Exception(errorName, 0)

        config = self.data[errorName]
        return Exception(config.errorStr, config.errorCode)

# manager instance
ErrorCodeManager = __ErrorCodeManager()
