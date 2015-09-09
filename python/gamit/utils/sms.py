__author__ = 'mahanzhou'

import urllib, urllib.request, urllib.parse
import os
import os.path
import xml.etree.ElementTree as xmlParser
from twisted.internet import reactor

from gamit.log.logger import Logger

class MsmSendCallback:
    def __init__(self, params, response):
        self.params = params
        self.response = response

    def __call__(self, *args, **kwargs):
        Logger.log("MsmSendCallback.response:", self.response.read())

class __SMSManager:
    def __init__(self):
        self.__account = ""
        self.__pswd = ""
        self.__domain = ""
        self.__url = ""
        self.__fullUrl = ""

        self.__baseVales = {}

    def __call__(self, params):
        req = urllib.request.Request(self.__fullUrl, params)
        res = urllib.request.urlopen(req)

        reactor.callFromThread(MsmSendCallback(params, res))

    def loadConfig(self):
        cwd = os.path.split(__file__)[0]
        configPath = os.path.join(cwd, "../../staticdata/utils/sms.xml")

        xmlDoc = xmlParser.parse(configPath)
        xmlRoot = xmlDoc.getroot()
        for child in xmlRoot:
            if child.tag == "account":
                self.__account = child.text

            elif child.tag == "password":
                self.__pswd = child.text

            elif child.tag == "domain":
                self.__domain = child.text

            elif child.tag == "url":
                self.__url = child.text

        self.__fullUrl = "http://{}/{}".format(self.__domain, self.__url)

        self.__baseVales = dict(
            account=self.__account,
            pswd=self.__pswd,
            needstatus='false',
        )

    def sendSMS(self, phoneNum, msg):
        values = {}
        values.update(self.__baseVales)

        if isinstance(phoneNum, list) or isinstance(phoneNum, tuple):
            phoneNum = ",".join(phoneNum)

        values["msg"] = msg
        values["mobile"] = phoneNum

        params = urllib.parse.urlencode(values).encode(encoding='UTF8')

        reactor.callInThread(self, params)

# singleton
SMSManager = __SMSManager()