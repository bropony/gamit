"""
@author: mahanzhou
@date: 8/26/15
@file: 
@desc:

"""

from gamit.log.logger import Logger
from staticdata.loader.manager import loadfile, ManagerBase
from message.db.configs.TTopicTag import TTopicTag, SeqTTopicTag

class __TopicTagConfigManager(ManagerBase):
    """
    :type data: dict[int, TTopicTag]
    """
    def __init__(self):
        super().__init__(SeqTTopicTag)

    def loadConfig(self, filepath):
        configs = loadfile(filepath, self.loader)

        self.data = {}
        for cnf in configs:
            self.data[cnf.tagId] = cnf

        return True

    def getTagNameByTagId(self, tagId):
        """
        :type tagId: int|str
        :rtype: str
        """

        if isinstance(tagId, str):
            if tagId.isdigit():
                tagId = int(tagId)

        if not tagId:
            return ""

        if tagId in self.data:
            return self.data[tagId].tagName

        return tagId

    def getTagNamesByTagIdList(self, idList):
        """
        :type idList: list[int]
        :rtype: list[str]
        """

        res = []

        for tagId in idList:
            res.append(self.getTagNameByTagId(tagId))

        return res

TopicTagConfigManager = __TopicTagConfigManager()
