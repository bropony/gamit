/*
* @filename gateconst.java
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


public class gateconst
{
    // enum EShareType
    public static class EShareType
    {
        final public static int WeChat = 1;

    }

    // enum EHintType
    public static class EHintType
    {
        final public static int AllType = 0;
        final public static int PostCommented = 1;
        final public static int PostUpvoted = 2;
        final public static int PostReposted = 3;
        final public static int PostCommentReplied = 4;
        final public static int NewFan = 10;
        final public static int FanUnfollow = 11;
        final public static int SysMsg = 20;

    }

    // enum ETailerOrderType
    public static class ETailerOrderType
    {
        final public static int NoneType = 0;
        final public static int ImageText = 1;
        final public static int Style = 2;
        final public static int Brushing = 3;

    }

    // enum ETailerOrderStage
    public static class ETailerOrderStage
    {
        final public static int NotBidded = 0;
        final public static int Bidded = 1;
        final public static int ToBeAccepted = 2;
        final public static int Accepted = 3;

    }

}

