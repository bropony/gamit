"""
* @name idbtestimpl.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/10 10:21
*
* @desc idbtestimpl.py
"""

from message.db.idbtest import IDbTestServant
from message.db.main_db import AnRmiTest
from gamit.mongodb.database import MongoDatabase

class IDbTestImpl(IDbTestServant):
    def __init__(self, name):
        super().__init__(name)

    def sayhello(self, hello, _request):
        table = MongoDatabase.findTableByMessageType(AnRmiTest)
        if not table:
            raise Exception("Table Not Found")
        table.update(hello)

        res = table.findOne(hello.ip)
        if not res:
            raise Exception("Db Engine Error")

        _request.response(res)