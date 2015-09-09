#
# file: iuserinfo.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *
from gamit.rmi.rmicore import *
from gamit.serialize.serializer import Serializer
from gamit.serialize.datatype import RmiDataType
import abc
import message.common.publicdef
import message.common.publicmsg
import message.gate.gateconst
import message.gate.gatemsg


class IUserInfo_Getmydetails_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, myDetails):
        if not isinstance(myDetails, message.gate.gatemsg.SMyDetailInfo):
            raise Exception("myDetails must be instance of message.gate.gatemsg.SMyDetailInfo", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        myDetails._write(_os)

        self.sendout()

class IUserInfo_Getfamilymembers_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, familyMembers):
        if not isinstance(familyMembers, message.gate.gatemsg.SeqFamilyMember):
            raise Exception("familyMembers must be instance of message.gate.gatemsg.SeqFamilyMember", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        familyMembers._write(_os)

        self.sendout()

class IUserInfo_Changenickname_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IUserInfo_Changeavatar_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IUserInfo_Updategender_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IUserInfo_Updatebirthday_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IUserInfo_Updatefamilymembers_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IUserInfo_Removefamilymember_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IUserInfo_Updateadress_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, newAddressIndex):
        if not isinstance(newAddressIndex, int):
            raise Exception("newAddressIndex must be instance of int", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        _os.writeInt(newAddressIndex)

        self.sendout()

class IUserInfo_Getaddresslist_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, addressList):
        if not isinstance(addressList, message.common.publicmsg.SeqAddress):
            raise Exception("addressList must be instance of message.common.publicmsg.SeqAddress", 0)

        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)
        addressList._write(_os)

        self.sendout()

class IUserInfo_Setdefaultaddress_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IUserInfo_Deleteaddress_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        if not self.msgId:
            return

        _os = self._os
        _os.writeInt(self.msgId)

        self.sendout()

class IUserInfo_Getmydetails_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        myDetails = message.gate.gatemsg.SMyDetailInfo()
        myDetails._read(_is)

        self.onResponse(myDetails)

    @abc.abstractmethod
    def onResponse(self, myDetails):
        """
        :type myDetails: message.gate.gatemsg.SMyDetailInfo
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfo_Getfamilymembers_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        familyMembers = message.gate.gatemsg.SeqFamilyMember()
        familyMembers._read(_is)

        self.onResponse(familyMembers)

    @abc.abstractmethod
    def onResponse(self, familyMembers):
        """
        :type familyMembers: list[message.gate.gatemsg.SFamilyMember]
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfo_Changenickname_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfo_Changeavatar_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfo_Updategender_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfo_Updatebirthday_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfo_Updatefamilymembers_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfo_Removefamilymember_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfo_Updateadress_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        newAddressIndex = int()
        newAddressIndex = _is.readInt()

        self.onResponse(newAddressIndex)

    @abc.abstractmethod
    def onResponse(self, newAddressIndex):
        """
        :type newAddressIndex: int
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfo_Getaddresslist_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        addressList = message.common.publicmsg.SeqAddress()
        addressList._read(_is)

        self.onResponse(addressList)

    @abc.abstractmethod
    def onResponse(self, addressList):
        """
        :type addressList: list[message.common.publicmsg.SAddress]
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfo_Setdefaultaddress_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfo_Deleteaddress_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        """
        """
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        """
        :type what: str
        :type code: int
        """
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IUserInfoServant(RmiServant):
    def __init__(self, name='IUserInfo'):
        super().__init__(name)
        self.methodMap['getMyDetails'] = self._getMyDetails
        self.methodMap['getFamilyMembers'] = self._getFamilyMembers
        self.methodMap['changeNickname'] = self._changeNickname
        self.methodMap['changeAvatar'] = self._changeAvatar
        self.methodMap['updateGender'] = self._updateGender
        self.methodMap['updateBirthDay'] = self._updateBirthDay
        self.methodMap['updateFamilyMembers'] = self._updateFamilyMembers
        self.methodMap['removeFamilyMember'] = self._removeFamilyMember
        self.methodMap['updateAdress'] = self._updateAdress
        self.methodMap['getAddressList'] = self._getAddressList
        self.methodMap['setDefaultAddress'] = self._setDefaultAddress
        self.methodMap['deleteAddress'] = self._deleteAddress

    def _getMyDetails(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        _request = IUserInfo_Getmydetails_Request(_connId, _msgId, self)
        self.getMyDetails(sessionKey, _request)

    def _getFamilyMembers(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        _request = IUserInfo_Getfamilymembers_Request(_connId, _msgId, self)
        self.getFamilyMembers(sessionKey, _request)

    def _changeNickname(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        newNickname = str()
        newNickname = _is.readString()
        _request = IUserInfo_Changenickname_Request(_connId, _msgId, self)
        self.changeNickname(sessionKey, newNickname, _request)

    def _changeAvatar(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        newAvatar = str()
        newAvatar = _is.readString()
        _request = IUserInfo_Changeavatar_Request(_connId, _msgId, self)
        self.changeAvatar(sessionKey, newAvatar, _request)

    def _updateGender(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        gender = message.common.publicdef.EGender.Unknown
        gender = _is.readInt()
        _request = IUserInfo_Updategender_Request(_connId, _msgId, self)
        self.updateGender(sessionKey, gender, _request)

    def _updateBirthDay(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        birthday = datetime.datetime.now()
        birthday = _is.readDate()
        _request = IUserInfo_Updatebirthday_Request(_connId, _msgId, self)
        self.updateBirthDay(sessionKey, birthday, _request)

    def _updateFamilyMembers(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        familyMembers = message.gate.gatemsg.SeqFamilyMember()
        familyMembers._read(_is)
        _request = IUserInfo_Updatefamilymembers_Request(_connId, _msgId, self)
        self.updateFamilyMembers(sessionKey, familyMembers, _request)

    def _removeFamilyMember(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        indexes = message.common.publicdef.SeqInt()
        indexes._read(_is)
        _request = IUserInfo_Removefamilymember_Request(_connId, _msgId, self)
        self.removeFamilyMember(sessionKey, indexes, _request)

    def _updateAdress(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        addressInfo = message.common.publicmsg.SAddress()
        addressInfo._read(_is)
        _request = IUserInfo_Updateadress_Request(_connId, _msgId, self)
        self.updateAdress(sessionKey, addressInfo, _request)

    def _getAddressList(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        _request = IUserInfo_Getaddresslist_Request(_connId, _msgId, self)
        self.getAddressList(sessionKey, _request)

    def _setDefaultAddress(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        addressIndex = int()
        addressIndex = _is.readInt()
        _request = IUserInfo_Setdefaultaddress_Request(_connId, _msgId, self)
        self.setDefaultAddress(sessionKey, addressIndex, _request)

    def _deleteAddress(self, _connId, _msgId, _is):
        sessionKey = str()
        sessionKey = _is.readString()
        addressIndex = int()
        addressIndex = _is.readInt()
        _request = IUserInfo_Deleteaddress_Request(_connId, _msgId, self)
        self.deleteAddress(sessionKey, addressIndex, _request)


    @abc.abstractmethod
    def getMyDetails(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.iuserinfo.IUserInfo_Getmydetails_Request
        """
        pass

    @abc.abstractmethod
    def getFamilyMembers(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.iuserinfo.IUserInfo_Getfamilymembers_Request
        """
        pass

    @abc.abstractmethod
    def changeNickname(self, sessionKey, newNickname, _request):
        """
        :type sessionKey: str
        :type newNickname: str
        :type _request: message.gate.iuserinfo.IUserInfo_Changenickname_Request
        """
        pass

    @abc.abstractmethod
    def changeAvatar(self, sessionKey, newAvatar, _request):
        """
        :type sessionKey: str
        :type newAvatar: str
        :type _request: message.gate.iuserinfo.IUserInfo_Changeavatar_Request
        """
        pass

    @abc.abstractmethod
    def updateGender(self, sessionKey, gender, _request):
        """
        :type sessionKey: str
        :type gender: int
        :type _request: message.gate.iuserinfo.IUserInfo_Updategender_Request
        """
        pass

    @abc.abstractmethod
    def updateBirthDay(self, sessionKey, birthday, _request):
        """
        :type sessionKey: str
        :type birthday: datetime.datetime
        :type _request: message.gate.iuserinfo.IUserInfo_Updatebirthday_Request
        """
        pass

    @abc.abstractmethod
    def updateFamilyMembers(self, sessionKey, familyMembers, _request):
        """
        :type sessionKey: str
        :type familyMembers: list[message.gate.gatemsg.SFamilyMember]
        :type _request: message.gate.iuserinfo.IUserInfo_Updatefamilymembers_Request
        """
        pass

    @abc.abstractmethod
    def removeFamilyMember(self, sessionKey, indexes, _request):
        """
        :type sessionKey: str
        :type indexes: list[int]
        :type _request: message.gate.iuserinfo.IUserInfo_Removefamilymember_Request
        """
        pass

    @abc.abstractmethod
    def updateAdress(self, sessionKey, addressInfo, _request):
        """
        :type sessionKey: str
        :type addressInfo: message.common.publicmsg.SAddress
        :type _request: message.gate.iuserinfo.IUserInfo_Updateadress_Request
        """
        pass

    @abc.abstractmethod
    def getAddressList(self, sessionKey, _request):
        """
        :type sessionKey: str
        :type _request: message.gate.iuserinfo.IUserInfo_Getaddresslist_Request
        """
        pass

    @abc.abstractmethod
    def setDefaultAddress(self, sessionKey, addressIndex, _request):
        """
        :type sessionKey: str
        :type addressIndex: int
        :type _request: message.gate.iuserinfo.IUserInfo_Setdefaultaddress_Request
        """
        pass

    @abc.abstractmethod
    def deleteAddress(self, sessionKey, addressIndex, _request):
        """
        :type sessionKey: str
        :type addressIndex: int
        :type _request: message.gate.iuserinfo.IUserInfo_Deleteaddress_Request
        """
        pass

# message.gate.iuserinfo.IUserInfoProxy
class IUserInfoProxy(RmiProxy):
    def __init__(self, name='IUserInfo'):
        super().__init__(name)

    def getMyDetails(self, _response, sessionKey):
        """
        :type _response: IUserInfo_Getmydetails_Response
        :type sessionKey: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getMyDetails')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        self.invoke(_os, _response)

    def getFamilyMembers(self, _response, sessionKey):
        """
        :type _response: IUserInfo_Getfamilymembers_Response
        :type sessionKey: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getFamilyMembers')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        self.invoke(_os, _response)

    def changeNickname(self, _response, sessionKey, newNickname):
        """
        :type _response: IUserInfo_Changenickname_Response
        :type sessionKey: str
        :type newNickname: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('changeNickname')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(newNickname)
        self.invoke(_os, _response)

    def changeAvatar(self, _response, sessionKey, newAvatar):
        """
        :type _response: IUserInfo_Changeavatar_Response
        :type sessionKey: str
        :type newAvatar: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('changeAvatar')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeString(newAvatar)
        self.invoke(_os, _response)

    def updateGender(self, _response, sessionKey, gender):
        """
        :type _response: IUserInfo_Updategender_Response
        :type sessionKey: str
        :type gender: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateGender')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeInt(gender)
        self.invoke(_os, _response)

    def updateBirthDay(self, _response, sessionKey, birthday):
        """
        :type _response: IUserInfo_Updatebirthday_Response
        :type sessionKey: str
        :type birthday: datetime.datetime
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateBirthDay')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeDate(birthday)
        self.invoke(_os, _response)

    def updateFamilyMembers(self, _response, sessionKey, familyMembers):
        """
        :type _response: IUserInfo_Updatefamilymembers_Response
        :type sessionKey: str
        :type familyMembers: list[message.gate.gatemsg.SFamilyMember]
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateFamilyMembers')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        familyMembers._write(_os)
        self.invoke(_os, _response)

    def removeFamilyMember(self, _response, sessionKey, indexes):
        """
        :type _response: IUserInfo_Removefamilymember_Response
        :type sessionKey: str
        :type indexes: list[int]
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('removeFamilyMember')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        indexes._write(_os)
        self.invoke(_os, _response)

    def updateAdress(self, _response, sessionKey, addressInfo):
        """
        :type _response: IUserInfo_Updateadress_Response
        :type sessionKey: str
        :type addressInfo: message.common.publicmsg.SAddress
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('updateAdress')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        addressInfo._write(_os)
        self.invoke(_os, _response)

    def getAddressList(self, _response, sessionKey):
        """
        :type _response: IUserInfo_Getaddresslist_Response
        :type sessionKey: str
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getAddressList')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        self.invoke(_os, _response)

    def setDefaultAddress(self, _response, sessionKey, addressIndex):
        """
        :type _response: IUserInfo_Setdefaultaddress_Response
        :type sessionKey: str
        :type addressIndex: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('setDefaultAddress')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeInt(addressIndex)
        self.invoke(_os, _response)

    def deleteAddress(self, _response, sessionKey, addressIndex):
        """
        :type _response: IUserInfo_Deleteaddress_Response
        :type sessionKey: str
        :type addressIndex: int
        """

        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('deleteAddress')
        if _response:
            _msgId = self.getMsgId()
            _os.writeInt(_msgId)
            _response._setMsgId(_msgId)
        else:
            _os.writeInt(0)

        _os.writeString(sessionKey)
        _os.writeInt(addressIndex)
        self.invoke(_os, _response)


