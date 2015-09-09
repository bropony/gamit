__author__ = 'mahanzhou'

from message.gate.ilogin import ILoginServant
from message.common.publicdef import ELoginType
from gamit.utils.md5hash import Md5Hash
from gamit.log.logger import Logger
from gamit.utils.myuuid import MyUuid

from dbutil.dbsaver import DbSaver
from dbutil.userdb import UserDbHelper
from dbutil.dbloghelper import DbLogHepler
from user.phonevalidation import PhoneValidationManager
from staticdata.manager.MessageConfigManager import MessageConfigManager
from staticdata.manager.ConstValueManager import ConstValueManager
from staticdata.serverconfig import ServerConfigManager
from staticdata.manager.ErrorCodeManager import ErrorCodeManager
from user.userentitymanager import UserEntityManager
from user.userentity import UserEntity

class ILoginImpl(ILoginServant):
    def __init__(self):
        super().__init__()

    def getPhoneSignupValidationCode(self, deviceCode, phoneNum, _request):
        """
        :type deviceCode: str
        :type phoneNum: str
        :type _request: message.gate.ilogin.ILogin_Getphonesignupvalidationcode_Request
        """

        if PhoneValidationManager.isInCooldown(phoneNum):
            ErrorCodeManager.raiseError("ErrorLogin_validationCodeInCD")

        lifeSpan = ConstValueManager.getIntValue("SignupPhoneValidationCodeLifeSpan")
        validationCode = PhoneValidationManager.genValidationCode()

        msg = MessageConfigManager.getMsg("regist_validation", [validationCode, lifeSpan])
        PhoneValidationManager.sendValidationCode(deviceCode, phoneNum, validationCode, msg, lifeSpan)

        _request.response()

    def login(self, loginInfo, _request):
        """
        :type loginInfo: message.gate.gatemsg.SLogin
        :type _request: message.gate.ilogin.ILogin_Login_Request
        """

        Logger.log("ILoginImpl.login: ", loginInfo.account)

        userEntity = UserEntityManager.findUserEntityByAccount(loginInfo.account)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorLogin_InvalidLoginInfo")

        if not userEntity.isPasswordValid(loginInfo.password):
            ErrorCodeManager.raiseError("ErrorLogin_InvalidLoginInfo")

        if not userEntity.isDataLoaded():
            userDataView = UserDbHelper.loadUserDataView(userEntity.getUserId())
            userEntity.updateUserData(userDataView)

        sessionKey = MyUuid.getUuid()
        userEntity.updateDeviceCodeAndSessionKey(loginInfo.deviceCode, sessionKey)
        UserEntityManager.onUserLogin(userEntity, _request.connId, loginInfo.deviceCode)

        loginReturn = userEntity.getLoginReturn()
        _request.response(loginReturn)

        DbSaver.saveTable(userEntity.getTUserSettings())
        DbSaver.saveTable(userEntity.getTUserBasic())

    def signup(self, signupInfo, _request):
        """
        :type signupInfo: message.gate.gatemsg.SSignup
        :type _request: message.gate.ilogin.ILogin_Signup_Request
        """

        if not signupInfo.account:
            ErrorCodeManager.raiseError("ErrorSignup_invalidAccount")

        if not signupInfo.password:
            ErrorCodeManager.raiseError("ErrorSignup_invalidPassword")

        if not ELoginType.isValueValid(signupInfo.loginType):
            ErrorCodeManager.raiseError("ErrorSignup_invalidLoginType")

        userEntity = UserEntityManager.findUserEntityByAccount(signupInfo.account)
        if userEntity:
            ErrorCodeManager.raiseError("ErrorLogin_AccountExists")

        if signupInfo.loginType == ELoginType.MobilePhoneNum:
            if ServerConfigManager.isValidationCodeEnabled:
                if not PhoneValidationManager.isValidationCodeValid(signupInfo.validationCode, signupInfo.account):
                    ErrorCodeManager.raiseError("ErrorLogin_InvalidValidationCode")
                else:
                    PhoneValidationManager.removeValidationCode(signupInfo.account)

        dataView = UserDbHelper.createAccount(signupInfo)
        userEntity = UserEntity(dataView.basicInfo)
        userEntity.updateUserData(dataView)
        UserEntityManager.addUser(userEntity)

        userEntity.updateDeviceCodeAndSessionKey(signupInfo.deviceCode, MyUuid.getUuid())
        UserEntityManager.onUserLogin(userEntity, _request.connId, signupInfo.deviceCode)

        _request.response(userEntity.getLoginReturn())

        # save changes
        DbSaver.saveTable(userEntity.getTUserSettings())

        # logging
        DbLogHepler.logSignup(userEntity.getLogUserInfo())

    def getPasswordResetValidationCode(self, deviceCode, phoneNum, _request):
        """
        :type deviceCode: str
        :type phoneNum: str
        :type _request: message.gate.ilogin.ILogin_Getpasswordresetvalidationcode_Request
        """

        if PhoneValidationManager.isInCooldown(phoneNum):
            ErrorCodeManager.raiseError("ErrorLogin_validationCodeInCD")

        lifeSpan = ConstValueManager.getIntValue("ResetPasswordValidationCodeLifeSpan")
        validationCode = PhoneValidationManager.genValidationCode()

        msg = MessageConfigManager.getMsg("regist_validation", [validationCode, lifeSpan])
        PhoneValidationManager.sendValidationCode(deviceCode, phoneNum, validationCode, msg, lifeSpan)

        _request.response()

    def resetPhoneUserPassword(self, phoneNum, validationCode, newPassword, _request):
        """
        :type phoneNum: str
        :type validationCode: str
        :type newPassword: str
        :type _request: message.gate.ilogin.ILogin_Resetphoneuserpassword_Request
        """

        userEntity = UserEntityManager.findUserEntityByAccount(phoneNum)
        if not userEntity:
            ErrorCodeManager.raiseError("ErrorLogin_noSuchPhoneRegistered")

        if userEntity.getTUserBasic().accountType != ELoginType.MobilePhoneNum:
            ErrorCodeManager.raiseError("ErrorLogin_noPhoneNumLoginType")

        if not PhoneValidationManager.isValidationCodeValid(validationCode, phoneNum):
            ErrorCodeManager.raiseError("ErrorLogin_InvalidValidationCode")
        else:
            PhoneValidationManager.removeValidationCode(phoneNum)

        userEntity.getTUserBasic().password = Md5Hash.encryptPassword(newPassword)
        DbSaver.saveTable(userEntity.getTUserBasic())

        _request.response()
