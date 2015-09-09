__author__ = 'mahanzhou'

from dbcallback.userdbcallback import IUserDbLoaduserbasicResponse
from gamit.app import apptype
from gamit.rmi.proxymanager import ProxyManager
from gamit.utils.mydate import MyDate

from logic.settings.proxy import ProxySetting
from gamit.log.logger import Logger

class UserDataLoader:
    loaded = False

    @classmethod
    def loadUserInfos(cls):
        if cls.loaded:
            return

        Logger.log("UserDataLoader.loadUserInfos...")
        proxy = ProxyManager.getProxy(apptype.DBCACHE, ProxySetting.IUserDbProxyName)
        if proxy:
            proxy.loadUserBasic(IUserDbLoaduserbasicResponse(), MyDate.getFairyDt(), 5000)

        cls.loaded = True
##
