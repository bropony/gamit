"""
@author: mahanzhou
@date: 8/14/15
@file: 
@desc:

"""

from gamit.rmi.proxymanager import ProxyManager
from gamit.app import apptype
from message.gate.ipostoper import IPostOper_Getimageuploadtokens_Response
from message.gate.ipostoper import IPostOper_Getimagedownloadtokens_Response
import qiniu

class IPostOperGetimageuploadtokensResponse(IPostOper_Getimageuploadtokens_Response):
    def __init__(self, filePath):
        super().__init__()
        self.filePath = filePath

    def onResponse(self, imageInfos):
        """
        :type imageInfos: list[message.gate.gatemsg.SImageInfo]
        """
        print("IPostOperGetimageuploadtokensResponse.onResponse")
        for token in imageInfos:
            ret, info = qiniu.put_file(token.token, token.imageKey, self.filePath)
            print("[ImageUploaded] Key:{}\ntoken:{}\nhash:{}\ninfo:{}".format(
                token.imageKey, token.token, ret['hash'], info))

    def onError(self, what, code):
        print("IPostOperGetimageuploadtokensResponse.onError. what:", what, ", code:", code)

    def onTimeout(self):
        print("IPostOperGetimageuploadtokensResponse.onTimeout")

class IPostOperGetimagedownloadtokensResponse(IPostOper_Getimagedownloadtokens_Response):
    def onResponse(self, imgDowloadToken):
        """
        :type imgDowloadToken: message.gate.gatemsg.SImageInfo
        """
        print("downloadToken:", imgDowloadToken.token)

    def onError(self, what, code):
        pass

    def onTimeout(self):
        pass

def updateImageTest():
    imageFile = "/Users/mahanzhou/Development/wechat_materials/2015.08.13/cover.jpg"

    proxy = ProxyManager.getProxy(apptype.GATE, "IPostOper")
    gateCB = IPostOperGetimageuploadtokensResponse(imageFile)

    print("Get a image upload token....")
    proxy.getImageUploadTokens(gateCB, "", 1)

def getDownloadToken():
    key = "e1a826f4-4d76-11e5-aed9-985aebccba40"
    gateCB = IPostOperGetimagedownloadtokensResponse()

    proxy = ProxyManager.getProxy(apptype.GATE, "IPostOper")

    proxy.getImageDownloadTokens(gateCB, "", key, "")

def imageTokeTest():
    # updateImageTest
    getDownloadToken()