/*
* @filename tailermsg.java
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
import message.common.publicdef;
import message.common.publicmsg;
import message.gate.gateconst;
import message.gate.gatemsg;


public class tailermsg
{
    // class STailerOrder
    public static class STailerOrder extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new STailerOrder();
            }
        }

        public static void __regist(){
            MessageBlock.regist("STailerOrder", new AutoRegist());
        }

        public String orderId;
        public gatemsg.SUserBrief userInfo;
        public Date publishedDt;
        public int orderType;
        public publicdef.SeqString tags;
        public String title;
        public String content;
        public gatemsg.SImageInfo imagesInfo;
        public int viewTimes;
        public int bidderNum;
        public boolean isBidded;

        public STailerOrder()
        {
            orderId = "";
            userInfo = new gatemsg.SUserBrief();
            publishedDt = new Date();
            orderType = gateconst.ETailerOrderType.NoneType;
            tags = new publicdef.SeqString();
            title = "";
            content = "";
            imagesInfo = new gatemsg.SImageInfo();
            viewTimes = 0;
            bidderNum = 0;
            isBidded = false;
        }

        @Override
        public void __read(Serializer __is)
        {
            orderId = __is.read(orderId);
            userInfo.__read(__is);
            publishedDt = __is.read(publishedDt);
            orderType = __is.readInt();
            tags.__read(__is);
            title = __is.read(title);
            content = __is.read(content);
            imagesInfo.__read(__is);
            viewTimes = __is.read(viewTimes);
            bidderNum = __is.read(bidderNum);
            isBidded = __is.read(isBidded);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(orderId);
            userInfo.__write(__os);
            __os.write(publishedDt);
            __os.write(orderType);
            tags.__write(__os);
            __os.write(title);
            __os.write(content);
            imagesInfo.__write(__os);
            __os.write(viewTimes);
            __os.write(bidderNum);
            __os.write(isBidded);
        }
    } // end of class STailerOrder

    // List SeqTailerOrder
    public static class SeqTailerOrder
    {
        private STailerOrder[] __array;

        public SeqTailerOrder()
        {
            __array = new STailerOrder[0];
        }

        public SeqTailerOrder(STailerOrder[] initArray)
        {
            __array = initArray;
        }

        public SeqTailerOrder(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new STailerOrder[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new STailerOrder();
            }
        }

        public STailerOrder[] getArray()
        {
            return __array;
        }

        public int getSize()
        {
            return (__array != null) ? __array.length : 0;
        }

        public boolean isEmpty()
        {
            return (getSize() == 0);
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            __array = new STailerOrder[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                STailerOrder __val = new STailerOrder();
                __val.__read(__is);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __array[i].__write(__os);
            }
        }

    } //..

    // class SMyTailerOrder
    public static class SMyTailerOrder extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SMyTailerOrder();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SMyTailerOrder", new AutoRegist());
        }

        public String orderId;
        public Date publishedDt;
        public int orderType;
        public publicdef.SeqString tags;
        public String title;
        public String content;
        public gatemsg.SImageInfo imagesInfo;
        public int orderStage;
        public int viewTimes;
        public int bidderNum;
        public boolean isBidded;

        public SMyTailerOrder()
        {
            orderId = "";
            publishedDt = new Date();
            orderType = gateconst.ETailerOrderType.NoneType;
            tags = new publicdef.SeqString();
            title = "";
            content = "";
            imagesInfo = new gatemsg.SImageInfo();
            orderStage = gateconst.ETailerOrderStage.NotBidded;
            viewTimes = 0;
            bidderNum = 0;
            isBidded = false;
        }

        @Override
        public void __read(Serializer __is)
        {
            orderId = __is.read(orderId);
            publishedDt = __is.read(publishedDt);
            orderType = __is.readInt();
            tags.__read(__is);
            title = __is.read(title);
            content = __is.read(content);
            imagesInfo.__read(__is);
            orderStage = __is.readInt();
            viewTimes = __is.read(viewTimes);
            bidderNum = __is.read(bidderNum);
            isBidded = __is.read(isBidded);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(orderId);
            __os.write(publishedDt);
            __os.write(orderType);
            tags.__write(__os);
            __os.write(title);
            __os.write(content);
            imagesInfo.__write(__os);
            __os.write(orderStage);
            __os.write(viewTimes);
            __os.write(bidderNum);
            __os.write(isBidded);
        }
    } // end of class SMyTailerOrder

    // List SeqMyTailerOrder
    public static class SeqMyTailerOrder
    {
        private SMyTailerOrder[] __array;

        public SeqMyTailerOrder()
        {
            __array = new SMyTailerOrder[0];
        }

        public SeqMyTailerOrder(SMyTailerOrder[] initArray)
        {
            __array = initArray;
        }

        public SeqMyTailerOrder(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SMyTailerOrder[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SMyTailerOrder();
            }
        }

        public SMyTailerOrder[] getArray()
        {
            return __array;
        }

        public int getSize()
        {
            return (__array != null) ? __array.length : 0;
        }

        public boolean isEmpty()
        {
            return (getSize() == 0);
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            __array = new SMyTailerOrder[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SMyTailerOrder __val = new SMyTailerOrder();
                __val.__read(__is);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __array[i].__write(__os);
            }
        }

    } //..

}

