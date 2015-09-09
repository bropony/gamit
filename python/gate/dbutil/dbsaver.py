"""
@author: mahanzhou
@date: 9/4/15
@file: 
@desc:

"""

from gamit.log.logger import Logger
from gamit.mongodb.database import MongoDatabase

class DbSaver:
    @classmethod
    def saveTable(cls, data):
        tb = MongoDatabase.findTableByMessageObj(data)

        if not tb:
            Logger.log("DbSaver.saveTable. Table not found:", data.__class__.__name__)
            return

        tb.update(data)

    @classmethod
    def saveTableBatch(cls, dataList):
        if not dataList:
            return

        tb = MongoDatabase.findTableByMessageObj(dataList[0])

        if not tb:
            Logger.log("DbSaver.saveTable. Table not found:", dataList[0].__class__.__name__)
            return

        tb.update(dataList)

    @classmethod
    def deleteFromTable(cls, tableType, filter):
        tb = MongoDatabase.findTableByMessageType(tableType)

        if not tb:
            Logger.log("DbSaver.delteFromTable. Table not found:", tableType.__name__)
            return

        tb.delete(filter, delete_one=True)

    @classmethod
    def deleteFromTableBatch(cls, tableType, filter):
        tb = MongoDatabase.findTableByMessageType(tableType)

        if not tb:
            Logger.log("DbSaver.delteFromTable. Table not found:", tableType.__name__)
            return

        tb.delete(filter, delete_one=False)
