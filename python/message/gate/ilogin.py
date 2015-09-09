#
# file: ilogin.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *
from gamit.rmi.rmicore import *
from gamit.serialize.serializer import Serializer
from gamit.serialize.datatype import RmiDataType
import abc
import message.common.publicdef
import message.common.publicmsg
import message.gate.gateconst
import message.gate.gatemsg


class ILogin_Getphonesignupvalidationcode_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ILogin_Login_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, loginRes):
        if not isinstance(loginRes, message.gate.gatemsg.SLoginReturn):
            raise Exception("loginRes must be instance of message.gate.gatemsg.SLoginReturn", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        loginRes._write(_os)

        self.sendout()

class ILogin_Signup_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, signupRes):
        if not isinstance(signupRes, message.gate.gatemsg.SLoginReturn):
            raise Exception("signupRes must be instance of message.gate.gatemsg.SLoginReturn", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        signupRes._write(_os)

        self.sendout()

class ILogin_Getpasswordresetvalidationcode_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ILogin_Resetphoneuserpassword_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ILogin_Getphonesignupvalidationcode_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ILogin_Login_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        loginRes = message.gate.gatemsg.SLoginReturn()
        loginRes._read(_is)

        self.onResponse(loginRes)

    @abc.abstractmethod
    def onResponse(self, loginRes):
        """
        :type loginRes: message.gate.gatemsg.SLoginReturn
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ILogin_Signup_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        signupRes = message.gate.gatemsg.SLoginReturn()
        signupRes._read(_is)

        self.onResponse(signupRes)

    @abc.abstractmethod
    def onResponse(self, signupRes):
        """
        :type signupRes: message.gate.gatemsg.SLoginReturn
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ILogin_Getpasswordresetvalidationcode_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ILogin_Resetphoneuserpassword_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ILoginServant(RmiServant):
    def __init__(self, name='ILogin'):
        super().__init__(name)
        self.methodMap['getPhoneSignupValidationCode'] = self._getPhoneSignupValidationCode
        self.methodMap['login'] = self._login
        self.methodMap['signup'] = self._signup
        self.methodMap['getPasswordResetValidationCode'] = self._getPasswordResetValidationCode
        self.methodMap['resetPhoneUserPassword'] = self._resetPhoneUserPassword

    def _getPhoneSignupValidationCode(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        phoneNum = str()
        phoneNum = _is.readString()
        _request = ILogin_Getphonesignupvalidationcode_Request(_connId, _msgId, self)
        self.getPhoneSignupValidationCode(deviceCode, phoneNum, _request)

    def _login(self, _connId, _msgId, _is):
        loginInfo = message.gate.gatemsg.SLogin()
        loginInfo._read(_is)
        _request = ILogin_Login_Request(_connId, _msgId, self)
        self.login(loginInfo, _request)

    def _signup(self, _connId, _msgId, _is):
        signupInfo = message.gate.gatemsg.SSignup()
        signupInfo._read(_is)
        _request = ILogin_Signup_Request(_connId, _msgId, self)
        self.signup(signupInfo, _request)

    def _getPasswordResetValidationCode(self, _connId, _msgId, _is):
        deviceCode = str()
        deviceCode = _is.readString()
        phoneNum = str()
        phoneNum = _is.readString()
        _request = ILogin_Getpasswordresetvalidationcode_Request(_connId, _msgId, self)
        self.getPasswordResetValidationCode(deviceCode, phoneNum, _request)

    def _resetPhoneUserPassword(self, _connId, _msgId, _is):
        phoneNum = str()
        phoneNum = _is.readString()
        validationCode = str()
        validationCode = _is.readString()
        newPassword = str()
        newPassword = _is.readString()
        _request = ILogin_Resetphoneuserpassword_Request(_connId, _msgId, self)
        self.resetPhoneUserPassword(phoneNum, validationCode, newPassword, _request)


    @abc.abstractmethod
    def getPhoneSignupValidationCode(self, deviceCode, phoneNum, _request):
        """
        :type deviceCode: str
        :type phoneNum: str
        :type _request: message.gate.ilogin.ILogin_Getphonesignupvalidationcode_Request
        """
        pass

    @abc.abstractmethod
    def login(self, loginInfo, _request):
        """
        :type loginInfo: message.gate.gatemsg.SLogin
        :type _request: message.gate.ilogin.ILogin_Login_Request
        """
        pass

    @abc.abstractmethod
    def signup(self, signupInfo, _request):
        """
        :type signupInfo: message.gate.gatemsg.SSignup
        :type _request: message.gate.ilogin.ILogin_Signup_Request
        """
        pass

    @abc.abstractmethod
    def getPasswordResetValidationCode(self, deviceCode, phoneNum, _request):
        """
        :type deviceCode: str
        :type phoneNum: str
        :type _request: message.gate.ilogin.ILogin_Getpasswordresetvalidationcode_Request
        """
        pass

    @abc.abstractmethod
    def resetPhoneUserPassword(self, phoneNum, validationCode, newPassword, _request):
        """
        :type phoneNum: str
        :type validationCode: str
        :type newPassword: str
        :type _request: message.gate.ilogin.ILogin_Resetphoneuserpassword_Request
        """
        pass

# message.gate.ilogin.ILoginProxy
class ILoginProxy(RmiProxy):
    def __init__(self, name='ILogin'):
        super().__init__(name)

    def getPhoneSignupValidationCode(self, _response, deviceCode, phoneNum):
        """
        :type _response: ILogin_Getphonesignupvalidationcode_Response
        :type deviceCode: str
        :type phoneNum: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getPhoneSignupValidationCode')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(phoneNum)
        self.invoke(_os, _response)

    def login(self, _response, loginInfo):
        """
        :type _response: ILogin_Login_Response
        :type loginInfo: message.gate.gatemsg.SLogin
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('login')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        loginInfo._write(_os)
        self.invoke(_os, _response)

    def signup(self, _response, signupInfo):
        """
        :type _response: ILogin_Signup_Response
        :type signupInfo: message.gate.gatemsg.SSignup
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('signup')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        signupInfo._write(_os)
        self.invoke(_os, _response)

    def getPasswordResetValidationCode(self, _response, deviceCode, phoneNum):
        """
        :type _response: ILogin_Getpasswordresetvalidationcode_Response
        :type deviceCode: str
        :type phoneNum: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getPasswordResetValidationCode')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(deviceCode)
        _os.writeString(phoneNum)
        self.invoke(_os, _response)

    def resetPhoneUserPassword(self, _response, phoneNum, validationCode, newPassword):
        """
        :type _response: ILogin_Resetphoneuserpassword_Response
        :type phoneNum: str
        :type validationCode: str
        :type newPassword: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('resetPhoneUserPassword')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(phoneNum)
        _os.writeString(validationCode)
        _os.writeString(newPassword)
        self.invoke(_os, _response)


