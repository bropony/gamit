"""
@author: mahanzhou
@date: 8/25/15
@file: 
@desc:

"""

import message.gate.itest
from message.db.mongodb.posttables import TSysTopic
from message.gate.gatemsg import SSysTopic
from resources.systopicmanager import SysTopicManager
from gamit.utils.myuuid import MyUuid
from helpers.dbcachehelper import DbCacheHelper

class Test:
    """
    :type a: int
    :type b: str
    """
    def __init__(self):
        self.a = 10
        self.b = "test"

    __slots__ = dict()
    __slots__["a"] = int
    __slots__["b"] = str

class ITestImpl(message.gate.itest.ITestServant):
    def __init__(self):
        super().__init__()

    def addSysTopic(self, newSysTopic, _request):
        """
        :type newSysTopic: message.gate.gatemsg.SSysTopic
        :type _request: message.gate.itest.ITest_Addsystopic_Request
        """

        tSysTopic = TSysTopic()
        tSysTopic.topicId = MyUuid.getUuid()
        tSysTopic.topicType = newSysTopic.topicType
        tSysTopic.publisherId = newSysTopic.publisherId
        tSysTopic.title = newSysTopic.title
        tSysTopic.content = newSysTopic.content

        for imgToken in newSysTopic.images:
            tSysTopic.imageKeys.append(imgToken.imageKey)

        tSysTopic.tags.extend(newSysTopic.tags)

        SysTopicManager.addSysTopics([tSysTopic], False)

        _request.response()

        DbCacheHelper.getITableSaverProxy().updateTSysTopic(None, tSysTopic)

