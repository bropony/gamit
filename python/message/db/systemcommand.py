#
# file: systemcommand.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *


# message.db.systemcommand.ESysCommandType
class ESysCommandType:
    AddSysTopic = 1001
    AddCommercialAd = 1002
    OnRecharge = 2001

    @classmethod
    def isValueValid(cls, _val):
        if _val == cls.AddSysTopic:
            return True

        if _val == cls.AddCommercialAd:
            return True

        if _val == cls.OnRecharge:
            return True

        return False

