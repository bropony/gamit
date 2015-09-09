"""
@author: mahanzhou
@date: 8/26/15
@file: 
@desc:

"""

from gamit.utils.myuuid import MyUuid
from gamit.log.logger import Logger
from message.gate.itest import ITest_Addsystopic_Response
from message.gate.ipostoper import IPostOper_Getimageuploadtokens_Response
from message.gate.gatemsg import SSysTopic
from message.common.publicdef import ESysTopicType
from staticdata.manager.TopicTagConfigManager import TopicTagConfigManager
import qiniu
from core.proxyhelper import ProxyHelper
import datetime

class AddSysTopicResponse(ITest_Addsystopic_Response):
    def __init__(self):
        super().__init__()

    def onResponse(self):
        Logger.log("AddSysTopicResponse.onResponse: Add SysTopic Success")

    def onError(self, what, code):
        Logger.log("AddSysTopicResponse.onError:", what, ", code:", code)

    def onTimeout(self):
        Logger.log("AddSysTopicResponse.onTimeout")

class GetImageUploadTokensResponse(IPostOper_Getimageuploadtokens_Response):
    """
    :type imgeList: list[str]
    """
    def __init__(self, imageList):
        super().__init__()

        self.imageList = imageList

    def onResponse(self, imageInfos):
        """
        :type imageInfos: list[message.gate.gatemsg.SImageInfo]
        """
        Logger.log("GetImageUploadTokensResponse.onReponse")
        newSysTopic = SSysTopic()
        newSysTopic.topicType = ESysTopicType.PlatformTopic
        newSysTopic.title = "啥也不想说"
        newSysTopic.content = "饿了就吃，困了就睡。" * 30
        newSysTopic.images.extend(imageInfos)

        newSysTopic.tags.extend(TopicTagConfigManager.getTagNamesByTagIdList([1, 2, 3, 4, 100, 101, 102, 103, '长沙', '成都', '上海']))

        idx = 0
        for token in imageInfos:
            ret, info = qiniu.put_file(token.token, token.imageKey, self.imageList[idx])
            print("[ImageUploaded] Key:{}\ntoken:{}\nhash:{}\ninfo:{}".format(
                token.imageKey, token.token, ret['hash'], info))
            idx += 1

        ProxyHelper.getITestProxy().addSysTopic(AddSysTopicResponse(), newSysTopic)

    def onError(self, what, code):
        Logger.log("GetImageUploadTokensResponse.onError:", what, ", code:", code)

    def onTimeout(self):
        Logger.log("GetImageUploadTokensResponse.onTimeout")

def addNewSysTopicTest():
    imageList = []
    imageList.append("/Users/mahanzhou/Development/wechat_materials/2015.09.05/004.jpg")
    imageList.append("/Users/mahanzhou/Development/wechat_materials/2015.09.05/005.jpg")
    imageList.append("/Users/mahanzhou/Development/wechat_materials/2015.09.05/003.jpg")

    Logger.log("Getting Image Upload Tokens...")
    ProxyHelper.getIPostOperProxy().getImageUploadTokens(GetImageUploadTokensResponse(imageList), "", len(imageList))

def getLatestSysTopicTest():
    tagId = "1"
    ProxyHelper.getIPostOperProxy().getLatestSysTopics(None, "xx", tagId, datetime.datetime.now() + datetime.timedelta(1), 10, "")