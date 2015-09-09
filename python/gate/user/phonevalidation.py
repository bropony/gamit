"""
@author: mahanzhou
@date: 8/4/15
@file: 
@desc:

"""

from gamit.utils.sms import SMSManager
import datetime
import random
from staticdata.manager.ConstValueManager import ConstValueManager

class _ValidataCode:
    """
    :type phoneNum: str
    :type validationCode: str
    :type expiredDt: datetime.datetime
    """
    def __init__(self, deviceCode, phoneNum, code, expiredDt):
        self.deviceCode = deviceCode
        self.phoneNum = phoneNum
        self.validationCode = code
        self.expiredDt = expiredDt
        self.createDt = datetime.datetime.now()

    def isExpired(self, tilDt):
        if tilDt >= self.expiredDt:
            return True

        return False

class __PhoneValidationManager:
    """
    :type codeMap: dict[str, _ValidataCode]
    """
    def __init__(self):
        self.codeMap = {}

    def __removeExpiredCode(self):
        keyToRemove = set()
        now = datetime.datetime.now()

        for key in self.codeMap:
            if self.codeMap[key].isExpired(now):
                keyToRemove.add(key)

        for key in keyToRemove:
            del self.codeMap[key]

    def genValidationCode(self):
        validationCode = "{:06d}".format(random.randint(1, 999999))

        return validationCode

    def sendValidationCode(self, deviceCode, phoneNum, validationCode, msg, lifeSpan=5):
        """
        :type deviceCode: str
        """

        if lifeSpan <= 0:
            lifeSpan = 5

        interval = datetime.timedelta(0, lifeSpan * 60)
        expiredDt = datetime.datetime.now() + interval

        self.codeMap[phoneNum] = _ValidataCode(deviceCode, phoneNum, validationCode, expiredDt)

        SMSManager.sendSMS(phoneNum, msg)

    def isInCooldown(self, phoneNum):
        if phoneNum not in self.codeMap:
            return False

        timeDelta = datetime.datetime.now() - self.codeMap[phoneNum].createDt
        if timeDelta.total_seconds() < 60:
            return True

        return False

    def isValidationCodeValid(self, validationCode, phoneNum):
        if phoneNum not in self.codeMap:
            return False

        vc = self.codeMap[phoneNum]

        if validationCode != vc.validationCode:
            return False

        now = datetime.datetime.now()
        if vc.expiredDt <= now:
            return False

        return True

    def removeValidationCode(self, phoneNum):
        if phoneNum in self.codeMap:
            del self.codeMap[phoneNum]

PhoneValidationManager = __PhoneValidationManager()
