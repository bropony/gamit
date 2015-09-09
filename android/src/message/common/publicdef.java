/*
* @filename publicdef.java
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


public class publicdef
{
    // List SeqInt
    public static class SeqInt
    {
        private int[] __array;

        public SeqInt()
        {
            __array = new int[0];
        }

        public SeqInt(int[] initArray)
        {
            __array = initArray;
        }

        public SeqInt(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new int[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = 0;
            }
        }

        public int[] getArray()
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
            __array = new int[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                int __val = 0;
                __val = __is.read(__val);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __os.write(__array[i]);
            }
        }

    } //..

    // List SeqLong
    public static class SeqLong
    {
        private long[] __array;

        public SeqLong()
        {
            __array = new long[0];
        }

        public SeqLong(long[] initArray)
        {
            __array = initArray;
        }

        public SeqLong(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new long[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = 0;
            }
        }

        public long[] getArray()
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
            __array = new long[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                long __val = 0;
                __val = __is.read(__val);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __os.write(__array[i]);
            }
        }

    } //..

    // List SeqByte
    public static class SeqByte
    {
        private byte[] __array;

        public SeqByte()
        {
            __array = new byte[0];
        }

        public SeqByte(byte[] initArray)
        {
            __array = initArray;
        }

        public SeqByte(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new byte[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = 0;
            }
        }

        public byte[] getArray()
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
            __array = new byte[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                byte __val = 0;
                __val = __is.read(__val);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __os.write(__array[i]);
            }
        }

    } //..

    // List SeqString
    public static class SeqString
    {
        private String[] __array;

        public SeqString()
        {
            __array = new String[0];
        }

        public SeqString(String[] initArray)
        {
            __array = initArray;
        }

        public SeqString(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new String[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = "";
            }
        }

        public String[] getArray()
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
            __array = new String[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                String __val = "";
                __val = __is.read(__val);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __os.write(__array[i]);
            }
        }

    } //..

    // List SeqDate
    public static class SeqDate
    {
        private Date[] __array;

        public SeqDate()
        {
            __array = new Date[0];
        }

        public SeqDate(Date[] initArray)
        {
            __array = initArray;
        }

        public SeqDate(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new Date[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new Date();
            }
        }

        public Date[] getArray()
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
            __array = new Date[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                Date __val = new Date();
                __val = __is.read(__val);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __os.write(__array[i]);
            }
        }

    } //..

    // Dict DictIntBool
    public static class DictIntBool
    {
        private HashMap<Integer, Boolean> __map;

        public DictIntBool()
        {
            __map = new HashMap<Integer, Boolean>();
        }

        public DictIntBool(HashMap<Integer, Boolean> initMap)
        {
            __map = initMap;
        }

        public HashMap<Integer, Boolean> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                Integer __key = new Integer(__is.readInt());
                Boolean __val = new Boolean(__is.readBool());
                __map.put(__key, __val);
            }
        }

        public void __write(Serializer __os)
        {
            __os.write(__map.size());

            Set<Integer> __keySet = __map.keySet();
            Iterator<Integer> __it = __keySet.iterator();
            while (__it.hasNext())
            {
                Integer __key = __it.next();
                __os.write(__key.intValue());
                Boolean __val = __map.get(__key);
                __os.write(__val.booleanValue());
            }
        }

    }

    // Dict DictIntInt
    public static class DictIntInt
    {
        private HashMap<Integer, Integer> __map;

        public DictIntInt()
        {
            __map = new HashMap<Integer, Integer>();
        }

        public DictIntInt(HashMap<Integer, Integer> initMap)
        {
            __map = initMap;
        }

        public HashMap<Integer, Integer> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                Integer __key = new Integer(__is.readInt());
                Integer __val = new Integer(__is.readInt());
                __map.put(__key, __val);
            }
        }

        public void __write(Serializer __os)
        {
            __os.write(__map.size());

            Set<Integer> __keySet = __map.keySet();
            Iterator<Integer> __it = __keySet.iterator();
            while (__it.hasNext())
            {
                Integer __key = __it.next();
                __os.write(__key.intValue());
                Integer __val = __map.get(__key);
                __os.write(__val.intValue());
            }
        }

    }

    // Dict DictStringString
    public static class DictStringString
    {
        private HashMap<String, String> __map;

        public DictStringString()
        {
            __map = new HashMap<String, String>();
        }

        public DictStringString(HashMap<String, String> initMap)
        {
            __map = initMap;
        }

        public HashMap<String, String> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                String __key = __is.readString();
                String __val = "";
                __val = __is.read(__val);
                __map.put(__key, __val);
            }
        }

        public void __write(Serializer __os)
        {
            __os.write(__map.size());

            Set<String> __keySet = __map.keySet();
            Iterator<String> __it = __keySet.iterator();
            while (__it.hasNext())
            {
                String __key = __it.next();
                __os.write(__key);
                String __val = __map.get(__key);
                __os.write(__val);
            }
        }

    }

    // Dict DictStringInt
    public static class DictStringInt
    {
        private HashMap<String, Integer> __map;

        public DictStringInt()
        {
            __map = new HashMap<String, Integer>();
        }

        public DictStringInt(HashMap<String, Integer> initMap)
        {
            __map = initMap;
        }

        public HashMap<String, Integer> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                String __key = __is.readString();
                Integer __val = new Integer(__is.readInt());
                __map.put(__key, __val);
            }
        }

        public void __write(Serializer __os)
        {
            __os.write(__map.size());

            Set<String> __keySet = __map.keySet();
            Iterator<String> __it = __keySet.iterator();
            while (__it.hasNext())
            {
                String __key = __it.next();
                __os.write(__key);
                Integer __val = __map.get(__key);
                __os.write(__val.intValue());
            }
        }

    }

    // Dict DictIntString
    public static class DictIntString
    {
        private HashMap<Integer, String> __map;

        public DictIntString()
        {
            __map = new HashMap<Integer, String>();
        }

        public DictIntString(HashMap<Integer, String> initMap)
        {
            __map = initMap;
        }

        public HashMap<Integer, String> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                Integer __key = new Integer(__is.readInt());
                String __val = "";
                __val = __is.read(__val);
                __map.put(__key, __val);
            }
        }

        public void __write(Serializer __os)
        {
            __os.write(__map.size());

            Set<Integer> __keySet = __map.keySet();
            Iterator<Integer> __it = __keySet.iterator();
            while (__it.hasNext())
            {
                Integer __key = __it.next();
                __os.write(__key.intValue());
                String __val = __map.get(__key);
                __os.write(__val);
            }
        }

    }

    // Dict DictStringBool
    public static class DictStringBool
    {
        private HashMap<String, Boolean> __map;

        public DictStringBool()
        {
            __map = new HashMap<String, Boolean>();
        }

        public DictStringBool(HashMap<String, Boolean> initMap)
        {
            __map = initMap;
        }

        public HashMap<String, Boolean> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                String __key = __is.readString();
                Boolean __val = new Boolean(__is.readBool());
                __map.put(__key, __val);
            }
        }

        public void __write(Serializer __os)
        {
            __os.write(__map.size());

            Set<String> __keySet = __map.keySet();
            Iterator<String> __it = __keySet.iterator();
            while (__it.hasNext())
            {
                String __key = __it.next();
                __os.write(__key);
                Boolean __val = __map.get(__key);
                __os.write(__val.booleanValue());
            }
        }

    }

    // enum ESysTopicType
    public static class ESysTopicType
    {
        final public static int PlatformTopic = 1;
        final public static int BusinessTopic = 2;
        final public static int Advertisement = 3;

    }

    // enum ELoginType
    public static class ELoginType
    {
        final public static int MobilePhoneNum = 1;
        final public static int TencentQQ = 2;
        final public static int WeChat = 3;

    }

    // enum EGender
    public static class EGender
    {
        final public static int Unknown = 0;
        final public static int Male = 1;
        final public static int Female = 2;

    }

    // enum EInteractiveType
    public static class EInteractiveType
    {
        final public static int Upvote = 1;
        final public static int Comment = 2;
        final public static int Shared = 3;

    }

}

