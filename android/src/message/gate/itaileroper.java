/*
* @filename itaileroper.java
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

package message.gate;


import java.util.Date;
import java.util.HashMap;
import java.util.Set;
import java.util.Iterator;

import rmi.Serializer;
import rmi.MessageBlock;
import rmi.RmiCore;
import rmi.ProxyManager;
import rmi.RmiManager;
import rmi.RmiErrorDefaultHandler;
import message.common.publicdef;
import message.common.publicmsg;
import message.gate.gateconst;
import message.gate.gatemsg;
import message.gate.tailermsg;


public class itaileroper
{
    // class SNewOrderParams
    public static class SNewOrderParams extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SNewOrderParams();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SNewOrderParams", new AutoRegist());
        }

        public int orderType;
        public String title;
        public String content;
        public publicdef.SeqString imageKeys;
        public publicdef.SeqString tags;

        public SNewOrderParams()
        {
            orderType = gateconst.ETailerOrderType.NoneType;
            title = "";
            content = "";
            imageKeys = new publicdef.SeqString();
            tags = new publicdef.SeqString();
        }

        @Override
        public void __read(Serializer __is)
        {
            orderType = __is.readInt();
            title = __is.read(title);
            content = __is.read(content);
            imageKeys.__read(__is);
            tags.__read(__is);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(orderType);
            __os.write(title);
            __os.write(content);
            imageKeys.__write(__os);
            tags.__write(__os);
        }
    } // end of class SNewOrderParams

    // Reponse ITailerOper_newTailerOrder_response
    public static abstract class ITailerOper_newTailerOrder_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public ITailerOper_newTailerOrder_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            String orderId = "";
            orderId = __is.read(orderId);

            onResponse(orderId);
        }

        @Override
        public void __onError(String what, int code)
        {
            onError(what, code);

            if (useDefaultErrorHandler)
            {
                RmiErrorDefaultHandler.onError(what, code);
            }
        }

        @Override
        public void __onTimeout()
        {
            onTimeout();
        }

        public abstract void onResponse(String orderId);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse ITailerOper_getMyTailerOrdrList_response
    public static abstract class ITailerOper_getMyTailerOrdrList_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public ITailerOper_getMyTailerOrdrList_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            tailermsg.SeqMyTailerOrder orderList = new tailermsg.SeqMyTailerOrder();
            orderList.__read(__is);

            onResponse(orderList);
        }

        @Override
        public void __onError(String what, int code)
        {
            onError(what, code);

            if (useDefaultErrorHandler)
            {
                RmiErrorDefaultHandler.onError(what, code);
            }
        }

        @Override
        public void __onTimeout()
        {
            onTimeout();
        }

        public abstract void onResponse(tailermsg.SeqMyTailerOrder orderList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse ITailerOper_getLatestTailerOrderList_response
    public static abstract class ITailerOper_getLatestTailerOrderList_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public ITailerOper_getLatestTailerOrderList_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            tailermsg.SeqTailerOrder orderList = new tailermsg.SeqTailerOrder();
            orderList.__read(__is);

            onResponse(orderList);
        }

        @Override
        public void __onError(String what, int code)
        {
            onError(what, code);

            if (useDefaultErrorHandler)
            {
                RmiErrorDefaultHandler.onError(what, code);
            }
        }

        @Override
        public void __onTimeout()
        {
            onTimeout();
        }

        public abstract void onResponse(tailermsg.SeqTailerOrder orderList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse ITailerOper_getOlderTailerOrderList_response
    public static abstract class ITailerOper_getOlderTailerOrderList_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public ITailerOper_getOlderTailerOrderList_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            tailermsg.SeqTailerOrder orderList = new tailermsg.SeqTailerOrder();
            orderList.__read(__is);

            onResponse(orderList);
        }

        @Override
        public void __onError(String what, int code)
        {
            onError(what, code);

            if (useDefaultErrorHandler)
            {
                RmiErrorDefaultHandler.onError(what, code);
            }
        }

        @Override
        public void __onTimeout()
        {
            onTimeout();
        }

        public abstract void onResponse(tailermsg.SeqTailerOrder orderList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Proxy ITailerOperProxy
    public static class ITailerOperProxy extends RmiCore.RmiProxyBase
    {
        public static void __regist(){
            // regist proxy at startup...
            ProxyManager.instance().addProxy(new ITailerOperProxy());
        }

        public ITailerOperProxy()
        {
            super("ITailerOper");
        }

        public void newTailerOrder(ITailerOper_newTailerOrder_response __response, String sessionKey, SNewOrderParams orderParams)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("newTailerOrder"));

            if (__response != null)
            {
                int __msgId = MessageBlock.getMsgId();
                __response.setMsgId(__msgId);
                __os.write(__msgId);
            }
            else
            {
                __os.write(0);
            }

            __os.write(sessionKey);
            orderParams.__write(__os);

            this.call(__os, __response);
        }

        public void getMyTailerOrdrList(ITailerOper_getMyTailerOrdrList_response __response, String sessionKey, int pageIndex)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getMyTailerOrdrList"));

            if (__response != null)
            {
                int __msgId = MessageBlock.getMsgId();
                __response.setMsgId(__msgId);
                __os.write(__msgId);
            }
            else
            {
                __os.write(0);
            }

            __os.write(sessionKey);
            __os.write(pageIndex);

            this.call(__os, __response);
        }

        public void getLatestTailerOrderList(ITailerOper_getLatestTailerOrderList_response __response, String sessionKey, Date latestOrderDt, int targetNum)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getLatestTailerOrderList"));

            if (__response != null)
            {
                int __msgId = MessageBlock.getMsgId();
                __response.setMsgId(__msgId);
                __os.write(__msgId);
            }
            else
            {
                __os.write(0);
            }

            __os.write(sessionKey);
            __os.write(latestOrderDt);
            __os.write(targetNum);

            this.call(__os, __response);
        }

        public void getOlderTailerOrderList(ITailerOper_getOlderTailerOrderList_response __response, String sessionKey, Date oldestOrderDt, int targetNum)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getOlderTailerOrderList"));

            if (__response != null)
            {
                int __msgId = MessageBlock.getMsgId();
                __response.setMsgId(__msgId);
                __os.write(__msgId);
            }
            else
            {
                __os.write(0);
            }

            __os.write(sessionKey);
            __os.write(oldestOrderDt);
            __os.write(targetNum);

            this.call(__os, __response);
        }

    }

}

