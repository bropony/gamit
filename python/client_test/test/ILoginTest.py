"""
@author: mahanzhou
@date: 8/4/15
@file: 
@desc:

"""

from gamit.log.logger import Logger
from gamit.rmi.proxymanager import ProxyManager
import gamit.app.apptype as apptype
from gamit.utils.myuuid import MyUuid

import message.gate.ilogin as ilogin
import message.gate.gatemsg as gatemsg
import message.common.publicdef as publicdef

class ILoginGetphonesignupvalidationcodeResponse(ilogin.ILogin_Getphonesignupvalidationcode_Response):
    def onResponse(self):
        Logger.log("ILoginGetphonesignupvalidationcodeResponse.onResponse")

    def onTimeout(self):
        Logger.log("ILoginGetphonesignupvalidationcodeResponse.onTimeout")

    def onError(self, what, code):
        Logger.log("ILoginGetphonesignupvalidationcodeResponse.onError:", what, ", code:", code)

class ILoginLoginResponse(ilogin.ILogin_Login_Response):
    def onResponse(self, loginRes):
        """
        :type loginRes: message.gate.gatemsg.SLoginReturn
        """
        Logger.log("ILoginLoginResponse.onResponse: ", loginRes.userId)

    def onTimeout(self):
        Logger.log("ILoginLoginResponse.onTimeout")

    def onError(self, what, code):
        Logger.log("ILoginLoginResponse.onError:", what, ", code:", code)

class ILoginSignupResponse(ilogin.ILogin_Signup_Response):
    def onResponse(self, signupRes):
        """
        :type signupRes: message.gate.gatemsg.SLoginReturn
        """
        Logger.log("ILoginSignupResponse.onResponse: ", signupRes.userId)

    def onError(self, what, code):
        Logger.log("ILoginSignupResponse.onError:", what, ", code:", code)

    def onTimeout(self):
        Logger.log("ILoginLoginResponse.onTimeout")

def getPhoneValidationCodeTest(proxy):
    response = ILoginGetphonesignupvalidationcodeResponse()
    deviceCode = "WhatTheHell"
    phoneNum = "18028663328"

    Logger.log("query for validation code")
    proxy.getPhoneSignupValidationCode(response, deviceCode, phoneNum)

def loginTest(proxy):
    """
    :type proxy: message.gate.ilogin.ILoginProxy
    """
    loginInf = gatemsg.SLogin()
    loginInf.account = "18672060456"
    loginInf.loginType = publicdef.ELoginType.MobilePhoneNum
    loginInf.deviceCode = MyUuid.getUuid()
    loginInf.password = "123456"

    Logger.log("Login as", loginInf.account)
    proxy.login(ILoginLoginResponse(), loginInf)

def sigunupTest(proxy):
    """
    :type proxy: message.gate.ilogin.ILoginProxy
    """

    signupInfo = gatemsg.SSignup()
    signupInfo.deviceCode = MyUuid.getUuid()
    signupInfo.account = "12311111111"
    signupInfo.loginType = publicdef.ELoginType.MobilePhoneNum
    signupInfo.password = "123456"
    signupInfo.validationCode = "556688"
    signupInfo.nickname = "ahda"

    Logger.log("signup as", signupInfo.account)
    proxy.signup(ILoginSignupResponse(), signupInfo)

def runILoginTest():
    proxy = ProxyManager.getProxy(apptype.GATE, "ILogin")

    getPhoneValidationCodeTest(proxy)
    #loginTest(proxy)
    #sigunupTest(proxy)

