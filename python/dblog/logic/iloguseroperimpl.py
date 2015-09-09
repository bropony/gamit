"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:

"""

from message.logdb.iloguseroper import ILogUserOperServant
from gamit.mongodb.database import MongoDatabase

def saveLog(logs):
    if not isinstance(logs, list) and not isinstance(logs, tuple):
            logs = [logs]

    if not logs:
        return

    table = MongoDatabase.findTableByMessageObj(logs[0])
    table.save(logs)


class ILogUserOperImpl(ILogUserOperServant):
    def logLogin(self, loginLog, _request):
        """
        :type loginLog: message.logdb.logtables.TLogLogin
        :type _request: message.logdb.iloguseroper.ILogUserOper_Loglogin_Request
        """
        saveLog(loginLog)
        _request.response()

    def logSignup(self, signupLog, _request):
        """
        :type signupLog: message.logdb.logtables.TLogSignup
        :type _request: message.logdb.iloguseroper.ILogUserOper_Logsignup_Request
        """
        saveLog(signupLog)
        _request.response()

    def logRefreshSysTopic(self, refreshLog, _request):
        """
        :type refreshLog: message.logdb.logtables.TLogRefreshSysTopic
        :type _request: message.logdb.iloguseroper.ILogUserOper_Logrefreshsystopic_Request
        """
        saveLog(refreshLog)
        _request.response()

    def logSysTopicOper(self, logSysTopicOper, _request):
        """
        :type logSysTopicOper: message.logdb.logtables.TLogSysTopicOper
        :type _request: message.logdb.iloguseroper.ILogUserOper_Logsystopicoper_Request
        """
        saveLog(logSysTopicOper)
        _request.response()

    def logRefreshUserPost(self, refreshLog, _request):
        """
        :type refreshLog: message.logdb.logtables.TLogRefreshUserPost
        :type _request: message.logdb.iloguseroper.ILogUserOper_Logrefreshuserpost_Request
        """
        saveLog(refreshLog)
        _request.response()

    def logUserPostOper(self, logUserOpostOper, _request):
        """
        :type logUserOpostOper: message.logdb.logtables.TLogUserPostOper
        :type _request: message.logdb.iloguseroper.ILogUserOper_Loguserpostoper_Request
        """
        saveLog(logUserOpostOper)
        _request.response()

