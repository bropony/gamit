/*
* @filename publicmsg.java
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

package message.common;


import java.util.Date;
import java.util.HashMap;
import java.util.Set;
import java.util.Iterator;

import rmi.Serializer;
import rmi.MessageBlock;
import message.common.publicdef;


public class publicmsg
{
    // class SAddress
    public static class SAddress extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SAddress();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SAddress", new AutoRegist());
        }

        public int addressIndex;
        public String countryCode;
        public String country;
        public String province;
        public String city;
        public String district;
        public String details;
        public String recipientName;
        public String recipientPhoneNum;
        public String postCode;
        public boolean isDefault;
        public double altitude;
        public double longitude;

        public SAddress()
        {
            addressIndex = 0;
            countryCode = "";
            country = "";
            province = "";
            city = "";
            district = "";
            details = "";
            recipientName = "";
            recipientPhoneNum = "";
            postCode = "";
            isDefault = false;
            altitude = 0;
            longitude = 0;
        }

        @Override
        public void __read(Serializer __is)
        {
            addressIndex = __is.read(addressIndex);
            countryCode = __is.read(countryCode);
            country = __is.read(country);
            province = __is.read(province);
            city = __is.read(city);
            district = __is.read(district);
            details = __is.read(details);
            recipientName = __is.read(recipientName);
            recipientPhoneNum = __is.read(recipientPhoneNum);
            postCode = __is.read(postCode);
            isDefault = __is.read(isDefault);
            altitude = __is.read(altitude);
            longitude = __is.read(longitude);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(addressIndex);
            __os.write(countryCode);
            __os.write(country);
            __os.write(province);
            __os.write(city);
            __os.write(district);
            __os.write(details);
            __os.write(recipientName);
            __os.write(recipientPhoneNum);
            __os.write(postCode);
            __os.write(isDefault);
            __os.write(altitude);
            __os.write(longitude);
        }
    } // end of class SAddress

    // List SeqAddress
    public static class SeqAddress
    {
        private SAddress[] __array;

        public SeqAddress()
        {
            __array = new SAddress[0];
        }

        public SeqAddress(SAddress[] initArray)
        {
            __array = initArray;
        }

        public SeqAddress(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SAddress[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SAddress();
            }
        }

        public SAddress[] getArray()
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
            __array = new SAddress[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SAddress __val = new SAddress();
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

