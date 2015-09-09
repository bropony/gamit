__author__ = 'mahanzhou'


from gamit.log.logger import Logger
from staticdata.loader.manager import ManagerBase, loadfile
from message.db.configs.TConstConfig import SeqTConstConfig

class _ConstValue:
    def __init__(self, intVal, strVal):
        self.intVal = intVal
        self.strVal = strVal


class __ConstValueManager(ManagerBase):
    def __init__(self):
        super().__init__(SeqTConstConfig)

    def loadConfig(self, filepath):
        configs = loadfile(filepath, self.loader)

        self.data = {}

        for cfg in configs:
            self.data[cfg.constName] = _ConstValue(cfg.intValue, cfg.strValue)

        return True

    def getValues(self, constName):
        """
        :rtype: (int, str)
        """

        if constName in self.data:
            val = self.data[constName]

            return (val.intVal, val.strVal)

        return ()

    def getIntValue(self, constName):
        """
        :rtype: int
        """

        if constName in self.data:
            return self.data[constName].intVal

        return 0

    def getStrValue(self, constName):
        """
        :rtype: str
        """

        if constName in self.data:
            return self.data[constName].strVal

        return ""

# singleton
ConstValueManager = __ConstValueManager()
###
