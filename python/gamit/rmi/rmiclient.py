"""
* @name rmiclient.py
*
* @author ahda86@gmail.com
*
* @date 2015/5/23 12:02
*
* @desc rmiclient.py
"""

import datetime
import traceback

from gamit.log.logger import Logger
from gamit.message.messagemanager import MessageManager
from gamit.message.message import MessageBlock
from gamit.serialize.serializer import Serializer, SerializeError
from gamit.serialize.encrypt import simpleDecrypt, simpleEncrypt
from gamit.serialize.datatype import RmiDataType
from gamit.rmi.proxymanager import ProxyManager
from twisted.internet import reactor

class RmiClient:
    def __init__(self, channelType, connector, isDebug, timeout=8):
        self.channelType = channelType
        self.isDebug = isDebug
        self.timeout = timeout
        self.isOpen = False

        self.connector = connector
        self.connector.setRmiClient(self)
        self.messageManager = MessageManager
        self.callbackMap = {}
        self.proxyMap = {}
        self.onOpenCallback = None
        self.openCallArgv = []

        self.onCloseCallback = None
        self.closeCallArgv = []

    def start(self):
        self.connector.start(self.isDebug)
        self._startMonitorCallbackTimeout()

    def stop(self):
        self.connector.stop()
        self.callbackMap = {}

    def setOnOpenCallback(self, cb, *argv):
        self.onOpenCallback = cb
        self.openCallArgv = argv

    def setOnCloseCallback(self, cb, *argv):
        self.onCloseCallback = cb
        self.closeCallArgv = argv

    def addProxy(self, proxy):
        self.proxyMap[proxy.name] = proxy
        proxy.setRmiClient(self)
        ProxyManager.addProxy(self.channelType, proxy)

    def getProxy(self, name):
        if name in self.proxyMap:
            return self.proxyMap[name]
        else:
            return None

    def onOpen(self, ws):
        self.isOpen = True

        if self.onOpenCallback:
            reactor.callLater(0.5, self.onOpenCallback, *self.openCallArgv)
            #cb = self.onOpenCallback
            #cb(*self.openCallArgv)

    def onClose(self):
        self.isOpen = False

        if self.onCloseCallback:
            cb = self.onCloseCallback
            cb(*self.closeCallArgv)

    def onMessage(self, payload, isBinary):
        try:
            payload = simpleDecrypt(payload) # decrypt

            _is = Serializer(payload)
            _is.startToRead()
            rmiType = _is.readByte()
            if rmiType == RmiDataType.RmiResponse:
                self.onResponse(_is)
            elif rmiType == RmiDataType.RmiException:
                self.onError(_is)
            elif rmiType == RmiDataType.MessageBlock:
                self.messageManager.onMessage(_is)
            else:
                raise SerializeError("Unknown RmiDataType")
        except Exception as ex:
            Logger.logInfo(ex)

    def send(self, payload, isBinary):
        payload = simpleEncrypt(payload)
        self.connector.send(payload, isBinary)

    def sendMessage(self, command, toIdList, data):
        msg = MessageBlock(command, toIdList, data)
        self.send(msg.getOsBuffer(), True)

    def onResponse(self, _is):
        msgId = _is.readInt()
        if msgId in self.callbackMap:
            callbackObj = self.callbackMap[msgId]
            del self.callbackMap[msgId]  # remove from cache before handling response

            try:
                callbackObj._onResponse(_is)
            except Exception as ex:
                traceback.print_exc()
                what = traceback.format_exc()
                code = -1
                callbackObj.onError(what, code)

    def onError(self, _is):
        msgId = _is.readInt()
        what = _is.readString()
        code = _is.readInt()
        if msgId in self.callbackMap:
            self.callbackMap[msgId].onError(what, code)
            del self.callbackMap[msgId]

    def _startMonitorCallbackTimeout(self):
        reactor.callLater(self.timeout, self._onTimeout)

    def _onTimeout(self):
        if self.timeout <= 0:
            return

        if self.callbackMap:
            now = datetime.datetime.now()
            newMap = {}
            for msgId in self.callbackMap:
                cb = self.callbackMap[msgId]
                if cb.isExpired(now, self.timeout):
                    cb.onTimeout()
                else:
                    newMap[msgId] = cb
            self.callbackMap = newMap

        reactor.callLater(self.timeout, self._onTimeout)

    def onCall(self, _os, callback):
        self.send(_os.getBuffer(), True)

        if callback:
            # Logger.log("RmiClient.onCall:", callback._msgId)
            self.callbackMap[callback._msgId] = callback

    def heartbeat(self):
        if self.isOpen:
            self.connector.ws.sendPing()
