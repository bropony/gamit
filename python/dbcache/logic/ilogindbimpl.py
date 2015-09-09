__author__ = 'mahanzhou'

from message.db.ilogindb import ILoginDbServant

from gamit.mongodb.database import MongoDatabase
from gamit.log.logger import Logger
from gamit.utils.myuuid import MyUuid
from gamit.utils.md5hash import Md5Hash
from message.db.mongodb.usertables import *
from message.db.dataview import SUserDataView
from staticdata.manager.ErrorCodeManager import ErrorCodeManager

class ILoginDbImpl(ILoginDbServant):
    def __init__(self):
        super().__init__()

    def createAccount(self, userInfo, _request):
        """
        :type userInfo: message.gate.gatemsg.SSignup
        :type _request: message.db.ilogindb.ILoginDb_Createaccount_Request
        """

        account = userInfo.account
        tableBasic = MongoDatabase.findTableByMessageType(TUserBasic)
        tableSettings = MongoDatabase.findTableByMessageType(TUserSettings)
        tableProperty = MongoDatabase.findTableByMessageType(TUserProperty)
        tableAddress = MongoDatabase.findTableByMessageType(TUserAddress)

        res = tableBasic.findOneWithQuery({"account": account})
        if res:
            ErrorCodeManager.raiseError("ErrorLogin_AccountExists")

        dataView = SUserDataView()
        tBasicInfo = dataView.basicInfo
        tUserSettings = dataView.userSettings
        tUserProperty = dataView.userProperty
        tUserAddress = dataView.userAddress

        tBasicInfo.userId = MyUuid.getUuid()
        tBasicInfo.accountType = userInfo.loginType
        tBasicInfo.account = userInfo.account
        tBasicInfo.password = Md5Hash.encryptPassword(userInfo.password)
        tBasicInfo.nickname = ""
        tBasicInfo.avatar = ""
        tBasicInfo.createDt = datetime.datetime.now()
        tBasicInfo.createdWithDeviceCode = userInfo.deviceCode

        tUserSettings.userId = tBasicInfo.userId
        tUserSettings.lastLoginDeviceCode = tBasicInfo.createdWithDeviceCode
        tUserSettings.lastLoginDt = tBasicInfo.createDt

        tUserProperty.userId = tBasicInfo.userId
        tUserAddress.userId = tBasicInfo.userId

        tableBasic.update(tBasicInfo)
        tableSettings.update(tUserSettings)
        tableProperty.update(tUserProperty)
        tableAddress.update(tUserAddress)

        Logger.log("ILoginDbImpl.createAccount: new user signup:", tBasicInfo.account)
        _request.response(dataView)
#
