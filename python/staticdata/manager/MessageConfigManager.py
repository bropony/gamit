"""
@author: mahanzhou
@date: 8/4/15
@file: 
@desc:

"""

from gamit.log.logger import Logger
from staticdata.loader.manager import *
from message.db.configs.TMessageConfig import SeqTMessageConfig

class __MessageConfigManager(ManagerBase):
    """
    :type data: dict[str, str]
    """
    def __init__(self):
        super().__init__(SeqTMessageConfig)

    def loadConfig(self, filepath):
        configs = loadfile(filepath, self.loader)
        self.data = {}

        for cfg in configs:
            self.data[cfg.msgKey] = cfg.msgContent

        return True

    def getMsg(self, msgKey, var=None):
        if not msgKey in self.data:
            return ""

        msgContent = self.data[msgKey]

        if isinstance(var, list) or isinstance(var, tuple):
            try:
                msgContent = msgContent.format(*var)
            except:
                Logger.log("Invalid vars for msgKey:", msgKey)

        return msgContent

MessageConfigManager = __MessageConfigManager()
