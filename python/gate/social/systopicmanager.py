"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:

"""

import datetime
from staticdata.serverconfig import ServerConfigManager
from social.systopic import WSysTopic
from message.db.mongodb.posttables import TSysTopic
from message.gate.gatemsg import SSysTopic, SeqSysTopic
from gamit.mongodb.database import MongoDatabase
from gamit.log.logger import Logger

class __SysTopicManager:
    """
    :type __topicMap: dict[str, WSysTopic]
    :type __sortedByDt: list[WSysTopic]
    """
    def __init__(self):
        self.__maxTargetNum = 20

        self.__topicMap = {}
        self.__sortedByDt = []

        if not ServerConfigManager.isDebug:
            self.__maxCachedNum = 100000
        else:
            self.__maxCachedNum = 20

    def loadSysTopics(self):
        if self.__topicMap:
            return

        tb = MongoDatabase.findTableByMessageType(TSysTopic)
        if not tb:
            Logger.log("Table TSysTopic not found")
            return

        sysTopicList = tb.findManyWithQuey(query={}, sort=MongoDatabase.SortByIdDesc, limit=self.__maxCachedNum)
        for topic in sysTopicList:
            wst = WSysTopic(topic)
            self.__topicMap[topic.topicId] = wst
            self.__sortedByDt.append(wst)

        Logger.log("Num of TSysTopic Loaded: ", len(sysTopicList))

    def addNewSysTopics(self, sysTopics):
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

        newSortedList.extend(self.__sortedByDt)
        if len(newSortedList) > self.__maxCachedNum:
            self.__sortedByDt = newSortedList[: self.__maxCachedNum]
        else:
            self.__sortedByDt = newSortedList

    def getLatestTopic(self, tag, thresholdDt, targetNum, imgFormat):
        """
        :type tag: str
        :type thresholdDt: datetime.datetime
        :type targetNum: int
        :type imgFormat: str
        :rtype: list[SSysTopic]
        """

        targetNum = targetNum if (targetNum <= self.__maxTargetNum) else self.__maxTargetNum
        res = SeqSysTopic()

        if thresholdDt < datetime.datetime.now():
            for topic in self.__sortedByDt:
                if topic.getCreateDt() > thresholdDt:
                    if topic.isTagMatched(tag):
                        res.append(topic.getClientInfo(imgFormat))
                else:
                    break
                if len(res) >= targetNum:
                    break
        else:
            for topic in self.__sortedByDt:
                if topic.isTagMatched(tag):
                    res.append(topic.getClientInfo(imgFormat))

                if len(res) >= targetNum:
                    break

        # print("getLatestTopic", tag, thresholdDt, targetNum)

        return res

    def getOlderSysTopicInDateOrder(self, tag, thresholdDt, targetNum, imgFormat):
        """
        :type tag: str
        :type thresholdDt: datetime.datetime
        :type targetNum: int
        :rtype: SeqSysTopic
        """

        targetNum = targetNum if (targetNum <= self.__maxTargetNum) else self.__maxTargetNum
        res = SeqSysTopic()

        for topic in self.__sortedByDt:
            if thresholdDt > topic.getCreateDt():
                if topic.isTagMatched(tag):
                    res.append(topic.getClientInfo(imgFormat))

                if len(res) >= targetNum:
                    break

        resSize = len(res)
        if resSize >= targetNum:
            return res

        # retrieve those not cached from DB
        thresholdDt = thresholdDt if (resSize == 0) else res[-1].createDt
        limit = targetNum - resSize
        sysTopicListFromDb = []
        tb = MongoDatabase.findTableByMessageType(TSysTopic)
        if tb:
            query = {TSysTopic.fn_createDt: {"$lt": thresholdDt}}
            if tag:
                query[TSysTopic.fn_tags] = tag

            sysTopicListFromDb = tb.findManyWithQuey(query,
                                                     limit=limit,
                                                     sort=MongoDatabase.SortByIdDesc)

        for tSysTopic in sysTopicListFromDb:
            wSysTopic = WSysTopic(tSysTopic)
            res.append(wSysTopic.getClientInfo(imgFormat))

        return res

    def getSysTopicByTopicId(self, topicId):
        """
        :type topicId: str
        :rtype: WSysTopic
        """
        if topicId in self.__topicMap:
            return self.__topicMap[topicId]

        tb = MongoDatabase.findTableByMessageType(TSysTopic)
        if tb:
            tSysTopic = tb.findOne(topicId)
            if tSysTopic:
                return WSysTopic(tSysTopic)

        return None

SysTopicManager = __SysTopicManager()
