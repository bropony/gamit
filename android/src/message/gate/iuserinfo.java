/*
* @filename iuserinfo.java
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


public class iuserinfo
{
    // Reponse IUserInfo_getMyDetails_response
    public static abstract class IUserInfo_getMyDetails_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_getMyDetails_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SMyDetailInfo myDetails = new gatemsg.SMyDetailInfo();
            myDetails.__read(__is);

            onResponse(myDetails);
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

        public abstract void onResponse(gatemsg.SMyDetailInfo myDetails);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IUserInfo_getFamilyMembers_response
    public static abstract class IUserInfo_getFamilyMembers_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_getFamilyMembers_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqFamilyMember familyMembers = new gatemsg.SeqFamilyMember();
            familyMembers.__read(__is);

            onResponse(familyMembers);
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

        public abstract void onResponse(gatemsg.SeqFamilyMember familyMembers);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IUserInfo_changeNickname_response
    public static abstract class IUserInfo_changeNickname_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_changeNickname_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            onResponse();
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

        public abstract void onResponse();
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IUserInfo_changeAvatar_response
    public static abstract class IUserInfo_changeAvatar_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_changeAvatar_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            onResponse();
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

        public abstract void onResponse();
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IUserInfo_updateGender_response
    public static abstract class IUserInfo_updateGender_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_updateGender_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            onResponse();
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

        public abstract void onResponse();
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IUserInfo_updateBirthDay_response
    public static abstract class IUserInfo_updateBirthDay_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_updateBirthDay_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            onResponse();
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

        public abstract void onResponse();
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IUserInfo_updateFamilyMembers_response
    public static abstract class IUserInfo_updateFamilyMembers_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_updateFamilyMembers_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            onResponse();
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

        public abstract void onResponse();
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IUserInfo_removeFamilyMember_response
    public static abstract class IUserInfo_removeFamilyMember_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_removeFamilyMember_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            onResponse();
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

        public abstract void onResponse();
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IUserInfo_updateAdress_response
    public static abstract class IUserInfo_updateAdress_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_updateAdress_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            int newAddressIndex = 0;
            newAddressIndex = __is.read(newAddressIndex);

            onResponse(newAddressIndex);
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

        public abstract void onResponse(int newAddressIndex);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IUserInfo_getAddressList_response
    public static abstract class IUserInfo_getAddressList_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_getAddressList_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            publicmsg.SeqAddress addressList = new publicmsg.SeqAddress();
            addressList.__read(__is);

            onResponse(addressList);
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

        public abstract void onResponse(publicmsg.SeqAddress addressList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IUserInfo_setDefaultAddress_response
    public static abstract class IUserInfo_setDefaultAddress_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_setDefaultAddress_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            onResponse();
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

        public abstract void onResponse();
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IUserInfo_deleteAddress_response
    public static abstract class IUserInfo_deleteAddress_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IUserInfo_deleteAddress_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            onResponse();
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

        public abstract void onResponse();
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Proxy IUserInfoProxy
    public static class IUserInfoProxy extends RmiCore.RmiProxyBase
    {
        public static void __regist(){
            // regist proxy at startup...
            ProxyManager.instance().addProxy(new IUserInfoProxy());
        }

        public IUserInfoProxy()
        {
            super("IUserInfo");
        }

        public void getMyDetails(IUserInfo_getMyDetails_response __response, String sessionKey)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getMyDetails"));

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

            this.call(__os, __response);
        }

        public void getFamilyMembers(IUserInfo_getFamilyMembers_response __response, String sessionKey)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getFamilyMembers"));

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

            this.call(__os, __response);
        }

        public void changeNickname(IUserInfo_changeNickname_response __response, String sessionKey, String newNickname)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("changeNickname"));

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
            __os.write(newNickname);

            this.call(__os, __response);
        }

        public void changeAvatar(IUserInfo_changeAvatar_response __response, String sessionKey, String newAvatar)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("changeAvatar"));

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
            __os.write(newAvatar);

            this.call(__os, __response);
        }

        public void updateGender(IUserInfo_updateGender_response __response, String sessionKey, int gender)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("updateGender"));

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
            __os.write(gender);

            this.call(__os, __response);
        }

        public void updateBirthDay(IUserInfo_updateBirthDay_response __response, String sessionKey, Date birthday)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("updateBirthDay"));

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
            __os.write(birthday);

            this.call(__os, __response);
        }

        public void updateFamilyMembers(IUserInfo_updateFamilyMembers_response __response, String sessionKey, gatemsg.SeqFamilyMember familyMembers)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("updateFamilyMembers"));

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
            familyMembers.__write(__os);

            this.call(__os, __response);
        }

        public void removeFamilyMember(IUserInfo_removeFamilyMember_response __response, String sessionKey, publicdef.SeqInt indexes)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("removeFamilyMember"));

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
            indexes.__write(__os);

            this.call(__os, __response);
        }

        public void updateAdress(IUserInfo_updateAdress_response __response, String sessionKey, publicmsg.SAddress addressInfo)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("updateAdress"));

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
            addressInfo.__write(__os);

            this.call(__os, __response);
        }

        public void getAddressList(IUserInfo_getAddressList_response __response, String sessionKey)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getAddressList"));

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

            this.call(__os, __response);
        }

        public void setDefaultAddress(IUserInfo_setDefaultAddress_response __response, String sessionKey, int addressIndex)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("setDefaultAddress"));

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
            __os.write(addressIndex);

            this.call(__os, __response);
        }

        public void deleteAddress(IUserInfo_deleteAddress_response __response, String sessionKey, int addressIndex)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("deleteAddress"));

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
            __os.write(addressIndex);

            this.call(__os, __response);
        }

    }

}

