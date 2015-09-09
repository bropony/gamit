__author__ = 'mahanzhou'

#
# @brief - A user entity groups user basic information.
#

from message.gate.gatemsg import SLoginReturn
from message.db.mongodb.usertables import TFamilyMember
from message.logdb.logtables import SLogUserInfo
from message.gate.gatemsg import SUserBrief, SeqMsgHint, SMsgHint, SUserBriefWithoutAvatar
from message.gate.gatemsg import SUserPostCommentHint, SeqUserPostCommentHint
from message.gate.gatemsg import SMyDetailInfo, SeqMyFan, SMyFan
from message.gate.gateconst import EHintType
from gamit.utils.md5hash import Md5Hash
from gamit.log.logger import Logger
from gamit.utils.imagetoken import ImageToken
import datetime
from dbutil.userdb import UserDbHelper

class UserEntity:
    """
    :type __userBasic: message.db.mongodb.usertables.TUserBasic
    :type __userSettings: message.db.mongodb.usertables.TUserSettings
    :type __userProperty: message.db.mongodb.usertables.TUserProperty
    :type __familyMembers: list[message.db.mongodb.usertables.TFamilyMember]
    :type __userAddress: message.db.mongodb.usertables.TUserAddress
    :type __dictSysHint: dict[int, int]
    :type __userPostNewOperList: list[SUserPostCommentHint]
    """
    def __init__(self, tUserBasic):
        self.__dictSysHint = dict()
        self.__userPostNewOperList = SeqUserPostCommentHint()
        self.__newFanList = SeqMyFan()

        self.__userBasic = tUserBasic
        self.__userSettings = None
        self.__userProperty = None
        self.__userAddress = None
        self.__familyMembers = []

    def getTUserBasic(self):
        """
        :rtype: message.db.mongodb.usertables.TUserBasic
        """

        return self.__userBasic

    def getAllHints(self):
        """
        :rtype: list[SSysHint]
        """

        res = SeqMsgHint()
        for hintType, num in self.__dictSysHint.items():
            hint = SMsgHint()
            hint.hintType = hintType
            hint.num = num

            res.append(hint)

        self.clearAllHints()
        return res

    def clearAllHints(self):
        self.__dictSysHint.clear()

    def addSysHint(self, hintType):
        """
        :type data: int
        :rtype: bool
        """
        if not isinstance(hintType, int):
            Logger.log("UserEntity.addSysHint. HintType Must Be int obj")
            return False

        if not EHintType.isValueValid(hintType):
            Logger.log("UserEntity.addSysHint. Invalid HintType: ", hintType)
            return False

        if not hintType in self.__dictSysHint:
            self.__dictSysHint[hintType] = 1
        else:
            self.__dictSysHint[hintType] += 1

        return True

    def addCommentHint(self, hint):

        self.__userPostNewOperList.append(hint)
        self.addSysHint(hint.hintType)

    def getAllCommentHints(self):
        res = SeqUserPostCommentHint()
        res.extend(self.__userPostNewOperList)
        self.__userPostNewOperList.clear()

        return res

    def addNewFan(self, myFan):
        """
        :type myFan: SMyFan
        """
        self.__newFanList.append(myFan)
        self.addSysHint(EHintType.NewFan)

    def getNewFans(self):
        res = SeqMyFan()
        res.extend(self.__newFanList)
        self.__newFanList.clear()

        return res

    def getTUserSettings(self):
        """
        :rtype: message.db.mongodb.usertables.TUserSettings
        """

        return self.__userSettings

    def getTUserProperty(self):
        """
        :rtype: message.db.mongodb.usertables.TUserProperty
        """
        return self.__userProperty

    def getTUserAddress(self):
        """
        :rtype: message.db.mongodb.usertables.TUserAddress
        """
        return self.__userAddress

    def setSessionKey(self, sk):
        self.__userSettings.sessionKey = sk

    def getSessionKey(self):
        return self.__userSettings.sessionKey

    def isSessionKeyValid(self, sk):
        if not self.__userSettings:
            return False

        if self.__userSettings.sessionKey == sk:
            return True

        return False

    def updateDeviceCodeAndSessionKey(self, deviceCode, sessionKey):
        self.getTUserSettings().sessionKey = sessionKey
        self.getTUserSettings().lastLoginDeviceCode = deviceCode
        self.getTUserSettings().lastLoginDt = datetime.datetime.now()

    def isPasswordValid(self, password):
        hashedPswd = Md5Hash.encryptPassword(password)
        # Logger.log("In:", hashedPswd, ", mine:", self.__userBasic.password)

        isValid = (hashedPswd == self.__userBasic.password)

        return isValid

    def isDataLoaded(self):
        """
        :rtype: bool
        """
        if self.__userSettings:
            return True

        return False

    def updateUserData(self, dataView):
        """
        :type dataView: message.db.dataview.SUserDataView
        """

        self.__userSettings = dataView.userSettings
        self.__userProperty = dataView.userProperty
        self.__familyMembers = dataView.familyMembers
        self.__userAddress = dataView.userAddress

    def loadUserData(self):
        """
        :rtype: bool
        """
        return True

    def getLoginReturn(self):
        loginReturn = SLoginReturn()

        loginReturn.sessionKey = self.getSessionKey()
        loginReturn.userId = self.__userBasic.userId
        loginReturn.avatarUrl = ImageToken.downloadToken(self.__userBasic.avatar)
        loginReturn.nickname = self.__userBasic.nickname
        loginReturn.gender = self.__userBasic.gender
        loginReturn.birthday = self.__userBasic.birthday

        return loginReturn

    def getAvatarDownloadUrl(self):
        if not self.__userBasic.avatar:
            return ""

        token = ImageToken.downloadToken(self.__userBasic.avatar)

        return token

    def getUserBriefInfo(self):
        """
        :rtype: SUserBrief
        """
        res = SUserBrief()
        res.avatarUrl = self.getAvatarDownloadUrl()
        res.nickname = self.__userBasic.nickname
        res.userId = self.__userBasic.userId

        return res

    def getUserBriefWithoutAvatar(self):
        """
        :rtype:
        """
        res = SUserBriefWithoutAvatar()
        res.nickName = self.getNickname()
        res.userId = self.getUserId()

        return res

    def getDetails(self):
        """
        :rtype: SMyDetailInfo
        """
        details = SMyDetailInfo()
        details.vipLevel = self.__userProperty.vipLevel
        details.goldBean = self.__userProperty.goldBean
        details.postNum = self.__userProperty.postNum
        details.fanNum = self.__userProperty.fanNum
        details.focusNum = self.__userProperty.focusNum

        return details

    def getAccount(self):
        return self.__userBasic.account

    def getUserId(self):
        return self.__userBasic.userId

    def getNickname(self):
        return self.__userBasic.nickname

    def getDeviceCode(self):
        return self.__userBasic.createdWithDeviceCode

    def getLogUserInfo(self):
        """
        :rtype: SLogUserInfo
        """

        logUserInfo = SLogUserInfo()
        logUserInfo.account = self.getAccount()
        logUserInfo.nickname = self.getNickname()
        logUserInfo.userId = self.getUserId()
        logUserInfo.deviceCode = self.getDeviceCode()

        return logUserInfo

    def updateFamilyMember(self, sfm):
        """
        :type sfm: message.gate.gatemsg.SFamilyMember
        :rtype: message.db.mongodb.usertables.TFamilyMember
        """

        tfm = self.getFamilyMember(sfm.index)
        if tfm:
            UserDbHelper.familyMemberStruct2Table(sfm, tfm)
            return tfm

        tfm = TFamilyMember()
        tfm.userId = self.getUserId()
        UserDbHelper.familyMemberStruct2Table(sfm, tfm)

        return tfm

    def getFamilyMember(self, index):
        """
        :type index: int
        :rtype: message.db.mongodb.usertables.TFamilyMember
        """

        for fm in self.__familyMembers:
            if fm.index == index:
                return fm

        return None

    def getAllFamilyMember(self):
        return self.__familyMembers

    def hasFamilyMember(self, index):
        """
        :type index: int
        :rtype: bool
        """

        if self.getFamilyMember(index):
            return True

        return False

    def removeFamilyMember(self, index):
        """
        :type index: int
        :rtype: bool
        """

        for i in range(len(self.__familyMembers)):
            if self.__familyMembers[i].index == index:
                del self.__familyMembers[i]
                return True

            return False

    def updateUserAddress(self, address):
        """
        :type address: common.publicmsg.SAddress
        :rtype: int
        """
        maxAddressIdx = 0

        for idx in range(len(self.__userAddress.addressList)):
            existedAddress = self.__userAddress.addressList[idx]
            if existedAddress.addressIndex > maxAddressIdx:
                maxAddressIdx = existedAddress.addressIndex

            if existedAddress.addressIndex == address.addressIndex:
                self.__userAddress.addressList[idx] = address
                return address.addressIndex

        if address.addressIndex == 0:
            address.addressIndex = maxAddressIdx + 1

        if not self.__userAddress.addressList:
            address.isDefault = True

        self.__userAddress.addressList.append(address)
        return address.addressIndex

    def deleleteAddress(self, addressIndex):
        """
        :type addressIndex: int
        :rtype: bool
        """

        for idx in range(len(self.__userAddress.addressList)):
            address = self.__userAddress.addressList[idx]
            if address.addressIndex == addressIndex:
                del self.__userAddress.addressList[idx]
                return True

        return False

    def setDefaultAddress(self, addressIndex):
        """
        :type addressIndex: int
        :rtype: bool
        """

        oldDefaultAddress = None
        newDefaultAddress = None
        for idx in range(len(self.__userAddress.addressList)):
            address = self.__userAddress.addressList[idx]
            if address.addressIndex == addressIndex:
                newDefaultAddress = address

            if address.isDefault:
                oldDefaultAddress = address

        if not newDefaultAddress:
            return False

        if oldDefaultAddress:
            oldDefaultAddress.isDefault = False

        newDefaultAddress.isDefault = True
        return True
