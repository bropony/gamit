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
-- Table structure for table `t_topic_tag`
--

DROP TABLE IF EXISTS `t_topic_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_topic_tag` (
  `tag_id` int(11) NOT NULL DEFAULT '0' COMMENT '标签id。ID为0的标签为系统保留标签，即“推荐”标签。其它值的ID无特殊全名规则。',
  `tag_type` int(11) DEFAULT '0' COMMENT '标签类型。保留字段。默认为0。“同城”标签暂字为1。',
  `tag_name` varchar(128) NOT NULL COMMENT '标签名字',
  `is_defualt` int(11) DEFAULT '0' COMMENT '是否为默认标签。即系统帮用户自动添加的标签。',
  `short_desc` varchar(1024) NOT NULL COMMENT '对该标签的一些描述，无特殊意义，可以空',
  PRIMARY KEY (`tag_id`),
  UNIQUE KEY `tag_name_UNIQUE` (`tag_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='话题标签';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_topic_tag`
--

LOCK TABLES `t_topic_tag` WRITE;
/*!40000 ALTER TABLE `t_topic_tag` DISABLE KEYS */;
INSERT INTO `t_topic_tag` VALUES (0,0,'推荐',1,'系统保留标签，id必须为0'),(1,0,'亲子装',1,''),(2,0,'情侣装',1,''),(3,0,'睡衣',1,''),(4,1,'同城',1,''),(100,0,'明星',0,''),(101,0,'运动',0,''),(102,0,'晏会',0,''),(103,0,'校服',0,'');
/*!40000 ALTER TABLE `t_topic_tag` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-28 12:01:50
