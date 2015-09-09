"""
@author: mahanzhou
@date: 9/9/15
@file: 
@desc:

"""

from message.gate.itaileroper import ITailerOperServant
from message.gate.tailermsg import SeqMyTailerOrder, SeqTailerOrder

class ITailerOperImpl(ITailerOperServant):
    def __init__(self):
        super().__init__()

    def newTailerOrder(self, sessionKey, orderParams, _request):
        """
        :type sessionKey: str
        :type orderParams: message.gate.itaileroper.SNewOrderParams
        :type _request: message.gate.itaileroper.ITailerOper_Newtailerorder_Request
        """
        _request.response("")

    def getMyTailerOrdrList(self, sessionKey, pageIndex, _request):
        """
        :type sessionKey: str
        :type pageIndex: int
        :type _request: message.gate.itaileroper.ITailerOper_Getmytailerordrlist_Request
        """
        res = SeqMyTailerOrder()
        _request.response(res)

    def getLatestTailerOrderList(self, sessionKey, latestOrderDt, targetNum, _request):
        """
        :type sessionKey: str
        :type latestOrderDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.itaileroper.ITailerOper_Getlatesttailerorderlist_Request
        """
        res = SeqTailerOrder()
        _request.response(res)

    def getOlderTailerOrderList(self, sessionKey, oldestOrderDt, targetNum, _request):
        """
        :type sessionKey: str
        :type oldestOrderDt: datetime.datetime
        :type targetNum: int
        :type _request: message.gate.itaileroper.ITailerOper_Getoldertailerorderlist_Request
        """
        res = SeqTailerOrder()
        _request.response(res)
