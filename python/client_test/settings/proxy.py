"""
* @name proxy.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 19:23
*
* @desc proxy.py
"""
from gamit.singleton.singleton import Singleton
from message.gate.ilogin import ILoginProxy
from message.gate.ipostoper import IPostOperProxy
from message.gate.iuserinfo import IUserInfoProxy
from message.gate.itest import ITestProxy

class ProxySetting(Singleton):
    @staticmethod
    def initGateProxy(client):
        client.addProxy(ILoginProxy())
        client.addProxy(IPostOperProxy())
        client.addProxy(IUserInfoProxy())
        client.addProxy(ITestProxy())
#