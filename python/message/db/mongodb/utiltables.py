#
# file: utiltables.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *
import message.db.systemcommand


# message.db.mongodb.utiltables.TSystemCommand
class TSystemCommand:
    __slots__ = dict()
    __slots__['commandType'] = int
    __slots__['priority'] = int
    __slots__['numericVal'] = int
    __slots__['stringVal'] = str
    __slots__['jsExtraInfo'] = str

    # field names
    fn_commandType = 'commandType'
    fn_priority = 'priority'
    fn_numericVal = 'numericVal'
    fn_stringVal = 'stringVal'
    fn_jsExtraInfo = 'jsExtraInfo'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TSystemCommand.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type commandType: int
    type priority: int
    type numericVal: int
    type stringVal: str
    type jsExtraInfo: str
    """
    def __init__(self):
        self.commandType = message.db.systemcommand.ESysCommandType.AddSysTopic
        self.priority = int()
        self.numericVal = int()
        self.stringVal = str()
        self.jsExtraInfo = str()

    def _read(self, _is):
        self.commandType = _is.readInt()
        self.priority = _is.readInt()
        self.numericVal = _is.readInt()
        self.stringVal = _is.readString()
        self.jsExtraInfo = _is.readString()

    def _write(self, _os):
        _os.writeInt(self.commandType)
        _os.writeInt(self.priority)
        _os.writeInt(self.numericVal)
        _os.writeString(self.stringVal)
        _os.writeString(self.jsExtraInfo)

    def _fromJson(self, js):
        if 'commandType' in js and isinstance(js['commandType'], int):
            self.commandType = js['commandType']
        if 'priority' in js and isinstance(js['priority'], int):
            self.priority = js['priority']
        if 'numericVal' in js and isinstance(js['numericVal'], int):
            self.numericVal = js['numericVal']
        if 'stringVal' in js and isinstance(js['stringVal'], str):
            self.stringVal = js['stringVal']
        if 'jsExtraInfo' in js and isinstance(js['jsExtraInfo'], str):
            self.jsExtraInfo = js['jsExtraInfo']

    def _toJson(self):
        js = dict()
        js['commandType'] = self.commandType
        js['priority'] = self.priority
        js['numericVal'] = self.numericVal
        js['stringVal'] = self.stringVal
        js['jsExtraInfo'] = self.jsExtraInfo
        return js

MessageBlock.register(TSystemCommand)

# message.db.mongodb.utiltables.SeqTSystemCommand
class SeqTSystemCommand(ListBase):
    def __init__(self, _data=None):
        super().__init__(TSystemCommand, 'SeqTSystemCommand')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TSystemCommand()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TSystemCommand()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

# message.db.mongodb.utiltables.TSystemCommandLog
class TSystemCommandLog:
    __slots__ = dict()
    __slots__['commandType'] = int
    __slots__['priority'] = int
    __slots__['numericVal'] = int
    __slots__['stringVal'] = str
    __slots__['jsExtraInfo'] = str
    __slots__['processedDt'] = datetime.datetime

    # field names
    fn_commandType = 'commandType'
    fn_priority = 'priority'
    fn_numericVal = 'numericVal'
    fn_stringVal = 'stringVal'
    fn_jsExtraInfo = 'jsExtraInfo'
    fn_processedDt = 'processedDt'

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TSystemCommandLog.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    """
    type commandType: int
    type priority: int
    type numericVal: int
    type stringVal: str
    type jsExtraInfo: str
    type processedDt: datetime.datetime
    """
    def __init__(self):
        self.commandType = message.db.systemcommand.ESysCommandType.AddSysTopic
        self.priority = int()
        self.numericVal = int()
        self.stringVal = str()
        self.jsExtraInfo = str()
        self.processedDt = datetime.datetime.now()

    def _read(self, _is):
        self.commandType = _is.readInt()
        self.priority = _is.readInt()
        self.numericVal = _is.readInt()
        self.stringVal = _is.readString()
        self.jsExtraInfo = _is.readString()
        self.processedDt = _is.readDate()

    def _write(self, _os):
        _os.writeInt(self.commandType)
        _os.writeInt(self.priority)
        _os.writeInt(self.numericVal)
        _os.writeString(self.stringVal)
        _os.writeString(self.jsExtraInfo)
        _os.writeDate(self.processedDt)

    def _fromJson(self, js):
        if 'commandType' in js and isinstance(js['commandType'], int):
            self.commandType = js['commandType']
        if 'priority' in js and isinstance(js['priority'], int):
            self.priority = js['priority']
        if 'numericVal' in js and isinstance(js['numericVal'], int):
            self.numericVal = js['numericVal']
        if 'stringVal' in js and isinstance(js['stringVal'], str):
            self.stringVal = js['stringVal']
        if 'jsExtraInfo' in js and isinstance(js['jsExtraInfo'], str):
            self.jsExtraInfo = js['jsExtraInfo']
        if 'processedDt' in js and isinstance(js['processedDt'], datetime.datetime):
            self.processedDt = js['processedDt']
        elif 'processedDt' in js and isinstance(self.processedDt, datetime.datetime):
            self.processedDt = datetime.datetime.strptime(js['processedDt'], '%Y-%m-%d %H:%M:%S')

    def _toJson(self):
        js = dict()
        js['commandType'] = self.commandType
        js['priority'] = self.priority
        js['numericVal'] = self.numericVal
        js['stringVal'] = self.stringVal
        js['jsExtraInfo'] = self.jsExtraInfo
        js['processedDt'] = self.processedDt
        return js

MessageBlock.register(TSystemCommandLog)

# message.db.mongodb.utiltables.SeqTSystemCommandLog
class SeqTSystemCommandLog(ListBase):
    def __init__(self, _data=None):
        super().__init__(TSystemCommandLog, 'SeqTSystemCommandLog')

        if _data:
            self.extend(_data)

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TSystemCommandLog()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TSystemCommandLog()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

