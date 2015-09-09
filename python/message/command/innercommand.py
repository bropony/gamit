#
# file: innercommand.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *


# message.command.innercommand.EDbUpdateCommand
class EDbUpdateCommand:
    NewSysTopic = 600001

    @classmethod
    def isValueValid(cls, _val):
        if _val == cls.NewSysTopic:
            return True

        return False

