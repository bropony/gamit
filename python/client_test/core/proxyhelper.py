"""
@author: mahanzhou
@date: 8/26/15
@file: 
@desc:

"""

import gamit.app.apptype as AppType
from gamit.rmi.proxymanager import ProxyManager
from message.gate.itest import ITestProxy
from message.gate.ipostoper import IPostOperProxy
from message.gate.iuserinfo import IUserInfoProxy
from message.gate.ilogin import ILoginProxy

class ProxyHelper:
    @staticmethod
    def getITestProxy():
        """
        :rtype: ITestProxy
        """
        return ProxyManager.getProxy(AppType.GATE, "ITest")

    @staticmethod
    def getIPostOperProxy():
        """
        :rtype: IPostOperProxy
        """
        return ProxyManager.getProxy(AppType.GATE, "IPostOper")

    @staticmethod
    def getIUserInfoProxy():
        """
        :rtype: IUserInfoProxy
        """

        return ProxyManager.getProxy(AppType.GATE, "IUserInfo")

    @staticmethod
    def getILoginProxy():
        """
        :rtype: ILoginProxy
        """

        return ProxyManager.getProxy(AppType.GATE, "ILogin")
