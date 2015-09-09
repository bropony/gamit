__author__ = 'mahanzhou'

import abc
import datetime

class _TimerIdBase:
    _timerId = 0
    @classmethod
    def getTimerId(cls):
        cls._timerId += 1
        return cls._timerId

class TimerBase(metaclass=abc.ABCMeta):
    def __init__(self):
        self._id = _TimerIdBase.getTimerId()

    def getId(self):
        return self._id

    @abc.abstractmethod
    def handleTimeout(self, data):
        pass

class TimerProxy:
    def __init__(self, timer, data, future, interval):
        self.timer = timer
        self.data = data
        self.future = future
        self.scheduledTimes = 0
        self.interval = interval

    def handleTimeout(self):
        now = datetime.datetime.now()
        if now >= self.future:
            self.timer.handleTimeout(self.data)
            self.scheduledTimes += 1
        else:
            return True

        if self.interval.total_seconds() > 0:
            while self.future <= now:
                self.future += self.interval
            return True
        else:
            return False
#####