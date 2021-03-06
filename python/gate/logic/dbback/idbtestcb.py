"""
* @name idbtestcb.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/10 10:40
*
* @desc idbtestcb.py
"""
from gamit.log.logger import Logger
from message.db.idbtest import IDbTest_Sayhello_Response
from settings.servant import ServantSetting

class IDbTest_Sayhello_callback(IDbTest_Sayhello_Response):
    def onResponse(self, world):
        Logger.logInfo("IDbTest_Sayhello_callback.onResponse",
                       "Success: ", world.passedTimes, "channelId:", ServantSetting.getChannelId())

    def onError(self, what, code):
        Logger.logInfo("IDbTest_Sayhello_callback.onError", "{}, {}".format(what, code))

    def onTimeout(self):
        Logger.logInfo("IDbTest_Sayhello_callback", "Timeout")
