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
-- Table structure for table `t_message_config`
--

DROP TABLE IF EXISTS `t_message_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_message_config` (
  `msg_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'msg_id for grouping',
  `msg_key` varchar(64) NOT NULL COMMENT '唯一键',
  `msg_content` varchar(1024) DEFAULT NULL COMMENT '内容',
  `short_desc` varchar(256) DEFAULT NULL COMMENT '描述',
  PRIMARY KEY (`msg_id`),
  UNIQUE KEY `msg_key_UNIQUE` (`msg_key`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='消息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_message_config`
--

LOCK TABLES `t_message_config` WRITE;
/*!40000 ALTER TABLE `t_message_config` DISABLE KEYS */;
INSERT INTO `t_message_config` VALUES (1,'regist_validation','{0}（家庭e柜手机动态码，{1}分钟内有效，请完成验证），如非本人操作，请忽略此短信。（归一科技）','手机方式注册账号验证码短信内容。{0}验证码，{1}为有效时间'),(2,'reset_pswd_validation','{0}(修改账号密码验证，{}分钟内有效)','修改密码手机短信验证码'),(3,'test_validation','尊敬的用户，您的手机动态验证码为{}.\r为保证个人账户安全请勿泄露他人','测试用验证码');
/*!40000 ALTER TABLE `t_message_config` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-28 12:02:11
