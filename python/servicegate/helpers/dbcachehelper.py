__author__ = 'mahanzhou'

import logic.settings.proxy
import gamit.rmi.proxymanager
import gamit.app.apptype

class DbCacheHelper:
    @classmethod
    def getDbProxy(cls, name):
        """
        :type name: str
        :rtype: gamit.rmi.rmicore.RmiProxy
        """
        dbProxy = gamit.rmi.proxymanager.ProxyManager.getProxy(
            gamit.app.apptype.DBCACHE, name)

        return dbProxy

    @classmethod
    def getIUserDbProxy(cls):
        """
        :rtype: message.db.iuserdb.IUserDbProxy
        """
        return cls.getDbProxy("IUserDb")

    @classmethod
    def getILoginDbProxy(cls):
        """
        :rtype: message.db.ilogindb.ILoginDbProxy
        """
        return cls.getDbProxy("ILoginDb")

    @classmethod
    def getITableSaverProxy(cls):
        """
        :rtype: message.db.itablesaver.ITableSaverProxy
        """
        return cls.getDbProxy("ITableSaver")

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
    def getTableSaverProxy(cls):
        """
        :rtype: message.db.itablesaver.ITableSaverProxy
        """
        return cls.getDbProxy(logic.settings.proxy.ProxySetting.ITableSaverProxyName)

    @classmethod
    def updateTUserBasic(cls, userBasic):
        cls.getTableSaverProxy().updateTUserBasic(None, userBasic)

    @classmethod
    def updateTUserSettings(cls, userSettings):
        cls.getTableSaverProxy().updateTUserSettings(None, userSettings)

    @classmethod
    def updateTUserProperty(cls, userProperty):
        cls.getTableSaverProxy().updateTUserProperty(None, userProperty)

    @classmethod
    def updateTFamilyMember(cls, familyMember):
        cls.getTableSaverProxy().updateTFamilyMember(None, familyMember)

    @classmethod
    def updateTFamilyMemberBatch(cls, familyMembers):
        cls.getTableSaverProxy().updateTFamilyMemberBatch(None, familyMembers)

    @classmethod
    def updateTUserAddress(cls, userAddress):
        cls.getITableSaverProxy().updateTUserAddress(None, userAddress)

