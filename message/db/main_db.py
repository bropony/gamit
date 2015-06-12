#
# file: main_db.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
import message.common.publicdef
import message.gate.gatemsg


class AnRmiTest:
    def __init__(self):
        self.message = message.gate.gatemsg.SMessage()
        self.ip = str()
        self.shortDesc = str()
        self.passedTimes = int()

    def _read(self, _is):
        self.message._read(_is)
        self.ip = _is.readString()
        self.shortDesc = _is.readString()
        self.passedTimes = _is.readInt()

    def _write(self, _os):
        self.message._write(_os)
        _os.writeString(self.ip)
        _os.writeString(self.shortDesc)
        _os.writeInt(self.passedTimes)

    def _fromJson(self, js):
        if 'message' in js and isinstance(js['message'], message.gate.gatemsg.SMessage):
            self.message._fromJson(js['message'])
        if 'ip' in js and isinstance(js['ip'], str):
            self.ip = js['ip']
        if 'shortDesc' in js and isinstance(js['shortDesc'], str):
            self.shortDesc = js['shortDesc']
        if 'passedTimes' in js and isinstance(js['passedTimes'], int):
            self.passedTimes = js['passedTimes']

    def _toJson(self):
        js = dict()
        js['message'] = self.message._toJson()
        js['ip'] = self.ip
        js['shortDesc'] = self.shortDesc
        js['passedTimes'] = self.passedTimes
        return js

MessageBlock.register(AnRmiTest)

