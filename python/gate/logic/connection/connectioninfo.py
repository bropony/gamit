__author__ = 'mahanzhou'

class ConnectionInfo:
    _isDbCacheOpen = False
    _isDbLogOpen = False
    _isAllUserDataLoaded = False

    @classmethod
    def setDbCacheOpen(cls, isOpen):
        cls._isDbCacheOpen = isOpen

    @classmethod
    def isDbCacheOpen(cls):
        return cls._isDbCacheOpen

    @classmethod
    def setDbLogOpen(cls, isOpen):
        cls._isDbLogOpen = isOpen

    @classmethod
    def isDbLogOpen(cls):
        return cls._isDbLogOpen

    @classmethod
    def setUserDataLoaded(cls, isLoaded):
        cls._isAllUserDataLoaded = isLoaded

    @classmethod
    def isAllUserDataLoaded(cls):
        return cls._isAllUserDataLoaded
###