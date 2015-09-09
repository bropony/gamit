#
# file: logconst.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *


# message.logdb.logconst.ELogPostOperType
class ELogPostOperType:
    View = 1
    Upvote = 2
    Comment = 3
    Share = 4
    Unupvote = 5

    @classmethod
    def isValueValid(cls, _val):
        if _val == cls.View:
            return True

        if _val == cls.Upvote:
            return True

        if _val == cls.Comment:
            return True

        if _val == cls.Share:
            return True

        if _val == cls.Unupvote:
            return True

        return False

