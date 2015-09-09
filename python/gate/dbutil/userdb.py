"""
@author: mahanzhou
@date: 9/4/15
@file: 
@desc:

"""

from gamit.log.logger import Logger
from gamit.mongodb.database import MongoDatabase
from message.db.mongodb.usertables import *
from message.db.dataview import SUserDataView
from gamit.utils.myuuid import MyUuid
from gamit.utils.md5hash import Md5Hash

from staticdata.manager.ErrorCodeManager import ErrorCodeManager

class UserDbHelper:
    @staticmethod
    def familyMemberStruct2Table(sfm, tfm):
        """
        :type sfm: message.gate.gatemsg.SFamilyMember
        :type tfm: message.db.mongodb.usertables.TFamilyMember
        """

        tfm.index = sfm.index
        tfm.member = sfm.member
        tfm.name = sfm.name
        tfm.gender = sfm.gender
        tfm.birthday = sfm.birthday
        tfm.height = sfm.height
        tfm.weight = sfm.weight
        tfm.bust = sfm.bust
        tfm.waistline = sfm.waistline
        tfm.hipline = sfm.hipline
        tfm.brachium = sfm.brachium
        tfm.leglength = sfm.leglength
        tfm.shoulder = sfm.shoulder

    @staticmethod
    def familyMemberTable2Struct(tfm, sfm):
        """
        :type sfm: message.gate.gatemsg.SFamilyMember
        :type tfm: message.db.mongodb.usertables.TFamilyMember
        """

        sfm.index = tfm.index
        sfm.member = tfm.member
        sfm.name = tfm.name
        sfm.gender = tfm.gender
        sfm.birthday = tfm.birthday
        sfm.height = tfm.height
        sfm.weight = tfm.weight
        sfm.bust = tfm.bust
        sfm.waistline = tfm.waistline
        sfm.hipline = tfm.hipline
        sfm.brachium = tfm.brachium
        sfm.leglength = tfm.leglength
        sfm.shoulder = tfm.shoulder

    @classmethod
    def loadAllUserBasics(cls):
        """
        :rtype: list[TUserBasic]
        """

        res = []
        tb = MongoDatabase.findTableByMessageType(TUserBasic)
        if not tb:
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        res = tb.findManyWithQuey()

        return res

    @classmethod
    def loadUserDataView(cls, userId):
        """
        :type userId: str
        :rtype: SUserDataView
        """

        userDataView = SUserDataView()

        tableUserSettings = MongoDatabase.findTableByMessageType(TUserSettings)
        tableUserProperty = MongoDatabase.findTableByMessageType(TUserProperty)
        tableFamilyMember = MongoDatabase.findTableByMessageType(TFamilyMember)
        tableUserAddress = MongoDatabase.findTableByMessageType(TUserAddress)

        settings = tableUserSettings.findOne(userId)
        if settings:
            userDataView.userSettings = settings
        else:
            userDataView.userSettings.userId = userId

        property = tableUserProperty.findOne(userId)
        if property:
            userDataView.userProperty = property
        else:
            userDataView.userSettings.userId = userId

        addresses = tableUserAddress.findOne(userId)
        if addresses:
            userDataView.userAddress = addresses
        else:
            userDataView.userAddress.userId = userId

        members = tableFamilyMember.findMany(userId)
        if members:
            userDataView.familyMembers.extend(members)

        return userDataView

    @classmethod
    def loadDataViewBySessionKey(cls, sessionKey):
        """
        :type sessionKey: str
        :rtype: SUserDataView
        """

        if not sessionKey:
            return None

        userDataView = SUserDataView()

        tableUserSettings = MongoDatabase.findTableByMessageType(TUserSettings)
        tableUserProperty = MongoDatabase.findTableByMessageType(TUserProperty)
        tableFamilyMember = MongoDatabase.findTableByMessageType(TFamilyMember)
        tableUserAddress = MongoDatabase.findTableByMessageType(TUserAddress)

        settings = tableUserSettings.findOneWithQuery({TUserSettings.fn_sessionKey: sessionKey})
        if not settings:
            return None

        userDataView.userSettings = settings
        userId = settings.userId

        property = tableUserProperty.findOne(userId)
        if property:
            userDataView.userProperty = property
        else:
            userDataView.userSettings.userId = userId

        addresses = tableUserAddress.findOne(userId)
        if addresses:
            userDataView.userAddress = addresses
        else:
            userDataView.userAddress.userId = userId

        members = tableFamilyMember.findMany(userId)
        if members:
            userDataView.familyMembers.extend(members)

        return userDataView

    @classmethod
    def removeFamilyMembers(cls, userId, indexes):
        """
        :type userId: str
        :type indexes: list[int]
        """

        tb = MongoDatabase.findTableByMessageType(TFamilyMember)

        if not tb:
            ErrorCodeManager.raiseError("ErrorDb_TableNotFound")

        for index in indexes:
            query = {TFamilyMember.fn_userId: userId, TFamilyMember.fn_index: index}
            tb.delete(query, True)

    @classmethod
    def createAccount(self, userInfo):
        """
        :type userInfo: message.gate.gatemsg.SSignup
        :rtype: SUserDataView
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

        Logger.log("createAccount.createAccount: new user signup:", tBasicInfo.account)
#
