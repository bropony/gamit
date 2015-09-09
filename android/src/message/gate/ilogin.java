/*
* @filename ilogin.java
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


public class ilogin
{
    // Reponse ILogin_getPhoneSignupValidationCode_response
    public static abstract class ILogin_getPhoneSignupValidationCode_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public ILogin_getPhoneSignupValidationCode_response()
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

    // Reponse ILogin_login_response
    public static abstract class ILogin_login_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public ILogin_login_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SLoginReturn loginRes = new gatemsg.SLoginReturn();
            loginRes.__read(__is);

            onResponse(loginRes);
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

        public abstract void onResponse(gatemsg.SLoginReturn loginRes);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse ILogin_signup_response
    public static abstract class ILogin_signup_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public ILogin_signup_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SLoginReturn signupRes = new gatemsg.SLoginReturn();
            signupRes.__read(__is);

            onResponse(signupRes);
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

        public abstract void onResponse(gatemsg.SLoginReturn signupRes);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse ILogin_getPasswordResetValidationCode_response
    public static abstract class ILogin_getPasswordResetValidationCode_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public ILogin_getPasswordResetValidationCode_response()
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

    // Reponse ILogin_resetPhoneUserPassword_response
    public static abstract class ILogin_resetPhoneUserPassword_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public ILogin_resetPhoneUserPassword_response()
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

    // Proxy ILoginProxy
    public static class ILoginProxy extends RmiCore.RmiProxyBase
    {
        public static void __regist(){
            // regist proxy at startup...
            ProxyManager.instance().addProxy(new ILoginProxy());
        }

        public ILoginProxy()
        {
            super("ILogin");
        }

        public void getPhoneSignupValidationCode(ILogin_getPhoneSignupValidationCode_response __response, String deviceCode, String phoneNum)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getPhoneSignupValidationCode"));

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

            __os.write(deviceCode);
            __os.write(phoneNum);

            this.call(__os, __response);
        }

        public void login(ILogin_login_response __response, gatemsg.SLogin loginInfo)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("login"));

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

            loginInfo.__write(__os);

            this.call(__os, __response);
        }

        public void signup(ILogin_signup_response __response, gatemsg.SSignup signupInfo)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("signup"));

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

            signupInfo.__write(__os);

            this.call(__os, __response);
        }

        public void getPasswordResetValidationCode(ILogin_getPasswordResetValidationCode_response __response, String deviceCode, String phoneNum)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getPasswordResetValidationCode"));

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

            __os.write(deviceCode);
            __os.write(phoneNum);

            this.call(__os, __response);
        }

        public void resetPhoneUserPassword(ILogin_resetPhoneUserPassword_response __response, String phoneNum, String validationCode, String newPassword)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("resetPhoneUserPassword"));

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

            __os.write(phoneNum);
            __os.write(validationCode);
            __os.write(newPassword);

            this.call(__os, __response);
        }

    }

}

