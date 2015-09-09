"""
@author: mahanzhou
@date: 8/4/15
@file: 
@desc:

"""

import threading
import queue

class TaskThread(threading.Thread):
    def __init__(self):
        super().__init__()

        self.__tasks = []
        self.__q = queue.Queue()
        self.__item = 1

        self.__q.put(self.__item)

    def run(self):
        self.__q.get()

        pass