__author__ = 'mahanzhou'

from message.db.iuserdb import IUserDbServant
from gamit.mongodb.database import MongoDatabase
from message.db.mongodb.usertables import *
from message.db.dataview import SUserDataView
from gamit.log.logger import Logger

from staticdata.manager.ErrorCodeManager import ErrorCodeManager

class IUserDbImpl(IUserDbServant):
    def __init__(self):
        super().__init__()

    def loadUserBasic(self, createdDtLimit, targetNum, _request):
        Logger.log("Loading userbasic request...")

        userBasicTable = MongoDatabase.findTableByMessageType(TUserBasic)

        if not userBasicTable:
            ErrorCodeManager.raiseError("")

        query = {"createDt": {"$gt": createdDtLimit}}
        res = userBasicTable.findManyWithQuey(query, targetNum)

        allLoaded = len(res) < targetNum
        tables = SeqTUserBasic(res)

        _request.response(allLoaded, tables)

    def loadUserDataView(self, account, _request):
        tableUserBasic = MongoDatabase.findTableByMessageType(TUserBasic)
        tableUserSettings = MongoDatabase.findTableByMessageType(TUserSettings)
        tableUserProperty = MongoDatabase.findTableByMessageType(TUserProperty)
        tableFamilyMember = MongoDatabase.findTableByMessageType(TFamilyMember)
        tableUserAddress = MongoDatabase.findTableByMessageType(TUserAddress)

        userDataView = SUserDataView()

        basic = tableUserBasic.findOneWithQuery({"account": account})
        if basic:
            userDataView.basicInfo = basic
        else:
            ErrorCodeManager.raiseError("ErrorLogin_InvalidLoginInfo")

        settings = tableUserSettings.findOne(basic.userId)
        if settings:
            userDataView.userSettings = settings
        else:
            userDataView.userSettings.userId = basic.userId

        property = tableUserProperty.findOne(basic.userId)
        if property:
            userDataView.userProperty = property
        else:
            userDataView.userSettings.userId = basic.userId

        addresses = tableUserAddress.findOne(basic.userId)
        if addresses:
            userDataView.userAddress = addresses
        else:
            userDataView.userAddress.userId = basic.userId

        members = tableFamilyMember.findMany(basic.userId)
        if members:
            userDataView.familyMembers.extend(members)

        _request.response(userDataView)
