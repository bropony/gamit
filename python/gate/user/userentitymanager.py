__author__ = 'mahanzhou'

from gamit.log.logger import Logger
from user.userentity import UserEntity
from dbutil.userdb import UserDbHelper
import datetime

class __UserEntityManager:
    """
    :type dictUserIdUser: dict[str, UserEntity]
    :type dictAccountUser: dict[str, UserEntity]
    :type dictConnIdUser: dict[int, UserEntity]
    :type dictSessionUser: dict[str, UserEntity]
    :type dictDeviceCodeUser: dict[str, UserEntity]
    """
    def __init__(self):
        self.dictUserIdUser = {}       # key: userId, val: UserEntity
        self.dictAccountUser = {}      # key: account, val: UserEntity
        self.dictConnIdUser = {}       # key: connId, val: UserEntity
        self.dictSessionUser = {}      # key: session, val: UserEntity
        self.dictDeviceCodeUser = {}   # key: deviceCode, val: UserEntity

    def onConnectionClose(self, connId):
        Logger.logInfo("UserEntityManager.onConnectionClose: {}".format(connId))
        if connId in self.dictConnIdUser:
            del self.dictConnIdUser[connId]

    def loadAllUserBasics(self):
        if self.dictUserIdUser:
            return

        allUserBasics = UserDbHelper.loadAllUserBasics()
        self.addUserBasics(allUserBasics)

        Logger.log("Num of User Loaded:", len(allUserBasics))

    def addUserBasics(self, userBasics):
        """
        __UserEntityManager.addUserBasics(message.db.mongodb.usertables.TUserBasic)
        """
        for ub in userBasics:
            userEntity = UserEntity(ub)
            self.addUser(userEntity)

    def addUser(self, userEntity):
        """
        :type userEntity: UserEntity
        """

        self.dictUserIdUser[userEntity.getUserId()] = userEntity
        self.dictAccountUser[userEntity.getAccount()] = userEntity

    def findUserEntityByUserId(self, userId):
        """
        :type userId: str
        :rtype: UserEntity
        """

        if userId not in self.dictUserIdUser:
            return self.dictUserIdUser[userId]

        userEntity = self.dictUserIdUser[userId]

        if not userEntity.getTUserProperty():
            dataView = UserDbHelper.loadUserDataView(userId)
            if not dataView:
                Logger.log("Load user data view failed")
                return None
            userEntity.updateUserData(dataView)

        return userEntity

    def findUserEntityByAccount(self, account):
        """
        :type account: str
        :rtype: UserEntity
        """

        if account in self.dictAccountUser:
            return self.dictAccountUser[account]

        return None

    def findUserEntityByConnId(self, connId):
        """
        :type connId: int
        :rtype: UserEntity
        """

        if connId in self.dictConnIdUser:
            return self.dictConnIdUser[connId]

        return None

    def findUserEntityBySessionKey(self, sessionKey):
        """
        :type sessionKey: str
        :rtype: UserEntity
        """

        if sessionKey in self.dictSessionUser:
            return self.dictSessionUser[sessionKey]

        dataView = UserDbHelper.loadDataViewBySessionKey(sessionKey)
        if not dataView:
            return None

        userEntity = self.findUserEntityByUserId(dataView.userSettings.userId)
        if not userEntity:
            return None

        userEntity.updateUserData(dataView)
        self.dictSessionUser[sessionKey] = userEntity

        return userEntity

    def findUserEntityByDeviceCode(self, deviceCode):
        """
        :type deviceCode: str
        :rtype: UserEntity
        """

        if deviceCode in self.dictDeviceCodeUser:
            return self.dictDeviceCodeUser[deviceCode]

        return None

    def onUserLogin(self, userEntity, connId, deviceCode):
        """
        :type userEntity: UserEntity
        :type connId: int
        """
        
        self.dictConnIdUser[connId] = userEntity
        self.dictSessionUser[userEntity.getSessionKey()] = userEntity
        self.dictDeviceCodeUser[deviceCode] = userEntity

# the singleton
UserEntityManager = __UserEntityManager()
