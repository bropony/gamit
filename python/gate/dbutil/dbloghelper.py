"""
@author: mahanzhou
@date: 8/8/15
@file: 
@desc:

"""

import gamit.rmi.proxymanager
import gamit.app.apptype
from message.logdb.logtables import *
from message.logdb.logconst import ELogPostOperType
from message.logdb.iloguseroper import ILogUserOperProxy

class DbLogHepler:
    @classmethod
    def getDbProxy(cls, name):
        dbProxy = gamit.rmi.proxymanager.ProxyManager.getProxy(
            gamit.app.apptype.DBLOG, name)

        return dbProxy

    @classmethod
    def getILogUserOperProxy(cls):
        """
        :rtype: ILogUserOperProxy
        """
        return cls.getDbProxy("ILogUserOper")

    @classmethod
    def logLogin(cls, logUserInfo):
        """
        :type logUserInfo: SLogUserInfo
        """
        log = TLogLogin()
        log.userInfo = logUserInfo
        cls.getILogUserOperProxy().logLogin(None, log)

    @classmethod
    def logSignup(cls, logUserInfo):
        """
        :type logUserInfo: SLogUserInfo
        """
        log = TLogSignup()
        log.userInfo = logUserInfo
        cls.getILogUserOperProxy().logSignup(None, log)

    @classmethod
    def logRefreshSysTopic(cls, logUserInfo, tags):
        """
        :type logUserInfo: SLogUserInfo
        """

        log = TLogRefreshSysTopic()
        log.userInfo = logUserInfo
        log.tags = tags
        cls.getILogUserOperProxy().logRefreshSysTopic(None, logUserInfo)

    @classmethod
    def logSysTopicOper(cls, logUserInfo, topicId, operType):
        """
        :type logUserInfo: SLogUserInfo
        :type operType: ELogPostOperType
        """

        log = TLogSysTopicOper()
        log.userInfo = logUserInfo
        log.topicId = topicId
        log.operType = operType
        cls.getILogUserOperProxy().logSysTopicOper(None, log)

    @classmethod
    def logRefreshUserPost(cls, logUserInfo, tags):
        """
        :type logUserInfo: SLogUserInfo
        """

        log = TLogRefreshUserPost()
        log.userInfo = logUserInfo
        log.tags = tags
        cls.getILogUserOperProxy().logRefreshUserPost(None, log)

    @classmethod
    def logUserPostOper(cls, logUserInfo, postId, operType):
        """
        :type logUserInfo: SLogUserInfo
        :type operType: ELogPostOperType
        """
        log = TLogUserPostOper()
        log.userInfo = logUserInfo
        log.postId = postId
        log.operType = operType

        cls.getILogUserOperProxy().logUserPostOper(None, log)
