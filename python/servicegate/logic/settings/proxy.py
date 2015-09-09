"""
* @name proxy.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/3 19:47
*
* @desc proxy.py
"""

from gamit.singleton.singleton import Singleton
from message.db.ilogindb import ILoginDbProxy
from message.db.iuserdb import IUserDbProxy
from message.db.itablesaver import ITableSaverProxy

from message.logdb.iloguseroper import ILogUserOperProxy

class ProxySetting(Singleton):
    ILoginDbProxyName = "ILoginDb"
    IUserDbProxyName = "IUserDb"
    ITableSaverProxyName = "ITableSaver"

    @classmethod
    def initDbCacheProxy(cls, client):
        client.addProxy(ILoginDbProxy())
        client.addProxy(IUserDbProxy())
        client.addProxy(ITableSaverProxy())

    @classmethod
    def initDbLogProxy(cls, client):
        client.addProxy(ILogUserOperProxy())
# ###
