"""
* @name singleton.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/3 19:49
*
* @desc For simple singleton pattern implementation.
*       Subclasses of class Singleton cannot be initiated.
*       All members and methods are suggested to be class members and methods.
"""

class Singleton:
    def __init__(self):
        raise Exception("Initiation of singleton is not allowed")
######