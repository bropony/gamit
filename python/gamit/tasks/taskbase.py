"""
@author: mahanzhou
@date: 8/4/15
@file: 
@desc:

"""

import abc

class TaskBase(metaclass=abc.ABCMeta):
    def __init__(self, *argv, **kwarg):
        self.argv = argv
        self.kwarg = kwarg

    @abc.abstractmethod
    def onTaskRun(self):
        pass

    @abc.abstractmethod
    def onTaskDone(self):
        pass