/*
* @filename ipostoper.java
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


public class ipostoper
{
    // Reponse IPostOper_getSysHints_response
    public static abstract class IPostOper_getSysHints_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getSysHints_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqMsgHint msgHintList = new gatemsg.SeqMsgHint();
            msgHintList.__read(__is);

            onResponse(msgHintList);
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

        public abstract void onResponse(gatemsg.SeqMsgHint msgHintList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getPostCommentsHints_response
    public static abstract class IPostOper_getPostCommentsHints_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getPostCommentsHints_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqUserPostCommentHint postCommentHint = new gatemsg.SeqUserPostCommentHint();
            postCommentHint.__read(__is);

            onResponse(postCommentHint);
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

        public abstract void onResponse(gatemsg.SeqUserPostCommentHint postCommentHint);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getFansByPageIndex_response
    public static abstract class IPostOper_getFansByPageIndex_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getFansByPageIndex_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqMyFan myFanList = new gatemsg.SeqMyFan();
            myFanList.__read(__is);

            onResponse(myFanList);
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

        public abstract void onResponse(gatemsg.SeqMyFan myFanList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getAllMyFocuses_response
    public static abstract class IPostOper_getAllMyFocuses_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getAllMyFocuses_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqMyFocus myFocusList = new gatemsg.SeqMyFocus();
            myFocusList.__read(__is);

            onResponse(myFocusList);
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

        public abstract void onResponse(gatemsg.SeqMyFocus myFocusList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getNewFanList_response
    public static abstract class IPostOper_getNewFanList_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getNewFanList_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqMyFan newFanList = new gatemsg.SeqMyFan();
            newFanList.__read(__is);

            onResponse(newFanList);
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

        public abstract void onResponse(gatemsg.SeqMyFan newFanList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_followAUser_response
    public static abstract class IPostOper_followAUser_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_followAUser_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SMyFocus newFocus = new gatemsg.SMyFocus();
            newFocus.__read(__is);

            onResponse(newFocus);
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

        public abstract void onResponse(gatemsg.SMyFocus newFocus);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_unfollowAUser_response
    public static abstract class IPostOper_unfollowAUser_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_unfollowAUser_response()
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

    // Reponse IPostOper_getLatestSysTopics_response
    public static abstract class IPostOper_getLatestSysTopics_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getLatestSysTopics_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqSysTopic sysTopicList = new gatemsg.SeqSysTopic();
            sysTopicList.__read(__is);

            onResponse(sysTopicList);
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

        public abstract void onResponse(gatemsg.SeqSysTopic sysTopicList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getFormerSysTopics_response
    public static abstract class IPostOper_getFormerSysTopics_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getFormerSysTopics_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqSysTopic sysTopicList = new gatemsg.SeqSysTopic();
            sysTopicList.__read(__is);

            onResponse(sysTopicList);
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

        public abstract void onResponse(gatemsg.SeqSysTopic sysTopicList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getSysTopicComments_response
    public static abstract class IPostOper_getSysTopicComments_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getSysTopicComments_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqComment commentList = new gatemsg.SeqComment();
            commentList.__read(__is);

            onResponse(commentList);
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

        public abstract void onResponse(gatemsg.SeqComment commentList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getSysTopicByTopicId_response
    public static abstract class IPostOper_getSysTopicByTopicId_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getSysTopicByTopicId_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SSysTopic sysTopic = new gatemsg.SSysTopic();
            sysTopic.__read(__is);

            onResponse(sysTopic);
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

        public abstract void onResponse(gatemsg.SSysTopic sysTopic);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_upvoteSysTopic_response
    public static abstract class IPostOper_upvoteSysTopic_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_upvoteSysTopic_response()
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

    // Reponse IPostOper_unupvoteSysTopic_response
    public static abstract class IPostOper_unupvoteSysTopic_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_unupvoteSysTopic_response()
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

    // Reponse IPostOper_shareSysTopic_response
    public static abstract class IPostOper_shareSysTopic_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_shareSysTopic_response()
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

    // Reponse IPostOper_commentSysTopic_response
    public static abstract class IPostOper_commentSysTopic_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_commentSysTopic_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            String newCommentId = "";
            newCommentId = __is.read(newCommentId);

            onResponse(newCommentId);
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

        public abstract void onResponse(String newCommentId);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_replySysTopicComment_response
    public static abstract class IPostOper_replySysTopicComment_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_replySysTopicComment_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            String newCommentId = "";
            newCommentId = __is.read(newCommentId);

            onResponse(newCommentId);
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

        public abstract void onResponse(String newCommentId);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_querySysTopicUpvoteStatus_response
    public static abstract class IPostOper_querySysTopicUpvoteStatus_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_querySysTopicUpvoteStatus_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            publicdef.DictStringBool sysTopicUpvoteStatusDict = new publicdef.DictStringBool();
            sysTopicUpvoteStatusDict.__read(__is);

            onResponse(sysTopicUpvoteStatusDict);
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

        public abstract void onResponse(publicdef.DictStringBool sysTopicUpvoteStatusDict);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_viewSysTopic_response
    public static abstract class IPostOper_viewSysTopic_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_viewSysTopic_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            int totalViewTimes = 0;
            totalViewTimes = __is.read(totalViewTimes);

            onResponse(totalViewTimes);
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

        public abstract void onResponse(int totalViewTimes);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getLatestUserPosts_response
    public static abstract class IPostOper_getLatestUserPosts_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getLatestUserPosts_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqUserPost userPostList = new gatemsg.SeqUserPost();
            userPostList.__read(__is);

            onResponse(userPostList);
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

        public abstract void onResponse(gatemsg.SeqUserPost userPostList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getFormerUserPosts_response
    public static abstract class IPostOper_getFormerUserPosts_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getFormerUserPosts_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqUserPost userPostList = new gatemsg.SeqUserPost();
            userPostList.__read(__is);

            onResponse(userPostList);
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

        public abstract void onResponse(gatemsg.SeqUserPost userPostList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getUserPostByPostId_response
    public static abstract class IPostOper_getUserPostByPostId_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getUserPostByPostId_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SUserPost userPost = new gatemsg.SUserPost();
            userPost.__read(__is);

            onResponse(userPost);
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

        public abstract void onResponse(gatemsg.SUserPost userPost);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getUserPostComments_response
    public static abstract class IPostOper_getUserPostComments_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getUserPostComments_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqComment commentList = new gatemsg.SeqComment();
            commentList.__read(__is);

            onResponse(commentList);
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

        public abstract void onResponse(gatemsg.SeqComment commentList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_commitUserPost_response
    public static abstract class IPostOper_commitUserPost_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_commitUserPost_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            String postId = "";
            postId = __is.read(postId);
            gatemsg.SeqImageInfo imageInfos = new gatemsg.SeqImageInfo();
            imageInfos.__read(__is);

            onResponse(postId, imageInfos);
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

        public abstract void onResponse(String postId, gatemsg.SeqImageInfo imageInfos);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_didImageUpload_response
    public static abstract class IPostOper_didImageUpload_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_didImageUpload_response()
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

    // Reponse IPostOper_getImageUploadTokens_response
    public static abstract class IPostOper_getImageUploadTokens_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getImageUploadTokens_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqImageInfo imageInfos = new gatemsg.SeqImageInfo();
            imageInfos.__read(__is);

            onResponse(imageInfos);
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

        public abstract void onResponse(gatemsg.SeqImageInfo imageInfos);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getImageDownloadTokens_response
    public static abstract class IPostOper_getImageDownloadTokens_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getImageDownloadTokens_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SImageInfo imgDowloadToken = new gatemsg.SImageInfo();
            imgDowloadToken.__read(__is);

            onResponse(imgDowloadToken);
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

        public abstract void onResponse(gatemsg.SImageInfo imgDowloadToken);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_upvoteUserPost_response
    public static abstract class IPostOper_upvoteUserPost_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_upvoteUserPost_response()
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

    // Reponse IPostOper_unupvoteUserPost_response
    public static abstract class IPostOper_unupvoteUserPost_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_unupvoteUserPost_response()
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

    // Reponse IPostOper_shareUserPost_response
    public static abstract class IPostOper_shareUserPost_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_shareUserPost_response()
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

    // Reponse IPostOper_commentUserPost_response
    public static abstract class IPostOper_commentUserPost_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_commentUserPost_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            String commentId = "";
            commentId = __is.read(commentId);

            onResponse(commentId);
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

        public abstract void onResponse(String commentId);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_replyUserPostComment_response
    public static abstract class IPostOper_replyUserPostComment_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_replyUserPostComment_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            String newCommentId = "";
            newCommentId = __is.read(newCommentId);

            onResponse(newCommentId);
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

        public abstract void onResponse(String newCommentId);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_queryUserPostUpvoteStatus_response
    public static abstract class IPostOper_queryUserPostUpvoteStatus_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_queryUserPostUpvoteStatus_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            publicdef.DictStringBool postUpvatedStatusDict = new publicdef.DictStringBool();
            postUpvatedStatusDict.__read(__is);

            onResponse(postUpvatedStatusDict);
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

        public abstract void onResponse(publicdef.DictStringBool postUpvatedStatusDict);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_viewUserPost_response
    public static abstract class IPostOper_viewUserPost_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_viewUserPost_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            int totalViewTimes = 0;
            totalViewTimes = __is.read(totalViewTimes);

            onResponse(totalViewTimes);
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

        public abstract void onResponse(int totalViewTimes);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_getMyUserByDateThreshold_response
    public static abstract class IPostOper_getMyUserByDateThreshold_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_getMyUserByDateThreshold_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SeqUserPost userPostList = new gatemsg.SeqUserPost();
            userPostList.__read(__is);

            onResponse(userPostList);
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

        public abstract void onResponse(gatemsg.SeqUserPost userPostList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse IPostOper_deleteUserPost_response
    public static abstract class IPostOper_deleteUserPost_response extends RmiCore.RmiResponseBase
    {
        /*
        * RmiErrorDefaultHandler.onError() will be called before onError()
        * when useDefaultErrorHandler is true;
        */
        protected boolean useDefaultErrorHandler = true;

        public IPostOper_deleteUserPost_response()
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

    // Proxy IPostOperProxy
    public static class IPostOperProxy extends RmiCore.RmiProxyBase
    {
        public static void __regist(){
            // regist proxy at startup...
            ProxyManager.instance().addProxy(new IPostOperProxy());
        }

        public IPostOperProxy()
        {
            super("IPostOper");
        }

        public void getSysHints(IPostOper_getSysHints_response __response, String sessionKey)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getSysHints"));

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

        public void getPostCommentsHints(IPostOper_getPostCommentsHints_response __response, String sessionKey)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getPostCommentsHints"));

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

        public void getFansByPageIndex(IPostOper_getFansByPageIndex_response __response, String sessionKey, int pageIndex)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getFansByPageIndex"));

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

        public void getAllMyFocuses(IPostOper_getAllMyFocuses_response __response, String sessionKey)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getAllMyFocuses"));

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

        public void getNewFanList(IPostOper_getNewFanList_response __response, String sessionKey)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getNewFanList"));

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

        public void followAUser(IPostOper_followAUser_response __response, String sessionKey, String userId)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("followAUser"));

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
            __os.write(userId);

            this.call(__os, __response);
        }

        public void unfollowAUser(IPostOper_unfollowAUser_response __response, String sessionKey, String userId)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("unfollowAUser"));

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
            __os.write(userId);

            this.call(__os, __response);
        }

        public void getLatestSysTopics(IPostOper_getLatestSysTopics_response __response, String deviceCode, String tagId, Date latestTopicDt, int targetNum, String imgFormat)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getLatestSysTopics"));

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
            __os.write(tagId);
            __os.write(latestTopicDt);
            __os.write(targetNum);
            __os.write(imgFormat);

            this.call(__os, __response);
        }

        public void getFormerSysTopics(IPostOper_getFormerSysTopics_response __response, String deviceCode, String tagId, Date oldestTopicDt, int targetNum, String imgFormat)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getFormerSysTopics"));

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
            __os.write(tagId);
            __os.write(oldestTopicDt);
            __os.write(targetNum);
            __os.write(imgFormat);

            this.call(__os, __response);
        }

        public void getSysTopicComments(IPostOper_getSysTopicComments_response __response, String deviceCode, String topicId, int interactiveType, Date latestCommentDt, int targetNum)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getSysTopicComments"));

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
            __os.write(topicId);
            __os.write(interactiveType);
            __os.write(latestCommentDt);
            __os.write(targetNum);

            this.call(__os, __response);
        }

        public void getSysTopicByTopicId(IPostOper_getSysTopicByTopicId_response __response, String deviceCode, String topicId, String imgFormat)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getSysTopicByTopicId"));

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
            __os.write(topicId);
            __os.write(imgFormat);

            this.call(__os, __response);
        }

        public void upvoteSysTopic(IPostOper_upvoteSysTopic_response __response, String sessionKey, String topicId)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("upvoteSysTopic"));

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
            __os.write(topicId);

            this.call(__os, __response);
        }

        public void unupvoteSysTopic(IPostOper_unupvoteSysTopic_response __response, String sessionKey, String topicId)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("unupvoteSysTopic"));

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
            __os.write(topicId);

            this.call(__os, __response);
        }

        public void shareSysTopic(IPostOper_shareSysTopic_response __response, String sessionKey, String topicId, int shareType)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("shareSysTopic"));

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
            __os.write(topicId);
            __os.write(shareType);

            this.call(__os, __response);
        }

        public void commentSysTopic(IPostOper_commentSysTopic_response __response, String sessionKey, String topicId, String comments)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("commentSysTopic"));

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
            __os.write(topicId);
            __os.write(comments);

            this.call(__os, __response);
        }

        public void replySysTopicComment(IPostOper_replySysTopicComment_response __response, String sessionKey, String topicId, String dstCommentId, String mentionedUserId, String comments)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("replySysTopicComment"));

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
            __os.write(topicId);
            __os.write(dstCommentId);
            __os.write(mentionedUserId);
            __os.write(comments);

            this.call(__os, __response);
        }

        public void querySysTopicUpvoteStatus(IPostOper_querySysTopicUpvoteStatus_response __response, String sessionKey, publicdef.SeqString sysTopicIdList)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("querySysTopicUpvoteStatus"));

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
            sysTopicIdList.__write(__os);

            this.call(__os, __response);
        }

        public void viewSysTopic(IPostOper_viewSysTopic_response __response, String deviceCode, String sysTopicId)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("viewSysTopic"));

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
            __os.write(sysTopicId);

            this.call(__os, __response);
        }

        public void getLatestUserPosts(IPostOper_getLatestUserPosts_response __response, String deviceCode, String tag, Date latestPostDt, int targetNum, String imgFormat)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getLatestUserPosts"));

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
            __os.write(tag);
            __os.write(latestPostDt);
            __os.write(targetNum);
            __os.write(imgFormat);

            this.call(__os, __response);
        }

        public void getFormerUserPosts(IPostOper_getFormerUserPosts_response __response, String deviceCode, String tag, Date oldestPostDt, int targetNum, String imgFormat)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getFormerUserPosts"));

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
            __os.write(tag);
            __os.write(oldestPostDt);
            __os.write(targetNum);
            __os.write(imgFormat);

            this.call(__os, __response);
        }

        public void getUserPostByPostId(IPostOper_getUserPostByPostId_response __response, String deviceCode, String postId, String imgFormat)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getUserPostByPostId"));

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
            __os.write(postId);
            __os.write(imgFormat);

            this.call(__os, __response);
        }

        public void getUserPostComments(IPostOper_getUserPostComments_response __response, String deviceCode, String postId, Date latestCommentDt, int targetNum)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getUserPostComments"));

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
            __os.write(postId);
            __os.write(latestCommentDt);
            __os.write(targetNum);

            this.call(__os, __response);
        }

        public void commitUserPost(IPostOper_commitUserPost_response __response, String sessionKey, String title, String content, publicdef.SeqString tags, int imageNum)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("commitUserPost"));

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
            __os.write(title);
            __os.write(content);
            tags.__write(__os);
            __os.write(imageNum);

            this.call(__os, __response);
        }

        public void didImageUpload(IPostOper_didImageUpload_response __response, String sessionKey, publicdef.SeqString imageKeys)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("didImageUpload"));

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
            imageKeys.__write(__os);

            this.call(__os, __response);
        }

        public void getImageUploadTokens(IPostOper_getImageUploadTokens_response __response, String sessionKey, int imgNum)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getImageUploadTokens"));

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
            __os.write(imgNum);

            this.call(__os, __response);
        }

        public void getImageDownloadTokens(IPostOper_getImageDownloadTokens_response __response, String sessionKey, String imgKey, String imgFormat)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getImageDownloadTokens"));

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
            __os.write(imgKey);
            __os.write(imgFormat);

            this.call(__os, __response);
        }

        public void upvoteUserPost(IPostOper_upvoteUserPost_response __response, String sessionKey, String postId)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("upvoteUserPost"));

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
            __os.write(postId);

            this.call(__os, __response);
        }

        public void unupvoteUserPost(IPostOper_unupvoteUserPost_response __response, String sessionKey, String postId)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("unupvoteUserPost"));

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
            __os.write(postId);

            this.call(__os, __response);
        }

        public void shareUserPost(IPostOper_shareUserPost_response __response, String sessionKey, String postId, int shareType)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("shareUserPost"));

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
            __os.write(postId);
            __os.write(shareType);

            this.call(__os, __response);
        }

        public void commentUserPost(IPostOper_commentUserPost_response __response, String sessionKey, String postId, String comments)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("commentUserPost"));

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
            __os.write(postId);
            __os.write(comments);

            this.call(__os, __response);
        }

        public void replyUserPostComment(IPostOper_replyUserPostComment_response __response, String sessionKey, String postId, String dstCommentId, String mentionedUserId, String comments)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("replyUserPostComment"));

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
            __os.write(postId);
            __os.write(dstCommentId);
            __os.write(mentionedUserId);
            __os.write(comments);

            this.call(__os, __response);
        }

        public void queryUserPostUpvoteStatus(IPostOper_queryUserPostUpvoteStatus_response __response, String sessionKey, publicdef.SeqString postIdList)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("queryUserPostUpvoteStatus"));

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
            postIdList.__write(__os);

            this.call(__os, __response);
        }

        public void viewUserPost(IPostOper_viewUserPost_response __response, String deviceCode, String postId)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("viewUserPost"));

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
            __os.write(postId);

            this.call(__os, __response);
        }

        public void getMyUserByDateThreshold(IPostOper_getMyUserByDateThreshold_response __response, String sessionKey, Date thresholdDate, String imgFormat)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getMyUserByDateThreshold"));

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
            __os.write(thresholdDate);
            __os.write(imgFormat);

            this.call(__os, __response);
        }

        public void deleteUserPost(IPostOper_deleteUserPost_response __response, String sessionKey, String postId)
        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("deleteUserPost"));

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
            __os.write(postId);

            this.call(__os, __response);
        }

    }

}

