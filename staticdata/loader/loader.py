"""
* @name loader
*
* @author ahda86@gmail.com
*
* @date 2015/6/11 14:44
*
* @desc loader
"""

import json

def loadfile(jsFile, loader):
    fjs = open(jsFile, encoding='utf8')
    js = json.load(fjs)
    print(js)
    fjs.close()

    res = loader(js)

    for r in res:
        for key, val in r.__dict__.items():
            print("'{}': '{}'".format(key, val))

    return res
