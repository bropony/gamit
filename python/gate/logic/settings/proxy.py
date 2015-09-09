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
from message.logdb.iloguseroper import ILogUserOperProxy

class ProxySetting(Singleton):

    @classmethod
    def initDbLogProxy(cls, client):
        client.addProxy(ILogUserOperProxy())
# ###
