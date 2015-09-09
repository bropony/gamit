__author__ = 'mahanzhou'

import message.db.iuserdb as iuserdb
import message.db.ilogindb as ilogindb
import message.db.itablesaver as itablesave

import datetime

from gamit.rmi.proxymanager import ProxyManager
from gamit.app import apptype
from gamit.log.logger import Logger
from gamit.timer.timerbase import TimerBase
from gamit.timer.schedule import Scheduler
from gamit.utils.myuuid import MyUuid

from staticdata.manager.ErrorCodeManager import ErrorCodeManager
from user.userentity import UserEntity
from user.userentitymanager import UserEntityManager
from logic.settings.proxy import ProxySetting
from logic.connection.connectioninfo import ConnectionInfo

from helpers.dbloghelper import DbLogHepler
from helpers.dbcachehelper import DbCacheHelper

class _LoadUserBasicTimer(TimerBase):
    def __init__(self, callback, dateLimit):
        super().__init__()

        self.callback = callback
        self.dateLimit = dateLimit

    def handleTimeout(self, data):
        proxy = ProxyManager.getProxy(apptype.DBCACHE, ProxySetting.IUserDbProxyName)
        if proxy:
            proxy.loadUserBasic(self.callback, self.dateLimit, 5000)


class IUserDbLoaduserbasicResponse(iuserdb.IUserDb_Loaduserbasic_Response):
    def __init__(self):
        super().__init__()
        self.dtLmt = datetime.datetime(2000, 1, 1, 0, 0, 0)

    def onResponse(self, isAllDataLoaded, userBasics):
        """
        :type isAllDataLoaded: bool
        :type userBasics: message.db.mongodb.usertables.SeqTUserBasic
        """

        Logger.log("IUserDbLoaduserbasicResponse.onResponse", "User Loaded:", len(userBasics))

        UserEntityManager.addUserBasics(userBasics)
        if not isAllDataLoaded and len(userBasics):
            proxy = ProxyManager.getProxy(apptype.DBCACHE, ProxySetting.IUserDbProxyName)
            if proxy:
                self.dtLmt = userBasics[-1].createDt
                proxy.loadUserBasic(self, self.dtLmt, 5000)
            else:
                Logger.log("IUserDbLoaduserbasicResponse.onResponse:",
                           "Proxy Not Found: ", ProxySetting.IUserDbProxyName)

        if isAllDataLoaded:
            ConnectionInfo.setUserDataLoaded(True)

    def onError(self, what, code):
        Logger.log("IUserDbLoaduserbasicResponse.onError:", what, ", ", code)
        raise Exception("Load User Data failed")

    def onTimeout(self):
        Logger.log("IUserDbLoaduserbasicResponse.onTimeout")

        timer = _LoadUserBasicTimer(self, self.dtLmt)

        # retry after 10secs
        Scheduler.schedule(timer, None, 10, 0)

class IUserDbLoaduserdataviewResponse(iuserdb.IUserDb_Loaduserdataview_Response):
    """
    :type userEntity: UserEntity
    """
    def __init__(self, userEntity, request, deviceCode):
        super().__init__()

        self.userEntity = userEntity
        self.request = request
        self.deviceCode = deviceCode

    def onResponse(self, userDataView):
        """
        :type userDataView: message.db.dataview.SUserDataView
        """

        sessionKey = MyUuid.getUuid()
        self.userEntity.updateUserData(userDataView)
        self.userEntity.updateDeviceCodeAndSessionKey(self.deviceCode, sessionKey)
        self.request.response(self.userEntity.getLoginReturn())

        UserEntityManager.onUserLogin(self.userEntity, self.request.connId, self.deviceCode)

        # save changes
        DbCacheHelper.getITableSaverProxy().updateTUserSettings(None, self.userEntity.getTUserSettings())

        # logging
        DbLogHepler.logLogin(self.userEntity.getLogUserInfo())

    def onError(self, what, code):
        Logger.log("IUserDbLoaduserdataviewResponse.onError:", what, ", ", code)
        self.request.error(what, code)

    def onTimeout(self):
        Logger.log("IUserDbLoaduserdataviewResponse.onTimeout")
        self.request.error(ErrorCodeManager.getError("ErrorLogin_loginOperTimeout"))

class ILoginDbCreateaccountResponse(ilogindb.ILoginDb_Createaccount_Response):
    def __init__(self, request, deviceCode):
        super().__init__()
        self.request = request
        self.deviceCode = deviceCode

    def onResponse(self, dataView):
        """
        :type dataView: message.db.dataview.SUserDataView
        """

        userEntity = UserEntity(dataView.basicInfo)
        userEntity.updateUserData(dataView)

        UserEntityManager.addUser(userEntity)

        userEntity.updateDeviceCodeAndSessionKey(self.deviceCode, MyUuid.getUuid())
        UserEntityManager.onUserLogin(userEntity, self.request.connId, self.deviceCode)

        self.request.response(userEntity.getLoginReturn())

        # save changes
        DbCacheHelper.getITableSaverProxy().updateTUserSettings(None, userEntity.getTUserSettings())
        # logging
        DbLogHepler.logSignup(userEntity.getLogUserInfo())

    def onError(self, what, code):
        Logger.log("ILoginDbCreateaccountResponse.onError:", what, ", ", code)
        self.request.error(what, code)

    def onTimeout(self):
        Logger.log("IUserDbLoaduserdataviewResponse.onTimeout")
        self.request.error(ErrorCodeManager.getError("ErrorLogin_signupOperTimeout"))


class ITableSaverRemovefamilymembersResponse(itablesave.ITableSaver_Removefamilymembers_Response):
    def __init__(self, clientRequest, userEntity, indexes):
        """
        :type clientRequest: message.gate.iuserinfo.IUserInfo_Removefamilymember_Request
        :type userEntity: UserEntity
        :type indexes: list[int]
        """

        super().__init__()
        self.clientRequest = clientRequest
        self.userEntity = userEntity
        self.indexes = indexes

    def onResponse(self):
        for index in self.indexes:
            if not self.userEntity.removeFamilyMember(index):
                Logger.log("ITableSaverRemovefamilymembersResponse.onResponse", "Oops: unexpected index: ", index)

        self.clientRequest.response()

    def onError(self, what, code):
        Logger.log("ITableSaverRemovefamilymembersResponse.onError:",
                   what, ", code:", code, ", who: ", self.userEntity.getUserId())

        self.clientRequest.error(what, code)

    def onTimeout(self):
        self.clientRequest.error(ErrorCodeManager.getError("ErrorLogin_signupOperTimeout"))
