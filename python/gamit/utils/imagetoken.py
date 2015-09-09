"""
@author: mahanzhou
@date: 8/3/15
@file: 
@desc:

"""

from qiniu import Auth
import xml.etree.ElementTree as xmlParser
import os

class __ImageTouken:
    def __init__(self):
        self.__acckey = ""
        self.__secretkey = ""
        self.__domain = ""
        self.__bucket = ""
        self.__callbackUrl = ""
        self.__expires = 3600

        self.__auth = None

    def loadConfig(self):
        filePath = os.path.split(__file__)[0]
        configPath = os.path.join(filePath, "../../staticdata/utils/imagetoken.xml")

        xmlDoc = xmlParser.parse(configPath)
        xmlRoot = xmlDoc.getroot()
        for child in xmlRoot:

            if child.tag == "acckey":
                self.__acckey = child.text

            elif child.tag == "secretkey":
                self.__secretkey = child.text

            elif child.tag == "domain":
                self.__domain = child.text

            elif child.tag == "bucket":
                self.__bucket = child.text

            elif child.tag == "callbackUrl":
                self.__callbackUrl = child.text

            elif child.tag == "expires":
                self.__expires = int(child.text)

        self.__createAuth()

    def __createAuth(self):
        self.__auth = Auth(self.__acckey, self.__secretkey)

    def getExpires(self):
        return self.__expires

    def uploadToken(self, key):
        policy = None

        if self.__callbackUrl:
            policy = dict(callbackUrl=self.__callbackUrl,
                          callbackBody="key=$(key)&hash=$(etag)",
                          returnBody="key=$(key)&hash=$(etag)&name=$(fname)"
                          )

        return self.__auth.upload_token(self.__bucket, key, self.__expires, policy)

    def downloadToken(self, key, imageFormat=""):
        bauseUrl = "http://{}/{}".format(self.__domain, key)
        if imageFormat:
            bauseUrl = "{}?{}".format(bauseUrl, imageFormat)

        privateUrl = self.__auth.private_download_url(bauseUrl, self.__expires)

        return privateUrl

ImageToken = __ImageTouken()
