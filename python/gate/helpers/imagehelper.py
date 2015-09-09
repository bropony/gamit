"""
@author: mahanzhou
@date: 8/11/15
@file: 
@desc:

"""

import datetime

from dbutil.dbsaver import DbSaver, MongoDatabase
from gamit.utils.imagetoken import ImageToken
from message.gate.gatemsg import SImageInfo
from message.db.mongodb.usertables import TUserImage, SeqTUserImage
from gamit.log.logger import Logger

class ImageHelper:
    @classmethod
    def genImageDownloadToken(cls, imgKey, imageFormat=""):
        imgToke = SImageInfo()
        imgToke.token = ImageToken.downloadToken(imgKey)
        imgToke.formatedDownloadUrl = ImageToken.downloadToken(imgKey, imageFormat)
        imgToke.imageKey = imgKey
        imgToke.expireDt = datetime.datetime.now() + datetime.timedelta(0, ImageToken.getExpires())

        return imgToke

    @classmethod
    def genImageUploadToken(cls, imgKey):
        imgToke = SImageInfo()
        imgToke.token = ImageToken.uploadToken(imgKey)
        imgToke.imageKey = imgKey
        imgToke.expireDt = datetime.datetime.now() + datetime.timedelta(0, ImageToken.getExpires())

        return imgToke

    @classmethod
    def saveImages(cls, userEntity, imageKeys):
        """
        :type userEntity: user.userentity.UserEntity
        :type imageKeys: list[str]
        :rtype:
        """
        if not imageKeys:
            return

        userImages = SeqTUserImage()

        for imgKey in imageKeys:
            tUserImg = TUserImage()
            tUserImg.imgKey = imgKey
            tUserImg.isUploaded = False
            tUserImg.userId = userEntity.getUserId()

            userImages.append(tUserImg)

        DbSaver.saveTableBatch(userImages)

    @classmethod
    def imageUploaded(cls, imageKeys):
        tb = MongoDatabase.findTableByMessageType(TUserImage)
        if not tb:
            Logger.log("Table not Found: TUserImage")
            return

        for imgKey in imageKeys:
            tb.updateWithQuery({TUserImage.fn_imgKey: imgKey},
                               {"$set":{TUserImage.fn_isUploaded: True}},
                               upsert=False, update_one=True)
