/*
* @filename gatemsg.java
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


public class gatemsg
{
    // class SUserBrief
    public static class SUserBrief extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SUserBrief();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SUserBrief", new AutoRegist());
        }

        public String userId;
        public String nickname;
        public String avatarUrl;

        public SUserBrief()
        {
            userId = "";
            nickname = "";
            avatarUrl = "";
        }

        @Override
        public void __read(Serializer __is)
        {
            userId = __is.read(userId);
            nickname = __is.read(nickname);
            avatarUrl = __is.read(avatarUrl);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(userId);
            __os.write(nickname);
            __os.write(avatarUrl);
        }
    } // end of class SUserBrief

    // List SeqUserBrief
    public static class SeqUserBrief
    {
        private SUserBrief[] __array;

        public SeqUserBrief()
        {
            __array = new SUserBrief[0];
        }

        public SeqUserBrief(SUserBrief[] initArray)
        {
            __array = initArray;
        }

        public SeqUserBrief(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SUserBrief[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SUserBrief();
            }
        }

        public SUserBrief[] getArray()
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
            __array = new SUserBrief[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SUserBrief __val = new SUserBrief();
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

    // class SUserBriefWithoutAvatar
    public static class SUserBriefWithoutAvatar extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SUserBriefWithoutAvatar();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SUserBriefWithoutAvatar", new AutoRegist());
        }

        public String userId;
        public String nickName;

        public SUserBriefWithoutAvatar()
        {
            userId = "";
            nickName = "";
        }

        @Override
        public void __read(Serializer __is)
        {
            userId = __is.read(userId);
            nickName = __is.read(nickName);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(userId);
            __os.write(nickName);
        }
    } // end of class SUserBriefWithoutAvatar

    // List SeqUserBriefWithoutAvatar
    public static class SeqUserBriefWithoutAvatar
    {
        private SUserBriefWithoutAvatar[] __array;

        public SeqUserBriefWithoutAvatar()
        {
            __array = new SUserBriefWithoutAvatar[0];
        }

        public SeqUserBriefWithoutAvatar(SUserBriefWithoutAvatar[] initArray)
        {
            __array = initArray;
        }

        public SeqUserBriefWithoutAvatar(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SUserBriefWithoutAvatar[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SUserBriefWithoutAvatar();
            }
        }

        public SUserBriefWithoutAvatar[] getArray()
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
            __array = new SUserBriefWithoutAvatar[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SUserBriefWithoutAvatar __val = new SUserBriefWithoutAvatar();
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

    // class SMyDetailInfo
    public static class SMyDetailInfo extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SMyDetailInfo();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SMyDetailInfo", new AutoRegist());
        }

        public int vipLevel;
        public int goldBean;
        public int postNum;
        public int fanNum;
        public int focusNum;

        public SMyDetailInfo()
        {
            vipLevel = 0;
            goldBean = 0;
            postNum = 0;
            fanNum = 0;
            focusNum = 0;
        }

        @Override
        public void __read(Serializer __is)
        {
            vipLevel = __is.read(vipLevel);
            goldBean = __is.read(goldBean);
            postNum = __is.read(postNum);
            fanNum = __is.read(fanNum);
            focusNum = __is.read(focusNum);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(vipLevel);
            __os.write(goldBean);
            __os.write(postNum);
            __os.write(fanNum);
            __os.write(focusNum);
        }
    } // end of class SMyDetailInfo

    // class SLogin
    public static class SLogin extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SLogin();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SLogin", new AutoRegist());
        }

        public String deviceCode;
        public int loginType;
        public String account;
        public String password;

        public SLogin()
        {
            deviceCode = "";
            loginType = publicdef.ELoginType.MobilePhoneNum;
            account = "";
            password = "";
        }

        @Override
        public void __read(Serializer __is)
        {
            deviceCode = __is.read(deviceCode);
            loginType = __is.readInt();
            account = __is.read(account);
            password = __is.read(password);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(deviceCode);
            __os.write(loginType);
            __os.write(account);
            __os.write(password);
        }
    } // end of class SLogin

    // class SSignup
    public static class SSignup extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SSignup();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SSignup", new AutoRegist());
        }

        public String deviceCode;
        public int loginType;
        public String account;
        public String password;
        public String nickname;
        public String validationCode;
        public String invitationCode;

        public SSignup()
        {
            deviceCode = "";
            loginType = publicdef.ELoginType.MobilePhoneNum;
            account = "";
            password = "";
            nickname = "";
            validationCode = "";
            invitationCode = "";
        }

        @Override
        public void __read(Serializer __is)
        {
            deviceCode = __is.read(deviceCode);
            loginType = __is.readInt();
            account = __is.read(account);
            password = __is.read(password);
            nickname = __is.read(nickname);
            validationCode = __is.read(validationCode);
            invitationCode = __is.read(invitationCode);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(deviceCode);
            __os.write(loginType);
            __os.write(account);
            __os.write(password);
            __os.write(nickname);
            __os.write(validationCode);
            __os.write(invitationCode);
        }
    } // end of class SSignup

    // class SLoginReturn
    public static class SLoginReturn extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SLoginReturn();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SLoginReturn", new AutoRegist());
        }

        public String sessionKey;
        public String userId;
        public String nickname;
        public String avatarUrl;
        public int gender;
        public Date birthday;

        public SLoginReturn()
        {
            sessionKey = "";
            userId = "";
            nickname = "";
            avatarUrl = "";
            gender = publicdef.EGender.Unknown;
            birthday = new Date();
        }

        @Override
        public void __read(Serializer __is)
        {
            sessionKey = __is.read(sessionKey);
            userId = __is.read(userId);
            nickname = __is.read(nickname);
            avatarUrl = __is.read(avatarUrl);
            gender = __is.readInt();
            birthday = __is.read(birthday);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(sessionKey);
            __os.write(userId);
            __os.write(nickname);
            __os.write(avatarUrl);
            __os.write(gender);
            __os.write(birthday);
        }
    } // end of class SLoginReturn

    // class SFamilyMember
    public static class SFamilyMember extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SFamilyMember();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SFamilyMember", new AutoRegist());
        }

        public int index;
        public String member;
        public String name;
        public int gender;
        public Date birthday;
        public float height;
        public float weight;
        public float bust;
        public float waistline;
        public float hipline;
        public float brachium;
        public float leglength;
        public float shoulder;

        public SFamilyMember()
        {
            index = 0;
            member = "";
            name = "";
            gender = 0;
            birthday = new Date();
            height = 0;
            weight = 0;
            bust = 0;
            waistline = 0;
            hipline = 0;
            brachium = 0;
            leglength = 0;
            shoulder = 0;
        }

        @Override
        public void __read(Serializer __is)
        {
            index = __is.read(index);
            member = __is.read(member);
            name = __is.read(name);
            gender = __is.read(gender);
            birthday = __is.read(birthday);
            height = __is.read(height);
            weight = __is.read(weight);
            bust = __is.read(bust);
            waistline = __is.read(waistline);
            hipline = __is.read(hipline);
            brachium = __is.read(brachium);
            leglength = __is.read(leglength);
            shoulder = __is.read(shoulder);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(index);
            __os.write(member);
            __os.write(name);
            __os.write(gender);
            __os.write(birthday);
            __os.write(height);
            __os.write(weight);
            __os.write(bust);
            __os.write(waistline);
            __os.write(hipline);
            __os.write(brachium);
            __os.write(leglength);
            __os.write(shoulder);
        }
    } // end of class SFamilyMember

    // List SeqFamilyMember
    public static class SeqFamilyMember
    {
        private SFamilyMember[] __array;

        public SeqFamilyMember()
        {
            __array = new SFamilyMember[0];
        }

        public SeqFamilyMember(SFamilyMember[] initArray)
        {
            __array = initArray;
        }

        public SeqFamilyMember(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SFamilyMember[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SFamilyMember();
            }
        }

        public SFamilyMember[] getArray()
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
            __array = new SFamilyMember[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SFamilyMember __val = new SFamilyMember();
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

    // class SImageInfo
    public static class SImageInfo extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SImageInfo();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SImageInfo", new AutoRegist());
        }

        public String imageKey;
        public String token;
        public String formatedDownloadUrl;
        public Date expireDt;

        public SImageInfo()
        {
            imageKey = "";
            token = "";
            formatedDownloadUrl = "";
            expireDt = new Date();
        }

        @Override
        public void __read(Serializer __is)
        {
            imageKey = __is.read(imageKey);
            token = __is.read(token);
            formatedDownloadUrl = __is.read(formatedDownloadUrl);
            expireDt = __is.read(expireDt);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(imageKey);
            __os.write(token);
            __os.write(formatedDownloadUrl);
            __os.write(expireDt);
        }
    } // end of class SImageInfo

    // List SeqImageInfo
    public static class SeqImageInfo
    {
        private SImageInfo[] __array;

        public SeqImageInfo()
        {
            __array = new SImageInfo[0];
        }

        public SeqImageInfo(SImageInfo[] initArray)
        {
            __array = initArray;
        }

        public SeqImageInfo(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SImageInfo[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SImageInfo();
            }
        }

        public SImageInfo[] getArray()
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
            __array = new SImageInfo[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SImageInfo __val = new SImageInfo();
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

    // class SSysTopic
    public static class SSysTopic extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SSysTopic();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SSysTopic", new AutoRegist());
        }

        public String topicId;
        public int topicType;
        public String publisherId;
        public String title;
        public String content;
        public SeqImageInfo images;
        public publicdef.SeqString tags;
        public Date createDt;
        public int sharedTimes;
        public int commentedTimes;
        public int upvotedTimes;
        public int viewTimes;

        public SSysTopic()
        {
            topicId = "";
            topicType = publicdef.ESysTopicType.PlatformTopic;
            publisherId = "";
            title = "";
            content = "";
            images = new SeqImageInfo();
            tags = new publicdef.SeqString();
            createDt = new Date();
            sharedTimes = 0;
            commentedTimes = 0;
            upvotedTimes = 0;
            viewTimes = 0;
        }

        @Override
        public void __read(Serializer __is)
        {
            topicId = __is.read(topicId);
            topicType = __is.readInt();
            publisherId = __is.read(publisherId);
            title = __is.read(title);
            content = __is.read(content);
            images.__read(__is);
            tags.__read(__is);
            createDt = __is.read(createDt);
            sharedTimes = __is.read(sharedTimes);
            commentedTimes = __is.read(commentedTimes);
            upvotedTimes = __is.read(upvotedTimes);
            viewTimes = __is.read(viewTimes);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(topicId);
            __os.write(topicType);
            __os.write(publisherId);
            __os.write(title);
            __os.write(content);
            images.__write(__os);
            tags.__write(__os);
            __os.write(createDt);
            __os.write(sharedTimes);
            __os.write(commentedTimes);
            __os.write(upvotedTimes);
            __os.write(viewTimes);
        }
    } // end of class SSysTopic

    // List SeqSysTopic
    public static class SeqSysTopic
    {
        private SSysTopic[] __array;

        public SeqSysTopic()
        {
            __array = new SSysTopic[0];
        }

        public SeqSysTopic(SSysTopic[] initArray)
        {
            __array = initArray;
        }

        public SeqSysTopic(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SSysTopic[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SSysTopic();
            }
        }

        public SSysTopic[] getArray()
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
            __array = new SSysTopic[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SSysTopic __val = new SSysTopic();
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

    // class SUserPost
    public static class SUserPost extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SUserPost();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SUserPost", new AutoRegist());
        }

        public String postId;
        public SUserBrief userInfo;
        public String title;
        public String content;
        public SeqImageInfo images;
        public publicdef.SeqString tags;
        public Date createDt;
        public int sharedTimes;
        public int commentedTimes;
        public int upvotedTimes;
        public int viewTimes;

        public SUserPost()
        {
            postId = "";
            userInfo = new SUserBrief();
            title = "";
            content = "";
            images = new SeqImageInfo();
            tags = new publicdef.SeqString();
            createDt = new Date();
            sharedTimes = 0;
            commentedTimes = 0;
            upvotedTimes = 0;
            viewTimes = 0;
        }

        @Override
        public void __read(Serializer __is)
        {
            postId = __is.read(postId);
            userInfo.__read(__is);
            title = __is.read(title);
            content = __is.read(content);
            images.__read(__is);
            tags.__read(__is);
            createDt = __is.read(createDt);
            sharedTimes = __is.read(sharedTimes);
            commentedTimes = __is.read(commentedTimes);
            upvotedTimes = __is.read(upvotedTimes);
            viewTimes = __is.read(viewTimes);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(postId);
            userInfo.__write(__os);
            __os.write(title);
            __os.write(content);
            images.__write(__os);
            tags.__write(__os);
            __os.write(createDt);
            __os.write(sharedTimes);
            __os.write(commentedTimes);
            __os.write(upvotedTimes);
            __os.write(viewTimes);
        }
    } // end of class SUserPost

    // List SeqUserPost
    public static class SeqUserPost
    {
        private SUserPost[] __array;

        public SeqUserPost()
        {
            __array = new SUserPost[0];
        }

        public SeqUserPost(SUserPost[] initArray)
        {
            __array = initArray;
        }

        public SeqUserPost(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SUserPost[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SUserPost();
            }
        }

        public SUserPost[] getArray()
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
            __array = new SUserPost[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SUserPost __val = new SUserPost();
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

    // class SComment
    public static class SComment extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SComment();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SComment", new AutoRegist());
        }

        public String commentId;
        public int interActiveType;
        public SUserBrief commenterInfo;
        public String comment;
        public Date commentDt;
        public SeqUserBriefWithoutAvatar mentioned;

        public SComment()
        {
            commentId = "";
            interActiveType = publicdef.EInteractiveType.Upvote;
            commenterInfo = new SUserBrief();
            comment = "";
            commentDt = new Date();
            mentioned = new SeqUserBriefWithoutAvatar();
        }

        @Override
        public void __read(Serializer __is)
        {
            commentId = __is.read(commentId);
            interActiveType = __is.readInt();
            commenterInfo.__read(__is);
            comment = __is.read(comment);
            commentDt = __is.read(commentDt);
            mentioned.__read(__is);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(commentId);
            __os.write(interActiveType);
            commenterInfo.__write(__os);
            __os.write(comment);
            __os.write(commentDt);
            mentioned.__write(__os);
        }
    } // end of class SComment

    // List SeqComment
    public static class SeqComment
    {
        private SComment[] __array;

        public SeqComment()
        {
            __array = new SComment[0];
        }

        public SeqComment(SComment[] initArray)
        {
            __array = initArray;
        }

        public SeqComment(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SComment[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SComment();
            }
        }

        public SComment[] getArray()
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
            __array = new SComment[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SComment __val = new SComment();
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

    // class SMsgHint
    public static class SMsgHint extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SMsgHint();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SMsgHint", new AutoRegist());
        }

        public int hintType;
        public int num;

        public SMsgHint()
        {
            hintType = gateconst.EHintType.AllType;
            num = 0;
        }

        @Override
        public void __read(Serializer __is)
        {
            hintType = __is.readInt();
            num = __is.read(num);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(hintType);
            __os.write(num);
        }
    } // end of class SMsgHint

    // List SeqMsgHint
    public static class SeqMsgHint
    {
        private SMsgHint[] __array;

        public SeqMsgHint()
        {
            __array = new SMsgHint[0];
        }

        public SeqMsgHint(SMsgHint[] initArray)
        {
            __array = initArray;
        }

        public SeqMsgHint(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SMsgHint[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SMsgHint();
            }
        }

        public SMsgHint[] getArray()
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
            __array = new SMsgHint[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SMsgHint __val = new SMsgHint();
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

    // class SUserPostCommentHint
    public static class SUserPostCommentHint extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SUserPostCommentHint();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SUserPostCommentHint", new AutoRegist());
        }

        public int hintType;
        public SUserBrief operUserInfo;
        public String content;
        public String postId;
        public String commentId;
        public Date operDt;

        public SUserPostCommentHint()
        {
            hintType = gateconst.EHintType.AllType;
            operUserInfo = new SUserBrief();
            content = "";
            postId = "";
            commentId = "";
            operDt = new Date();
        }

        @Override
        public void __read(Serializer __is)
        {
            hintType = __is.readInt();
            operUserInfo.__read(__is);
            content = __is.read(content);
            postId = __is.read(postId);
            commentId = __is.read(commentId);
            operDt = __is.read(operDt);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(hintType);
            operUserInfo.__write(__os);
            __os.write(content);
            __os.write(postId);
            __os.write(commentId);
            __os.write(operDt);
        }
    } // end of class SUserPostCommentHint

    // List SeqUserPostCommentHint
    public static class SeqUserPostCommentHint
    {
        private SUserPostCommentHint[] __array;

        public SeqUserPostCommentHint()
        {
            __array = new SUserPostCommentHint[0];
        }

        public SeqUserPostCommentHint(SUserPostCommentHint[] initArray)
        {
            __array = initArray;
        }

        public SeqUserPostCommentHint(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SUserPostCommentHint[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SUserPostCommentHint();
            }
        }

        public SUserPostCommentHint[] getArray()
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
            __array = new SUserPostCommentHint[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SUserPostCommentHint __val = new SUserPostCommentHint();
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

    // class SMyFan
    public static class SMyFan extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SMyFan();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SMyFan", new AutoRegist());
        }

        public SUserBrief fanInfo;
        public Date operDt;

        public SMyFan()
        {
            fanInfo = new SUserBrief();
            operDt = new Date();
        }

        @Override
        public void __read(Serializer __is)
        {
            fanInfo.__read(__is);
            operDt = __is.read(operDt);
        }

        @Override
        public void __write(Serializer __os)
        {
            fanInfo.__write(__os);
            __os.write(operDt);
        }
    } // end of class SMyFan

    // List SeqMyFan
    public static class SeqMyFan
    {
        private SMyFan[] __array;

        public SeqMyFan()
        {
            __array = new SMyFan[0];
        }

        public SeqMyFan(SMyFan[] initArray)
        {
            __array = initArray;
        }

        public SeqMyFan(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SMyFan[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SMyFan();
            }
        }

        public SMyFan[] getArray()
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
            __array = new SMyFan[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SMyFan __val = new SMyFan();
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

    // class SMyFocus
    public static class SMyFocus extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SMyFocus();
            }
        }

        public static void __regist(){
            MessageBlock.regist("SMyFocus", new AutoRegist());
        }

        public SUserBrief userInfo;
        public Date operDt;

        public SMyFocus()
        {
            userInfo = new SUserBrief();
            operDt = new Date();
        }

        @Override
        public void __read(Serializer __is)
        {
            userInfo.__read(__is);
            operDt = __is.read(operDt);
        }

        @Override
        public void __write(Serializer __os)
        {
            userInfo.__write(__os);
            __os.write(operDt);
        }
    } // end of class SMyFocus

    // List SeqMyFocus
    public static class SeqMyFocus
    {
        private SMyFocus[] __array;

        public SeqMyFocus()
        {
            __array = new SMyFocus[0];
        }

        public SeqMyFocus(SMyFocus[] initArray)
        {
            __array = initArray;
        }

        public SeqMyFocus(int arraySize)
        {
            arraySize = (arraySize >= 0 ? arraySize : 0);

            __array = new SMyFocus[arraySize];
            for (int i = 0; i < arraySize; i++)
            {
                __array[i] = new SMyFocus();
            }
        }

        public SMyFocus[] getArray()
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
            __array = new SMyFocus[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SMyFocus __val = new SMyFocus();
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

