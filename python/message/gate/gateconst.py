#
# file: gateconst.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *


# message.gate.gateconst.EShareType
class EShareType:
    WeChat = 1

    @classmethod
    def isValueValid(cls, _val):
        if _val == cls.WeChat:
            return True

        return False

# message.gate.gateconst.EHintType
class EHintType:
    AllType = 0
    PostCommented = 1
    PostUpvoted = 2
    PostReposted = 3
    PostCommentReplied = 4
    NewFan = 10
    FanUnfollow = 11
    SysMsg = 20

    @classmethod
    def isValueValid(cls, _val):
        if _val == cls.AllType:
            return True

        if _val == cls.PostCommented:
            return True

        if _val == cls.PostUpvoted:
            return True

        if _val == cls.PostReposted:
            return True

        if _val == cls.PostCommentReplied:
            return True

        if _val == cls.NewFan:
            return True

        if _val == cls.FanUnfollow:
            return True

        if _val == cls.SysMsg:
            return True

        return False

# message.gate.gateconst.ETailerOrderType
class ETailerOrderType:
    NoneType = 0
    ImageText = 1
    Style = 2
    Brushing = 3

    @classmethod
    def isValueValid(cls, _val):
        if _val == cls.NoneType:
            return True

        if _val == cls.ImageText:
            return True

        if _val == cls.Style:
            return True

        if _val == cls.Brushing:
            return True

        return False

# message.gate.gateconst.ETailerOrderStage
class ETailerOrderStage:
    NotBidded = 0
    Bidded = 1
    ToBeAccepted = 2
    Accepted = 3

    @classmethod
    def isValueValid(cls, _val):
        if _val == cls.NotBidded:
            return True

        if _val == cls.Bidded:
            return True

        if _val == cls.ToBeAccepted:
            return True

        if _val == cls.Accepted:
            return True

        return False

