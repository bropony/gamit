"""
@author: mahanzhou
@date: 8/11/15
@file: 
@desc:

"""

import datetime

from helpers.dbcachehelper import DbCacheHelper
from gamit.utils.imagetoken import ImageToken
from message.gate.gatemsg import SImageInfo
from message.db.mongodb.usertables import TUserImage, SeqTUserImage

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

        DbCacheHelper.getITableSaverProxy().saveUserImages(None, userImages)
