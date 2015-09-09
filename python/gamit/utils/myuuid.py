__author__ = 'mahanzhou'

import uuid

class MyUuid:
    @staticmethod
    def getUuid():
        return str(uuid.uuid1())