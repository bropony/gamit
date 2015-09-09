#
# file: iloguseroper.py
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
import message.logdb.logconst
import message.logdb.logtables


class ILogUserOper_Loglogin_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ILogUserOper_Logsignup_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ILogUserOper_Logrefreshsystopic_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ILogUserOper_Logsystopicoper_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ILogUserOper_Logrefreshuserpost_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ILogUserOper_Loguserpostoper_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class ILogUserOper_Loglogin_Response(RmiResponseBase):
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


class ILogUserOper_Logsignup_Response(RmiResponseBase):
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


class ILogUserOper_Logrefreshsystopic_Response(RmiResponseBase):
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


class ILogUserOper_Logsystopicoper_Response(RmiResponseBase):
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


class ILogUserOper_Logrefreshuserpost_Response(RmiResponseBase):
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


class ILogUserOper_Loguserpostoper_Response(RmiResponseBase):
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


class ILogUserOperServant(RmiServant):
    def __init__(self, name='ILogUserOper'):
        super().__init__(name)
        self.methodMap['logLogin'] = self._logLogin
        self.methodMap['logSignup'] = self._logSignup
        self.methodMap['logRefreshSysTopic'] = self._logRefreshSysTopic
        self.methodMap['logSysTopicOper'] = self._logSysTopicOper
        self.methodMap['logRefreshUserPost'] = self._logRefreshUserPost
        self.methodMap['logUserPostOper'] = self._logUserPostOper

    def _logLogin(self, _connId, _msgId, _is):
        loginLog = message.logdb.logtables.TLogLogin()
        loginLog._read(_is)
        _request = ILogUserOper_Loglogin_Request(_connId, _msgId, self)
        self.logLogin(loginLog, _request)

    def _logSignup(self, _connId, _msgId, _is):
        signupLog = message.logdb.logtables.TLogSignup()
        signupLog._read(_is)
        _request = ILogUserOper_Logsignup_Request(_connId, _msgId, self)
        self.logSignup(signupLog, _request)

    def _logRefreshSysTopic(self, _connId, _msgId, _is):
        refreshLog = message.logdb.logtables.TLogRefreshSysTopic()
        refreshLog._read(_is)
        _request = ILogUserOper_Logrefreshsystopic_Request(_connId, _msgId, self)
        self.logRefreshSysTopic(refreshLog, _request)

    def _logSysTopicOper(self, _connId, _msgId, _is):
        logSysTopicOper = message.logdb.logtables.TLogSysTopicOper()
        logSysTopicOper._read(_is)
        _request = ILogUserOper_Logsystopicoper_Request(_connId, _msgId, self)
        self.logSysTopicOper(logSysTopicOper, _request)

    def _logRefreshUserPost(self, _connId, _msgId, _is):
        refreshLog = message.logdb.logtables.TLogRefreshUserPost()
        refreshLog._read(_is)
        _request = ILogUserOper_Logrefreshuserpost_Request(_connId, _msgId, self)
        self.logRefreshUserPost(refreshLog, _request)

    def _logUserPostOper(self, _connId, _msgId, _is):
        logUserPostOper = message.logdb.logtables.TLogUserPostOper()
        logUserPostOper._read(_is)
        _request = ILogUserOper_Loguserpostoper_Request(_connId, _msgId, self)
        self.logUserPostOper(logUserPostOper, _request)


    @abc.abstractmethod
    def logLogin(self, loginLog, _request):
        """
        :type loginLog: message.logdb.logtables.TLogLogin
        :type _request: message.logdb.iloguseroper.ILogUserOper_Loglogin_Request
        """
        pass

    @abc.abstractmethod
    def logSignup(self, signupLog, _request):
        """
        :type signupLog: message.logdb.logtables.TLogSignup
        :type _request: message.logdb.iloguseroper.ILogUserOper_Logsignup_Request
        """
        pass

    @abc.abstractmethod
    def logRefreshSysTopic(self, refreshLog, _request):
        """
        :type refreshLog: message.logdb.logtables.TLogRefreshSysTopic
        :type _request: message.logdb.iloguseroper.ILogUserOper_Logrefreshsystopic_Request
        """
        pass

    @abc.abstractmethod
    def logSysTopicOper(self, logSysTopicOper, _request):
        """
        :type logSysTopicOper: message.logdb.logtables.TLogSysTopicOper
        :type _request: message.logdb.iloguseroper.ILogUserOper_Logsystopicoper_Request
        """
        pass

    @abc.abstractmethod
    def logRefreshUserPost(self, refreshLog, _request):
        """
        :type refreshLog: message.logdb.logtables.TLogRefreshUserPost
        :type _request: message.logdb.iloguseroper.ILogUserOper_Logrefreshuserpost_Request
        """
        pass

    @abc.abstractmethod
    def logUserPostOper(self, logUserPostOper, _request):
        """
        :type logUserPostOper: message.logdb.logtables.TLogUserPostOper
        :type _request: message.logdb.iloguseroper.ILogUserOper_Loguserpostoper_Request
        """
        pass

# message.logdb.iloguseroper.ILogUserOperProxy
class ILogUserOperProxy(RmiProxy):
    def __init__(self, name='ILogUserOper'):
        super().__init__(name)

    def logLogin(self, _response, loginLog):
        """
        :type _response: ILogUserOper_Loglogin_Response
        :type loginLog: message.logdb.logtables.TLogLogin
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('logLogin')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        loginLog._write(_os)
        self.invoke(_os, _response)

    def logSignup(self, _response, signupLog):
        """
        :type _response: ILogUserOper_Logsignup_Response
        :type signupLog: message.logdb.logtables.TLogSignup
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('logSignup')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        signupLog._write(_os)
        self.invoke(_os, _response)

    def logRefreshSysTopic(self, _response, refreshLog):
        """
        :type _response: ILogUserOper_Logrefreshsystopic_Response
        :type refreshLog: message.logdb.logtables.TLogRefreshSysTopic
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('logRefreshSysTopic')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        refreshLog._write(_os)
        self.invoke(_os, _response)

    def logSysTopicOper(self, _response, logSysTopicOper):
        """
        :type _response: ILogUserOper_Logsystopicoper_Response
        :type logSysTopicOper: message.logdb.logtables.TLogSysTopicOper
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('logSysTopicOper')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        logSysTopicOper._write(_os)
        self.invoke(_os, _response)

    def logRefreshUserPost(self, _response, refreshLog):
        """
        :type _response: ILogUserOper_Logrefreshuserpost_Response
        :type refreshLog: message.logdb.logtables.TLogRefreshUserPost
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('logRefreshUserPost')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        refreshLog._write(_os)
        self.invoke(_os, _response)

    def logUserPostOper(self, _response, logUserPostOper):
        """
        :type _response: ILogUserOper_Loguserpostoper_Response
        :type logUserPostOper: message.logdb.logtables.TLogUserPostOper
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('logUserPostOper')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        logUserPostOper._write(_os)
        self.invoke(_os, _response)


