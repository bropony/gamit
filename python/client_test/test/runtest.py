"""
* @name runtest.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 19:56
*
* @desc runtest.py
"""

from gamit.log.logger import Logger
from gamit.rmi.proxymanager import ProxyManager
from gamit.app import apptype as AppType
from gamit.message.messagemanager import MessageManager
from test.ILoginTest import runILoginTest
from test.UploadImageTest import imageTokeTest
from test.NewSysTopicTest import addNewSysTopicTest, getLatestSysTopicTest


def runTest():
    # runILoginTest()
    # imageTokeTest()
    addNewSysTopicTest()
    # getLatestSysTopicTest()

