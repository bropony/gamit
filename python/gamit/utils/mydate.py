__author__ = 'mahanzhou'

import datetime

class MyDate:
    @classmethod
    def getOldDt(cls):
        return datetime.datetime(1980, 1, 1, 0, 0, 0)

    @classmethod
    def getFairyDt(cls):
        return datetime.datetime(2000, 1, 1, 0, 0, 0)
