__author__ = 'mahanzhou'

import hashlib

class Md5Hash:
    @staticmethod
    def md5sum(src):
        m = hashlib.md5()
        if isinstance(src, bytes):
            m.update(src)
        elif isinstance(src ,str):
            m.update(bytes(src, 'utf8'))

        return m.hexdigest()

    @staticmethod
    def encryptPassword(pswd):
        return Md5Hash.md5sum(pswd)

