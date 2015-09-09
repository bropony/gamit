package message;

import rmi.MessageBlock;
import message.common.publicmsg.SAddress;
import message.gate.gatemsg.SComment;
import message.gate.gatemsg.SFamilyMember;
import message.gate.gatemsg.SImageInfo;
import message.gate.gatemsg.SLogin;
import message.gate.gatemsg.SLoginReturn;
import message.gate.gatemsg.SMsgHint;
import message.gate.gatemsg.SMyDetailInfo;
import message.gate.gatemsg.SMyFan;
import message.gate.gatemsg.SMyFocus;
import message.gate.gatemsg.SSignup;
import message.gate.gatemsg.SSysTopic;
import message.gate.gatemsg.SUserBrief;
import message.gate.gatemsg.SUserBriefWithoutAvatar;
import message.gate.gatemsg.SUserPost;
import message.gate.gatemsg.SUserPostCommentHint;
import message.gate.ilogin.ILoginProxy;
import message.gate.ipostoper.IPostOperProxy;
import message.gate.itaileroper.ITailerOperProxy;
import message.gate.itaileroper.SNewOrderParams;
import message.gate.iuserinfo.IUserInfoProxy;
import message.gate.tailermsg.SMyTailerOrder;
import message.gate.tailermsg.STailerOrder;

public class MessageRegister{
    public static void regist(){
        message.common.publicmsg.SAddress.__regist();
        message.gate.gatemsg.SComment.__regist();
        message.gate.gatemsg.SFamilyMember.__regist();
        message.gate.gatemsg.SImageInfo.__regist();
        message.gate.gatemsg.SLogin.__regist();
        message.gate.gatemsg.SLoginReturn.__regist();
        message.gate.gatemsg.SMsgHint.__regist();
        message.gate.gatemsg.SMyDetailInfo.__regist();
        message.gate.gatemsg.SMyFan.__regist();
        message.gate.gatemsg.SMyFocus.__regist();
        message.gate.gatemsg.SSignup.__regist();
        message.gate.gatemsg.SSysTopic.__regist();
        message.gate.gatemsg.SUserBrief.__regist();
        message.gate.gatemsg.SUserBriefWithoutAvatar.__regist();
        message.gate.gatemsg.SUserPost.__regist();
        message.gate.gatemsg.SUserPostCommentHint.__regist();
        message.gate.ilogin.ILoginProxy.__regist();
        message.gate.ipostoper.IPostOperProxy.__regist();
        message.gate.itaileroper.ITailerOperProxy.__regist();
        message.gate.itaileroper.SNewOrderParams.__regist();
        message.gate.iuserinfo.IUserInfoProxy.__regist();
        message.gate.tailermsg.SMyTailerOrder.__regist();
        message.gate.tailermsg.STailerOrder.__regist();
    }
}

