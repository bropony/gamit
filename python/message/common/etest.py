#
# file: etest.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *


class EHelloWorld:
    Hello = 0
    World = 1

class SHelloEnum:
    __slots__ = dict()
    __slots__['age'] = int
    __slots__['damn'] = str
    __slots__['greetType'] = int

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SHelloEnum.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    def __init__(self):
        self.age = int()
        self.damn = str()
        self.greetType = EHelloWorld.Hello

    def _read(self, _is):
        self.age = _is.readInt()
        self.damn = _is.readString()
        self.greetType = _is.readInt()

    def _write(self, _os):
        _os.writeInt(self.age)
        _os.writeString(self.damn)
        _os.writeInt(self.greetType)

    def _fromJson(self, js):
        if 'age' in js and isinstance(js['age'], int):
            self.age = js['age']
        if 'damn' in js and isinstance(js['damn'], str):
            self.damn = js['damn']
        if 'greetType' in js and isinstance(js['greetType'], int):
            self.greetType = js['greetType']

    def _toJson(self):
        js = dict()
        js['age'] = self.age
        js['damn'] = self.damn
        js['greetType'] = self.greetType
        return js

MessageBlock.register(SHelloEnum)

