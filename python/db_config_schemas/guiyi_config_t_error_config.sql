CREATE DATABASE  IF NOT EXISTS `guiyi_config` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `guiyi_config`;
-- MySQL dump 10.13  Distrib 5.6.24, for osx10.8 (x86_64)
--
-- Host: 192.168.0.168    Database: guiyi_config
-- ------------------------------------------------------
-- Server version	5.6.19-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_error_config`
--

DROP TABLE IF EXISTS `t_error_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_error_config` (
  `error_code` int(11) NOT NULL DEFAULT '0' COMMENT '异常代码。用于分类。数值策划人员勿个性此字段。',
  `error_name` varchar(128) NOT NULL DEFAULT '' COMMENT '异常标识。用于开发使用，策划人员请勿修改此字段。',
  `error_str` varchar(256) NOT NULL DEFAULT '' COMMENT '异常的内容。一个简明的描述。用于呈现给用户。',
  PRIMARY KEY (`error_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='异常表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_error_config`
--

LOCK TABLES `t_error_config` WRITE;
/*!40000 ALTER TABLE `t_error_config` DISABLE KEYS */;
INSERT INTO `t_error_config` VALUES (10000,'ErrorGate_fatalError','服务器异常'),(10001,'ErrorDb_DbError','数据库异常'),(10010,'ErrorDb_TableNotFound','找不到表'),(20000,'ErrorCommon_Deprecated','禁用的功能'),(20001,'ErrorLogin_InvalidValidationCode','手机验证码无效'),(20002,'ErrorLogin_InvalidLoginInfo','账号或者密码不正确'),(20003,'ErrorLogin_EmptyPassword','密码不能为空'),(20004,'ErrorLogin_loginOperTimeout','登录超时'),(20005,'ErrorLogin_signupOperTimeout','操作超时，请重试'),(20006,'ErrorLogin_AccountExists','账号已存在'),(20010,'ErrorSignup_invalidAccount','无效的账号'),(20011,'ErrorSignup_invalidPassword','无效的密码'),(20012,'ErrorSignup_invalidLoginType','无效的登录方式'),(20020,'ErrorGate_notLoggedInYet','请先登录'),(20021,'ErrorGate_invalidNickname','非法的昵称'),(20022,'ErrorGate_invalidAvatar','无效的头像'),(20023,'ErrorGate_operTimeout','操作超时'),(20024,'ErrorGate_avatarSizeTooLarge','头像图片尺寸超过限制'),(20030,'ErrorGate_noSuchPost','帖子不存在'),(20031,'ErrorGate_hasUpvotedUserPost','已经为该贴点过赞'),(20032,'ErrorGate_mentionedUserNotExist','被提及的用户不存在'),(20033,'ErrorGate_dstCommentNotExistedErrorGate_dstCommentNotExisted','被提及的评论不存在'),(20034,'ErrorGate_hasFollowedThisUser','已经关注过该用户'),(20035,'ErrorGate_noSuchUser','用户不存在'),(20036,'ErrorGate_didNotFollowThisUser','未关注该用户'),(20040,'ErrorGate_invalidGender','性别选择有误'),(20041,'ErrorGate_invalidBirthday','生日大于当前时间'),(20050,'ErrorGate_noSuchSysTopic','话题不存在'),(20060,'ErrorGate_addressRecipentNameEmpty','收件人姓名不能为空'),(20061,'ErrorGate_addressRecipentPhoneNumEmpty','收件人电话不能为空'),(20062,'ErrorGate_addressCityEmpty','请选择城市'),(20063,'ErrorGate_addressDetailsEmpty','请填写详地址信息'),(20064,'ErrorGate_addressNotExisted','无该联系地址');
/*!40000 ALTER TABLE `t_error_config` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-28 12:02:21
