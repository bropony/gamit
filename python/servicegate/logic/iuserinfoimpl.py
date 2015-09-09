__author__ = 'mahanzhou'

import datetime
from message.gate.iuserinfo import IUserInfoServant
from message.gate.gatemsg import SeqFamilyMember, SFamilyMember
from message.common.publicdef import EGender
from message.db.mongodb.usertables import SeqTFamilyMember
from user.userentitymanager import UserEntityManager
from staticdata.manager.ErrorCodeManager import ErrorCodeManager
from gamit.log.logger import Logger

from helpers.dbcachehelper import DbCacheHelper
from dbcallback.userdbcallback import ITableSaverRemovefamilymembersResponse

class IUserInfoImpl(IUserInfoServant):
    def __init__(self):
        super().__init__()

    def getMyDetails(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.iuserinfo.IUserInfo_Getmydetails_Request
        """
        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        details = userEntity.getDetails()
        _request.response(details)

    def getFamilyMembers(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.iuserinfo.IUserInfo_Getfamilymembers_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        res = SeqFamilyMember()

        for tfm in userEntity.getAllFamilyMember():
            sfm = SFamilyMember()

            DbCacheHelper.familyMemberTable2Struct(tfm, sfm)
            res.append(sfm)

        _request.response(res)

    def changeNickname(self, sessionKey, newNickname, _request):
        """
        :type sessionKey: str
        :type newNickname: str
        :type _request: IUserInfo_Changenickname_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        if not newNickname:
            ErrorCodeManager.raiseError("ErrorGate_invalidNickname")

        tUserBasic = userEntity.getTUserBasic()
        tUserBasic.nickname = newNickname

        DbCacheHelper.updateTUserBasic(tUserBasic)

        _request.response()

    def changeAvatar(self, sessionKey, newAvatar, _request):
        """
        :type sessionKey: str
        :type newAvatar: str
        :type _request: message.gate.iuserinfo.IUserInfo_Changeavatar_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        if not newAvatar or len(newAvatar) < 20:
            ErrorCodeManager.raiseError("ErrorGate_invalidAvatar")

        # avatarSizeLimit = 200 * 1024
        # if len(newAvatar) > avatarSizeLimit:
        #    ErrorCodeManager.raiseError("ErrorGate_avatarSizeTooLarge")

        tUserBasic = userEntity.getTUserBasic()
        tUserBasic.avatar = newAvatar
        DbCacheHelper.updateTUserBasic(tUserBasic)

        _request.response()
        Logger.log("Change Avatar Success...")

    def updateGender(self, sessionKey, gender, _request):
        """
        :type sessionKey: str
        :type gender: int
        :type _request: message.gate.iuserinfo.IUserInfo_Updategender_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        if gender != EGender.Female and gender != EGender.Male:
            ErrorCodeManager.raiseError("ErrorGate_invalidGender")

        userEntity.getTUserBasic().gender = gender
        DbCacheHelper.updateTUserBasic(userEntity.getTUserBasic())

        _request.response()

    def updateBirthDay(self, sessionKey, birthday, _request):
        """
        :type sessionKye: str
        :type birthday: datetime.datetime
        :type _request: message.gate.iuserinfo.IUserInfo_Updatebirthday_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        if birthday > datetime.datetime.now():
            ErrorCodeManager.raiseError("ErrorGate_invalidBirthday")

        userEntity.getTUserBasic().birthday = birthday
        DbCacheHelper.updateTUserBasic(userEntity.getTUserBasic())

    def updateFamilyMembers(self, sessionKey, familyMembers, _request):
        """
        :type sessionKey: str
        :type familyMembers: list[message.gate.gatemsg.SFamilyMember]
        :type _request: IUserInfo_Updatefamilymembers_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        indexSet = set()
        tfms = SeqTFamilyMember()

        for fm in familyMembers:
            if fm.index in indexSet:
                Logger.log("Duplicated index:", fm.index)
                ErrorCodeManager.raiseError("ErrorGate_clientInputError")

            if not EGender.isValueValid(fm.gender):
                Logger.log("Invalid Gender:", fm.index)
                ErrorCodeManager.raiseError("ErrorGate_clientInputError")

            tfm = userEntity.updateFamilyMember(fm)
            tfms.append(tfm)

        DbCacheHelper.getTableSaverProxy().updateTFamilyMemberBatch(None, tfms)

    def removeFamilyMember(self, sessionKey, indexes, _request):
        """
        :type sessionKey: str
        :type indexes: list[int]
        :type _request: message.gate.iuserinfo.IUserInfo_Removefamilymember_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        for index in indexes:
            if not userEntity.hasFamilyMember(index):
                ErrorCodeManager.raiseError("ErrorGate_clientInputError")

        dbRemoveCb = ITableSaverRemovefamilymembersResponse(_request, userEntity, indexes)
        DbCacheHelper.getTableSaverProxy().removeFamilyMembers(dbRemoveCb, userEntity.getUserId(), indexes)

    def updateAdress(self, sessionKey, addressInfo, _request):
        """
        :type sessionKey: str
        :type addressInfo: message.common.publicmsg.SAddress
        :type _request: message.gate.iuserinfo.IUserInfo_Updateadress_Request
        """

        if not addressInfo.recipientName:
            ErrorCodeManager.raiseError("ErrorGate_addressRecipentNameEmpty")

        if not addressInfo.recipientPhoneNum:
            ErrorCodeManager.raiseError("ErrorGate_addressRecipentPhoneNumEmpty")

        if not addressInfo.city:
            ErrorCodeManager.raiseError("ErrorGate_addressCityEmpty")

        if not addressInfo.details:
            ErrorCodeManager.raiseError("ErrorGate_addressDetailsEmpty")

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        addressIndex = userEntity.updateUserAddress(addressInfo)
        _request.response(addressIndex)

        DbCacheHelper.updateTUserAddress(userEntity.getTUserAddress())

    def getAddressList(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.iuserinfo.IUserInfo_Getaddresslist_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        _request.response(userEntity.getTUserAddress().addressList)

    def setDefaultAddress(self, sessionKey, addressIndex, _request):
        """
        :type addressIndex: int
        :type _request: message.gate.iuserinfo.IUserInfo_Setdefaultaddress_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        res = userEntity.setDefaultAddress(addressIndex)
        if not res:
            ErrorCodeManager.raiseError("ErrorGate_addressNotExisted")
        else:
            DbCacheHelper.updateTUserAddress(userEntity.getTUserAddress())
            _request.response()

    def deleteAddress(self, sessionKey, addressIndex, _request):
        """
        :type addressIndex: int
        :type _request: message.gate.iuserinfo.IUserInfo_Deleteaddress_Request
        """

        userEntity = UserEntityManager.findUserEntityBySessionKey(sessionKey)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorGate_notLoggedInYet")

        res = userEntity.deleleteAddress(addressIndex)

        if not res:
            ErrorCodeManager.raiseError("ErrorGate_addressNotExisted")
        else:
            DbCacheHelper.updateTUserAddress(userEntity.getTUserAddress())
            _request.response()

