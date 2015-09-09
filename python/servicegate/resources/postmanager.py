"""
@author: mahanzhou
@date: 8/5/15
@file: 
@desc:
"""

import datetime
from gamit.log.logger import Logger
from resources.post import WUserPost
from message.gate.gatemsg import SeqUserPost

from message.gate.gatemsg import SUserPost

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
        self.maxCachedNum = 100000
        self.notUploadedImageMap = {}

    def addPosts(self, postList, pushback=True):
        """
        :type postList: list[message.db.mongodb.posttables.TUserPost]
        """

        newPostList = []
        for post in postList:
            wup = WUserPost(post)
            self.postMap[post.postId] = wup

            newPostList.append(wup)

            self.__updateUserPostStatsus(post.userId, post.postId, pushback)

        if pushback:
            self.sortedByDt.extend(newPostList)
        else:
            newPostList.extend(self.sortedByDt)
            self.sortedByDt = newPostList

    def addNewPost(self, post):
        """
        :type post: message.db.mongodb.posttables.TUserPost
        """
        wup = WUserPost(post)
        self.postMap[post.postId] = wup
        self.sortedByDt.insert(0, wup)

        self.__updateUserPostStatsus(post.userId, post.postId, False)

    def __updateUserPostStatsus(self, userId, postId, pushBack):
        if userId not in self.userPostIdMap:
            self.userPostIdMap[userId] = []

        if pushBack:
            self.userPostIdMap[userId].append(postId)
        else:
            self.userPostIdMap[userId].insert(0, postId)

    def isCacheFull(self):
        """
        :rtype: bool
        """
        return (self.maxCachedNum <= len(self.postMap))

    def __findPostIndexBeforeDate(self, latestPostDt):
        if len(self.sortedByDt) < 10:
            index = 0
            for post in self.sortedByDt:
                if post.getCreateDt() < latestPostDt:
                    return index
                index += 1
            return -1

        if not self.sortedByDt:
            return -1

        if latestPostDt > self.sortedByDt[0].getCreateDt():
            return 0

        if latestPostDt < self.sortedByDt[-1].getCreateDt():
            return -1

        start = 1
        end = len(self.sortedByDt) - 1

        while True:
            if end < start:
                break

            middle = int((start + end) / 2)
            middleDt = self.sortedByDt[middle].getCreateDt()
            if middleDt >= latestPostDt:
                start = middle + 1
                continue

            if middleDt < latestPostDt:
                if self.sortedByDt[middle - 1].getCreateDt() >= latestPostDt:
                    return middle
                end = middle - 1

        Logger.log("__findPostIndexBeforeDate", "Unexpected Error.")
        return -1

    def findPostsByInDtOrder(self, tag, latestPostDt, targetNum, imgFormat):
        """
        :type tag: str
        :type latestPostDt: datetime.datetime
        :type targetNum: int
        :return: list[SUserPost]
        """

        startPostIndex = self.__findPostIndexBeforeDate(latestPostDt)

        if startPostIndex < 0:
            return SeqUserPost()

        targetNum = targetNum if (targetNum <= self.maxCachedNum) else self.maxCachedNum
        totalPostNum = len(self.sortedByDt)

        res = SeqUserPost()
        currentIndex = startPostIndex
        while True:
            if currentIndex >= totalPostNum:
                break

            post = self.sortedByDt[currentIndex]
            if not post.areAllImagesUploaded():
                continue

            res.append(post.getClientInfo(imgFormat))
            if len(res) >= targetNum:
                break

            currentIndex += 1

        return res

    def getNewestPosts(self, tag, dtThres, targetNum, imgFormat):
        """
        :type tag: str
        :type dtThres: datetime.datetime
        :type targetNum: int
        :return: list[SUserPost]
        """

        targetNum = targetNum if (targetNum <= self.maxCachedNum) else self.maxCachedNum

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

    def findPostByPostId(self, postId):
        """
        :type postId: str
        :rtype: WUserPost
        """
        if postId in self.postMap:
            return self.postMap[postId]
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

            if postId not in postMap:
                postMap[postId] = userPost

            postMap[postId].getTUserPost().imgageUploadedNum += 1

        res = [userPost.getTUserPost() for (postId, userPost) in postMap.items()]
        return res

PostManager = __PostManager()
