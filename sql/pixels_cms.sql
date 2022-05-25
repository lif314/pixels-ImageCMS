/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.7.38-log : Database - pixels_cms
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pixels_cms` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `pixels_cms`;

/*Table structure for table `collect` */

DROP TABLE IF EXISTS `collect`;

CREATE TABLE `collect` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) DEFAULT NULL COMMENT '用户id',
  `image_id` bigint(20) DEFAULT NULL COMMENT '图片id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `collect` */

insert  into `collect`(`id`,`user_id`,`image_id`) values (1,5,24),(2,5,26),(3,5,19),(4,5,38);

/*Table structure for table `picture` */

DROP TABLE IF EXISTS `picture`;

CREATE TABLE `picture` (
  `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '图片id',
  `url` varchar(255) DEFAULT NULL COMMENT '图片url',
  `owner_id` bigint(20) DEFAULT NULL COMMENT '上传者的id',
  `owner_name` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '上传者的名字',
  `note` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '图片描述信息',
  `tags` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '图片标签(多个以,分隔)',
  `score` double DEFAULT NULL COMMENT '相似度评分',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

/*Data for the table `picture` */

insert  into `picture`(`id`,`url`,`owner_id`,`owner_name`,`note`,`tags`,`score`) values (19,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2Ffba3da13.png',5,'Adam Boost','pic','giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca',92.05194115638733),(21,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2F11ca8ae9.png',5,'Adam Boost','pic','hip, rose hip, rosehip',6.170918047428131),(22,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2Fe9804b39.png',5,'Adam Boost','pic','whippet',28.211241960525513),(23,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2F64113042.png',5,'Adam Boost','pic','American Staffordshire terrier, Staffordshire terrier, American pit bull terrier, pit bull terrier',65.69880247116089),(24,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2Fcca2c029.png',5,'Adam Boost','pic','golden retriever',72.05637097358704),(25,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2Fe43aa0ea.png',5,'Adam Boost','pic','pug, pug-dog',61.79274916648865),(26,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2F495f8b37.png',5,'Adam Boost','pic','pot, flowerpot',18.821825087070465),(27,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2F94daca1b.png',5,'Adam Boost','pic','lipstick, lip rouge',20.362435281276703),(28,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2F0babb65a.png',5,'Adam Boost','pic','daisy',58.66566300392151),(29,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2F505da662.png',5,'Adam Boost','pic','vulture',58.82912874221802),(30,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2Fda32cec4.png',5,'Adam Boost','pic','upright, upright piano',15.606583654880524),(31,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2F0658106e.png',5,'Adam Boost','pic','comic book',63.544028997421265),(32,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2Ff4d7f3aa.png',5,'Adam Boost','pic','fly',96.67391180992126),(33,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2Fa505bd39.png',5,'Adam Boost','pic','basset, basset hound',95.03628015518188),(34,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2Ff5040de1.png',5,'Adam Boost','pic','vase',35.97417771816254),(35,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2Fb95a7940.png',5,'Adam Boost','pic','pajama, pyjama, pj\'s, jammies',25.02950429916382),(36,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-24%2F67231749.png',5,'Adam Boost','pic','Arabian camel, dromedary, Camelus dromedarius',96.40178680419922),(37,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-25%2Fd8572b8d.png',5,'Adam Boost','pic','sorrel',73.37303161621094),(38,'http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-25%2F856e4d07.png',5,'Adam Boost','pic','fox squirrel, eastern fox squirrel, Sciurus niger',51.06627941131592);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `name` varchar(255) DEFAULT NULL COMMENT '用户名',
  `password` varchar(255) DEFAULT NULL COMMENT '密码',
  `avatar` varchar(255) DEFAULT NULL COMMENT '用户肖像',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

/*Data for the table `user` */

insert  into `user`(`id`,`name`,`password`,`avatar`) values (4,'llf','llf1232','https://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-22/439735f4.png'),(5,'Adam Boost','111111','https://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-22/439735f4.png');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
