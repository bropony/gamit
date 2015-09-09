"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:

"""

import datetime
from resources.systopic import WSysTopic
from message.gate.gatemsg import SSysTopic, SeqSysTopic

class __SysTopicManager:
    """
    :type __topicMap: dict[str, WSysTopic]
    :type __sortedByDt: list[WSysTopic]
    """
    def __init__(self):
        self.__maxTargetNum = 20

        self.__topicMap = {}
        self.__sortedByDt = []
        self.__maxCachedNum = 10000

    def addSysTopics(self, sysTopics, pushBack):
        """
        :type sysTopics: list[message.db.mongodb.posttables.TSysTopic]
        :type pushBack: bool
        """

        newSortedList = []
        for topic in sysTopics:
            if topic.topicId not in self.__topicMap:
                wst = WSysTopic(topic)
                self.__topicMap[topic.topicId] = wst
                newSortedList.append(wst)

        if pushBack:
            self.__sortedByDt.extend(newSortedList)
        else:
            newSortedList.extend(self.__sortedByDt)
            self.__sortedByDt = newSortedList

    def sortTopics(self):
        self.__sortedByDt.sort(key=lambda x: x.getTSysTopic().createDt)

    def getTopicNum(self):
        """
        :rtype: int
        """
        return len(self.__sortedByDt)

    def isCacheFull(self):
        """
        :rtype: bool
        """
        return (self.__maxCachedNum <= len(self.__sortedByDt))

    def getLatestTopic(self, tag, thresholdDt, targetNum, imgFormat):
        """
        :type tag: str
        :type thresholdDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        :rtype: list[SSysTopic]
        """

        targetNum = targetNum if targetNum <= self.__maxCachedNum else self.__maxCachedNum
        res = SeqSysTopic()

        if thresholdDt < datetime.datetime.now():
            for post in self.__sortedByDt:
                if post.getCreateDt() > thresholdDt:
                    res.append(post.getClientInfo(imgFormat))
                else:
                    break
                if len(res) >= targetNum:
                    break
        else:
            for post in self.__sortedByDt:
                res.append(post.getClientInfo(imgFormat))

                if len(res) >= targetNum:
                    break

        return res

    def getOlderSysTopicInDateOrder(self, tag, thresholdDt, targetNum, imgFormat):
        """
        :type tag: str
        :type thresholdDt: datetime.datetime
        :type targetNum: int
        :rtype: SeqSysTopic
        """

        targetNum = targetNum if targetNum <= self.__maxCachedNum else self.__maxCachedNum
        res = SeqSysTopic()

        for post in self.__sortedByDt:
            if thresholdDt > post.getCreateDt():
                res.append(post.getClientInfo(imgFormat))
                if len(res) >= targetNum:
                    break
        return res

    def getSysTopicByTopicId(self, topicId):
        if topicId in self.__topicMap:
            return self.__topicMap[topicId]

        return None


SysTopicManager = __SysTopicManager()
