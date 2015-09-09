"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:
"""

import datetime
from staticdata.serverconfig import ServerConfigManager
from social.post import WUserPost
from message.gate.gatemsg import SeqUserPost, SUserPost
from message.db.mongodb.posttables import TUserPost
from gamit.mongodb.database import MongoDatabase
from gamit.log.logger import Logger

class __PostManager:
    """
    :type postMap: dict[str, WUserPost]
    :type sortedByDt: list[WUserPost]
    :type userPostIdMap: dict[str, list[str]]
    :type notUploadedImageMap: dict[str, str]
    """
    def __init__(self):
        self.maxTargetNum = 20 #

        self.postMap = {}
        self.userPostIdMap = {}
        self.sortedByDt = []

        if not ServerConfigManager.isDebug:
            self.maxCachedNum = 100000
        else:
            self.maxCachedNum = 1000

        self.notUploadedImageMap = {}

    def loadPosts(self):
        if self.postMap:
            return

        tb = MongoDatabase.findTableByMessageType(TUserPost)
        if not tb:
            Logger.log("table TUserPost not found")
            return

        tPostList = tb.findManyWithQuey({}, sort=MongoDatabase.SortByIdDesc, limit=self.maxCachedNum)
        for tPost in tPostList:
            wup = WUserPost(tPost)
            self.postMap[tPost.postId] = wup
            self.sortedByDt.append(wup)

            self.__updateUserPostStatsus(tPost.userId, tPost.postId, True)

        Logger.log("Num of TUserPost Loaded:", len(tPostList))

    def addNewPost(self, post):
        """
        :type post: message.db.mongodb.posttables.TUserPost
        """
        wup = WUserPost(post)
        self.postMap[post.postId] = wup
        self.sortedByDt.insert(0, wup)

        self.__updateUserPostStatsus(post.userId, post.postId, False)

        if len(self.sortedByDt) > self.maxCachedNum:
            postId = self.sortedByDt[-1].getPostId()
            userId = self.sortedByDt[-1].getOwnerUserId()

            if postId in self.postMap:
                del self.postMap[postId]
            del self.sortedByDt[-1]

            self.__delUserPostId(userId, postId)

    def __updateUserPostStatsus(self, userId, postId, pushBack):
        if userId not in self.userPostIdMap:
            self.userPostIdMap[userId] = []

        if pushBack:
            self.userPostIdMap[userId].append(postId)
        else:
            self.userPostIdMap[userId].insert(0, postId)

    def __delUserPostId(self, userId, postId):
        if userId not in self.userPostIdMap:
            return
        postIdList = self.userPostIdMap[userId]
        if postId in postIdList:
            postIdList.remove(postId)

    def getNewestPosts(self, tag, dtThres, targetNum, imgFormat):
        """
        :type tag: str
        :type dtThres: datetime.datetime
        :type targetNum: int
        :return: list[SUserPost]
        """

        targetNum = targetNum if (targetNum <= self.maxTargetNum) else self.maxTargetNum

        res = SeqUserPost()
        if dtThres < datetime.datetime.now():
            for post in self.sortedByDt:
                if not post.areAllImagesUploaded():
                    continue

                if post.getCreateDt() > dtThres:
                    res.append(post.getClientInfo(imgFormat))
                else:
                    break

                if len(res) >= targetNum:
                    break
        else:
            for post in self.sortedByDt:
                if not post.areAllImagesUploaded():
                    continue

                res.append(post.getClientInfo(imgFormat))
                if len(res) >= targetNum:
                    break

        return res

    def getOlderPosts(self, tag, dtThres, targetNum, imgFormat):
        """
        :type tag: str
        :type dtThres: datetime.datetime
        :type targetNum: int
        :return: list[SUserPost]
        """

        targetNum = targetNum if (targetNum <= self.maxTargetNum) else self.maxTargetNum

        res = SeqUserPost()
        for wuPost in self.sortedByDt:
            if wuPost.getCreateDt() >= dtThres:
                continue

            if wuPost.areAllImagesUploaded():
                res.append(wuPost.getClientInfo(imgFormat))

            if len(res) >= targetNum:
                break

        resSize = len(res)
        if resSize >= targetNum:
            return res

        limit = targetNum - resSize

        tPostList = []
        tb = MongoDatabase.findTableByMessageType(TUserPost)
        if tb:
            tPostList = tb.findManyWithQuey({TUserPost.fn_createDt: {"$lt": dtThres}},
                                            limit=limit,
                                            sort=MongoDatabase.SortByIdDesc)

        for tPost in tPostList:
            wuPost = WUserPost(tPost)
            if wuPost.areAllImagesUploaded():
                res.append(wuPost)

    def findPostByPostId(self, postId):
        """
        :type postId: str
        :rtype: WUserPost
        """

        if postId in self.postMap:
            return self.postMap[postId]

        tb = MongoDatabase.findTableByMessageType(TUserPost)
        if tb:
            tPost = tb.findOne(postId)
            if tPost:
                return WUserPost(tPost)

        return None

    def addImageKeysToUpload(self, postId, imageKeys):
        """
        :type imageKeys: list[str]
        """
        for imgKey in imageKeys:
            self.notUploadedImageMap[imgKey] = postId

    def didImageUpload(self, imageKeys):
        """
        :type imageKeys: list[str]
        :rtype: list[WUserPost]
        """
        postMap = {}
        for imgKey in imageKeys:
            postId = ""
            if imgKey not in self.notUploadedImageMap:
                continue
            else:
                postId = self.notUploadedImageMap[imgKey]
                del self.notUploadedImageMap[imgKey]

            userPost = self.findPostByPostId(postId)
            if not userPost:
                continue

            postMap[postId] = userPost
            userPost.getTUserPost().imgageUploadedNum += 1

        res = [userPost.getTUserPost() for (postId, userPost) in postMap.items()]
        return res

    def getUserPostListByUserId(self, userId, dtThreshold, targetNum, imgForat, userPostNum):
        """
        :type userId: str
        :type targetNum: int
        :type imgForat: str
        :type userPostNum: int
        :rtype: list[SUserPost]
        """

        targetNum = targetNum if (targetNum <= self.maxTargetNum) else self.maxTargetNum
        oldestDt = dtThreshold

        resPostList = SeqUserPost()

        if not userPostNum:
            return resPostList

        cachedPostIdList = []
        if userId in self.userPostIdMap:
            cachedPostIdList = self.userPostIdMap[userId]

        for postId in cachedPostIdList:
            if postId not in self.postMap:
                Logger.log("getUserPostListByUserId. PostId not found in postMap")
                continue

            wuPost = self.postMap[postId]
            if wuPost.getCreateDt() < dtThreshold:
                resPostList.append(wuPost.getClientInfo(imgForat))

                if oldestDt > wuPost.getCreateDt():
                    oldestDt = wuPost.getCreateDt()

                if len(resPostList) >= targetNum:
                    break

        if len(resPostList) >= targetNum:
            return resPostList

        if len(cachedPostIdList) >= userPostNum:
            return resPostList

        limit = targetNum - len(resPostList)
        tPostList = []
        tb = MongoDatabase.findTableByMessageType(TUserPost)
        if tb:
            query = {TUserPost.fn_userId: userId,
                     TUserPost.fn_createDt: {"$lt": oldestDt}}

            tPostList = tb.findManyWithQuey(query, limit=limit, sort=MongoDatabase.SortByIdDesc)

        for tPost in tPostList:
            wuPost = WUserPost(tPost)
            resPostList.append(wuPost.getClientInfo(imgForat))

        return resPostList

    def deleteUserPost(self, postId):
        if not postId in self.postMap:
            return

        userId = self.postMap[postId].getOwnerUserId()
        self.__delUserPostId(userId, postId)

        for idx in range(len(self.sortedByDt)):
            userPost = self.sortedByDt[idx]
            if userPost.getPostId() == postId:
                del self.sortedByDt[idx]
                break

        del self.postMap[postId]

PostManager = __PostManager()
