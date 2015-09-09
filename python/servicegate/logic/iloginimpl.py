__author__ = 'mahanzhou'

from message.gate.ilogin import ILoginServant
from message.common.publicdef import ELoginType
from gamit.utils.md5hash import Md5Hash

from dbcallback.userdbcallback import *
from user.phonevalidation import PhoneValidationManager
from staticdata.manager.MessageConfigManager import MessageConfigManager
from staticdata.manager.ConstValueManager import ConstValueManager
from helpers.dbloghelper import DbLogHepler
from helpers.dbcachehelper import DbCacheHelper
from staticdata.serverconfig import ServerConfigManager

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

        if userEntity.isDataLoaded():
            loginReturn = userEntity.getLoginReturn()
            _request.response(loginReturn)

            sessionKey = MyUuid.getUuid()
            userEntity.updateDeviceCodeAndSessionKey(loginInfo.deviceCode, sessionKey)
            UserEntityManager.onUserLogin(userEntity, _request.connId, loginInfo.deviceCode)

            DbCacheHelper.getITableSaverProxy().updateTUserSettings(None, userEntity.getTUserSettings())
            DbLogHepler.logLogin(userEntity.getLogUserInfo())
            return

        # load infos from db
        dbProxy = ProxyManager.getProxy(apptype.DBCACHE, ProxySetting.IUserDbProxyName)
        if dbProxy:
            dbCb = IUserDbLoaduserdataviewResponse(userEntity, _request, loginInfo.deviceCode)
            dbProxy.loadUserDataView(dbCb, userEntity.getAccount())
        else:
            ErrorCodeManager.raiseError("ErrorGate_fatalError")

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

        dbProxy = ProxyManager.getProxy(apptype.DBCACHE, ProxySetting.ILoginDbProxyName)
        if dbProxy:
            dbResponse = ILoginDbCreateaccountResponse(_request, signupInfo.deviceCode)
            dbProxy.createAccount(dbResponse, signupInfo)

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
        DbCacheHelper.getITableSaverProxy().updateTUserBasic(None, userEntity.getTUserBasic())

        _request.response()
