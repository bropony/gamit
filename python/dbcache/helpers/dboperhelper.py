"""
@author: mahanzhou
@date: 8/8/15
@file: 
@desc:

"""

from gamit.mongodb.database import MongoDatabase
from staticdata.manager.ErrorCodeManager import ErrorCodeManager

class DbOperHelper:
    @staticmethod
    def generalUpdate(data, request=None):
        tb = MongoDatabase.findTableByMessageObj(data)

        if tb:
            tb.update(data)
        else:
            error = ErrorCodeManager.getError("ErrorDb_TableNotFound")
            request.error(error.what, error.code)
            return

        if request:
            request.response()

    @staticmethod
    def generalError(request, errorName):
        error = ErrorCodeManager.getError("ErrorDb_TableNotFound")
        request.error(error.what, error.code)
