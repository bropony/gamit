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
-- Table structure for table `t_const_config`
--

DROP TABLE IF EXISTS `t_const_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_const_config` (
  `const_name` varchar(128) NOT NULL DEFAULT '' COMMENT '常量名',
  `int_value` int(11) NOT NULL DEFAULT '0' COMMENT '整型值',
  `str_value` varchar(256) NOT NULL DEFAULT '' COMMENT '字符串型值',
  `short_desc` varchar(256) NOT NULL DEFAULT '' COMMENT '描述，仅用于解释该常量的含义。',
  PRIMARY KEY (`const_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='常量';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_const_config`
--

LOCK TABLES `t_const_config` WRITE;
/*!40000 ALTER TABLE `t_const_config` DISABLE KEYS */;
INSERT INTO `t_const_config` VALUES ('ResetPasswordValidationCodeLifeSpan',15,'','修改手机注册用户的密码，手机验证码有效时间。单位：分钟'),('SignupPhoneValidationCodeLifeSpan',30,'','手机用户注册，手机验证码有效时间。单位：分钟');
/*!40000 ALTER TABLE `t_const_config` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-28 12:02:00
