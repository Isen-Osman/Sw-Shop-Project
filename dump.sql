/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-12.0.2-MariaDB, for osx10.20 (arm64)
--
-- Host: localhost    Database: swshop
-- ------------------------------------------------------
-- Server version	12.0.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Current Database: `swshop`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `swshop` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

USE `swshop`;

--
-- Table structure for table `account_emailaddress`
--

DROP TABLE IF EXISTS `account_emailaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_emailaddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_emailaddress_user_id_email_987c8728_uniq` (`user_id`,`email`),
  KEY `account_emailaddress_email_03be32b2` (`email`),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailaddress`
--

LOCK TABLES `account_emailaddress` WRITE;
/*!40000 ALTER TABLE `account_emailaddress` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `account_emailaddress` VALUES
(1,'isen.osman252@gmail.com',1,1,3),
(2,'amirosman382@gmail.com',1,1,4);
/*!40000 ALTER TABLE `account_emailaddress` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `account_emailconfirmation`
--

DROP TABLE IF EXISTS `account_emailconfirmation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_emailconfirmation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`),
  KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`),
  CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailconfirmation`
--

LOCK TABLES `account_emailconfirmation` WRITE;
/*!40000 ALTER TABLE `account_emailconfirmation` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `account_emailconfirmation` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `app_product`
--

DROP TABLE IF EXISTS `app_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_product` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `color` varchar(20) NOT NULL,
  `category` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_product`
--

LOCK TABLES `app_product` WRITE;
/*!40000 ALTER TABLE `app_product` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `app_product` VALUES
(1,'test','Test',192.00,'RED','panties','2025-08-25 15:33:53.681000'),
(9,'Denise Lace Balconette Bra','Test',999.00,'BLACK','bras','2025-08-17 14:58:42.144000'),
(10,'Sofia Natural Lift Balconette Bra in Ultralight Microfiber','Test',1499.00,'BLACK','bras','2025-08-17 15:59:02.149000'),
(11,'Lace String Thong','Test',199.00,'WHITE','panties','2025-08-17 16:08:21.166000'),
(15,'Francesca Ultimate T-shirt Balconette Bra','Meet your new go-to, the ultralight microfiber Francesca Bra. This ultimate t-shirt bra has sculpted cups providing maximum support and a smoothing effect. With lightweight padding and a double-layered tulle back, the Francesca is certain to be your new go-to bra. This item runs big in the cup.\r\n\r\n• Super light and breathable molded, padded cups\r\n• Underwire\r\n• Microfiber lined straps are adjustable in back\r\n• Optimal support\r\n• Contain and round the bust',599.00,'WHITE','bras','2025-08-24 11:36:16.499000');
/*!40000 ALTER TABLE `app_product` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `app_productimage`
--

DROP TABLE IF EXISTS `app_productimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_productimage` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_productimage_product_id_53d99c25_fk_app_product_id` (`product_id`),
  CONSTRAINT `app_productimage_product_id_53d99c25_fk_app_product_id` FOREIGN KEY (`product_id`) REFERENCES `app_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_productimage`
--

LOCK TABLES `app_productimage` WRITE;
/*!40000 ALTER TABLE `app_productimage` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `app_productimage` VALUES
(5,'products/bra.jpg',9),
(6,'products/bra3.jpg',9),
(7,'products/bran3.jpg',10),
(8,'products/bran2.jpg',10),
(9,'products/img.jpg',11),
(10,'products/img2.jpg',11),
(11,'products/img3.jpg',11),
(13,'products/bra1.jpg',15),
(14,'products/bra2.jpg',15),
(15,'products/bra3_h8LGlRY.jpg',15);
/*!40000 ALTER TABLE `app_productimage` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `app_productquantity`
--

DROP TABLE IF EXISTS `app_productquantity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_productquantity` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `size` varchar(5) NOT NULL,
  `quantity` int(10) unsigned NOT NULL CHECK (`quantity` >= 0),
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_productquantity_product_id_74f9844a_fk_app_product_id` (`product_id`),
  CONSTRAINT `app_productquantity_product_id_74f9844a_fk_app_product_id` FOREIGN KEY (`product_id`) REFERENCES `app_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_productquantity`
--

LOCK TABLES `app_productquantity` WRITE;
/*!40000 ALTER TABLE `app_productquantity` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `app_productquantity` VALUES
(1,'S',2,1),
(11,'XS',3,9),
(12,'S',0,9),
(13,'M',0,9),
(14,'L',0,9),
(15,'XL',0,9),
(24,'XS',0,10),
(25,'S',0,10),
(26,'M',0,10),
(27,'L',0,10),
(28,'XL',0,10),
(29,'XS',0,11),
(30,'S',0,11),
(31,'M',0,11),
(32,'L',0,11),
(33,'XL',0,11),
(37,'XXL',0,9),
(38,'XS',0,15),
(39,'S',0,15),
(40,'M',0,15),
(41,'L',0,15),
(42,'XL',0,15),
(43,'XXL',0,15),
(44,'XXL',0,11),
(45,'XXL',0,10);
/*!40000 ALTER TABLE `app_productquantity` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add site',7,'add_site'),
(26,'Can change site',7,'change_site'),
(27,'Can delete site',7,'delete_site'),
(28,'Can view site',7,'view_site'),
(29,'Can add product',8,'add_product'),
(30,'Can change product',8,'change_product'),
(31,'Can delete product',8,'delete_product'),
(32,'Can view product',8,'view_product'),
(33,'Can add product image',9,'add_productimage'),
(34,'Can change product image',9,'change_productimage'),
(35,'Can delete product image',9,'delete_productimage'),
(36,'Can view product image',9,'view_productimage'),
(37,'Can add product quantity',10,'add_productquantity'),
(38,'Can change product quantity',10,'change_productquantity'),
(39,'Can delete product quantity',10,'delete_productquantity'),
(40,'Can view product quantity',10,'view_productquantity'),
(41,'Can add wishlist',11,'add_wishlist'),
(42,'Can change wishlist',11,'change_wishlist'),
(43,'Can delete wishlist',11,'delete_wishlist'),
(44,'Can view wishlist',11,'view_wishlist'),
(45,'Can add wishlist product',12,'add_wishlistproduct'),
(46,'Can change wishlist product',12,'change_wishlistproduct'),
(47,'Can delete wishlist product',12,'delete_wishlistproduct'),
(48,'Can view wishlist product',12,'view_wishlistproduct'),
(49,'Can add order',13,'add_order'),
(50,'Can change order',13,'change_order'),
(51,'Can delete order',13,'delete_order'),
(52,'Can view order',13,'view_order'),
(53,'Can add order item',14,'add_orderitem'),
(54,'Can change order item',14,'change_orderitem'),
(55,'Can delete order item',14,'delete_orderitem'),
(56,'Can view order item',14,'view_orderitem'),
(57,'Can add email address',15,'add_emailaddress'),
(58,'Can change email address',15,'change_emailaddress'),
(59,'Can delete email address',15,'delete_emailaddress'),
(60,'Can view email address',15,'view_emailaddress'),
(61,'Can add email confirmation',16,'add_emailconfirmation'),
(62,'Can change email confirmation',16,'change_emailconfirmation'),
(63,'Can delete email confirmation',16,'delete_emailconfirmation'),
(64,'Can view email confirmation',16,'view_emailconfirmation'),
(65,'Can add social account',17,'add_socialaccount'),
(66,'Can change social account',17,'change_socialaccount'),
(67,'Can delete social account',17,'delete_socialaccount'),
(68,'Can view social account',17,'view_socialaccount'),
(69,'Can add social application',18,'add_socialapp'),
(70,'Can change social application',18,'change_socialapp'),
(71,'Can delete social application',18,'delete_socialapp'),
(72,'Can view social application',18,'view_socialapp'),
(73,'Can add social application token',19,'add_socialtoken'),
(74,'Can change social application token',19,'change_socialtoken'),
(75,'Can delete social application token',19,'delete_socialtoken'),
(76,'Can view social application token',19,'view_socialtoken');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `auth_user` VALUES
(1,'pbkdf2_sha256$600000$sQDQnmHbq2Ch4guwt25U7L$8p0WGAS2jTBHL6p4K5KI8/NHMSAvB8segpAmcAymaVc=','2025-08-25 13:34:21.334000',1,'admin','','','',1,1,'2025-08-17 11:37:34.810000'),
(2,'pbkdf2_sha256$600000$hDc8rqVMTxWbNnINtFKKO8$aAni/5PuYeONc1pIglCMMBLrWT6i9UrdBfwox1vrr2U=',NULL,1,'isendev','','','',1,1,'2025-08-17 19:13:53.766000'),
(3,'!BRbURTfn8kNrjJp1wmkVUrp8pnGCnTiaIRuZkez2','2025-08-25 13:38:45.582000',0,'isenn','Isenn','Osman','isen.osman252@gmail.com',0,1,'2025-08-20 11:22:13.354000'),
(4,'!pbtoVuLhHs4XVuGGHSVBVR1camMxiYpLGEO6LYDu','2025-08-24 12:30:16.390000',0,'amir','Amir','Osman','amirosman382@gmail.com',0,1,'2025-08-20 12:42:36.605000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_admin_log` VALUES
(1,'2025-08-17 11:38:43.090000','1','Test (female_tops)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"product quantity\", \"object\": \"Test - S: 5\"}}, {\"added\": {\"name\": \"product quantity\", \"object\": \"Test - XS: 2\"}}, {\"added\": {\"name\": \"product image\", \"object\": \"Image for Test\"}}]',7,1),
(2,'2025-08-19 15:59:22.768000','1','Facebook-login',1,'[{\"added\": {}}]',15,1),
(3,'2025-08-19 16:01:26.771000','1','http://127.0.0.1:8000/',2,'[{\"changed\": {\"fields\": [\"Domain name\", \"Display name\"]}}]',11,1),
(4,'2025-08-19 18:02:49.280000','2','Google',1,'[{\"added\": {}}]',15,1),
(5,'2025-08-19 18:03:00.796000','2','Google-login',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',15,1),
(6,'2025-08-20 10:59:52.138000','2','https://127.0.0.1:8000/',1,'[{\"added\": {}}]',11,1),
(7,'2025-08-20 11:00:00.909000','2','Google-login',2,'[{\"changed\": {\"fields\": [\"Sites\"]}}]',15,1),
(8,'2025-08-20 11:21:45.910000','2','Google-login',2,'[{\"changed\": {\"fields\": [\"Sites\"]}}]',15,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_content_type` VALUES
(15,'account','emailaddress'),
(16,'account','emailconfirmation'),
(1,'admin','logentry'),
(8,'app','product'),
(9,'app','productimage'),
(10,'app','productquantity'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(13,'orders','order'),
(14,'orders','orderitem'),
(6,'sessions','session'),
(7,'sites','site'),
(17,'socialaccount','socialaccount'),
(18,'socialaccount','socialapp'),
(19,'socialaccount','socialtoken'),
(11,'wishlist','wishlist'),
(12,'wishlist','wishlistproduct');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2025-08-25 15:20:34.010568'),
(2,'auth','0001_initial','2025-08-25 15:20:34.688703'),
(3,'account','0001_initial','2025-08-25 15:20:34.868716'),
(4,'account','0002_email_max_length','2025-08-25 15:20:34.934553'),
(5,'account','0003_alter_emailaddress_create_unique_verified_email','2025-08-25 15:20:34.998857'),
(6,'account','0004_alter_emailaddress_drop_unique_email','2025-08-25 15:20:35.086082'),
(7,'account','0005_emailaddress_idx_upper_email','2025-08-25 15:20:35.094396'),
(8,'account','0006_emailaddress_lower','2025-08-25 15:20:35.103775'),
(9,'account','0007_emailaddress_idx_email','2025-08-25 15:20:35.154490'),
(10,'account','0008_emailaddress_unique_primary_email_fixup','2025-08-25 15:20:35.163992'),
(11,'account','0009_emailaddress_unique_primary_email','2025-08-25 15:20:35.169834'),
(12,'admin','0001_initial','2025-08-25 15:20:35.293080'),
(13,'admin','0002_logentry_remove_auto_add','2025-08-25 15:20:35.299097'),
(14,'admin','0003_logentry_add_action_flag_choices','2025-08-25 15:20:35.305088'),
(15,'app','0001_initial','2025-08-25 15:20:35.461527'),
(16,'app','0002_alter_product_category_alter_productquantity_size','2025-08-25 15:20:35.467083'),
(17,'app','0003_alter_product_category','2025-08-25 15:20:35.470127'),
(18,'app','0002_alter_product_category','2025-08-25 15:20:35.473283'),
(19,'app','0004_merge_20250818_1407','2025-08-25 15:20:35.474244'),
(20,'app','0005_profile','2025-08-25 15:20:35.551685'),
(21,'app','0006_delete_profile','2025-08-25 15:20:35.575383'),
(22,'app','0004_merge_20250819_1543','2025-08-25 15:20:35.577370'),
(23,'app','0007_merge_0004_merge_20250819_1543_0006_delete_profile','2025-08-25 15:20:35.578880'),
(24,'app','0008_alter_product_color','2025-08-25 15:20:35.582024'),
(25,'contenttypes','0002_remove_content_type_name','2025-08-25 15:20:35.692071'),
(26,'auth','0002_alter_permission_name_max_length','2025-08-25 15:20:35.741098'),
(27,'auth','0003_alter_user_email_max_length','2025-08-25 15:20:35.791236'),
(28,'auth','0004_alter_user_username_opts','2025-08-25 15:20:35.796227'),
(29,'auth','0005_alter_user_last_login_null','2025-08-25 15:20:35.849034'),
(30,'auth','0006_require_contenttypes_0002','2025-08-25 15:20:35.850423'),
(31,'auth','0007_alter_validators_add_error_messages','2025-08-25 15:20:35.856232'),
(32,'auth','0008_alter_user_username_max_length','2025-08-25 15:20:35.909944'),
(33,'auth','0009_alter_user_last_name_max_length','2025-08-25 15:20:35.957802'),
(34,'auth','0010_alter_group_name_max_length','2025-08-25 15:20:36.006270'),
(35,'auth','0011_update_proxy_permissions','2025-08-25 15:20:36.013629'),
(36,'auth','0012_alter_user_first_name_max_length','2025-08-25 15:20:36.061242'),
(37,'orders','0001_initial','2025-08-25 15:20:36.264542'),
(38,'orders','0002_order_size','2025-08-25 15:20:36.327293'),
(39,'orders','0003_remove_order_size_orderitem_size','2025-08-25 15:20:36.436758'),
(40,'orders','0004_order_comment_order_phone_number_alter_order_address','2025-08-25 15:20:36.677224'),
(41,'sessions','0001_initial','2025-08-25 15:20:36.756127'),
(42,'sites','0001_initial','2025-08-25 15:20:36.775089'),
(43,'sites','0002_alter_domain_unique','2025-08-25 15:20:36.823447'),
(44,'socialaccount','0001_initial','2025-08-25 15:20:37.320429'),
(45,'socialaccount','0002_token_max_lengths','2025-08-25 15:20:37.462448'),
(46,'socialaccount','0003_extra_data_default_dict','2025-08-25 15:20:37.469973'),
(47,'socialaccount','0004_app_provider_id_settings','2025-08-25 15:20:37.712677'),
(48,'socialaccount','0005_socialtoken_nullable_app','2025-08-25 15:20:37.894536'),
(49,'socialaccount','0006_alter_socialaccount_extra_data','2025-08-25 15:20:37.959478'),
(50,'wishlist','0001_initial','2025-08-25 15:20:38.206903'),
(51,'wishlist','0002_remove_wishlist_products_wishlistitem','2025-08-25 15:20:38.361665'),
(52,'wishlist','0003_wishlist_products_delete_wishlistitem','2025-08-25 15:20:38.582182'),
(53,'wishlist','0004_wishlistproduct','2025-08-25 15:20:38.728832'),
(54,'app','0009_alter_product_category','2025-08-25 15:38:46.414371');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_session` VALUES
('135bip694vz6lxzr1yzrfxjnae5vgtym','.eJxVjEEOwiAQRe_C2hBhCgWX7j0DGWZAqgaS0q6Md7dNutDtf-_9twi4LiWsPc1hYnERSpx-t4j0THUH_MB6b5JaXeYpyl2RB-3y1ji9rof7d1Cwl632jM7QkA2D9w5GGjVlnTQSqeRQ5QGiJtok6y0zgbIKEFjz2RgTs_h8AfjQOGI:1unbi3:Dga0fSM7Y-w8uMXPbQLutkbwUr5DA6gLIoaclv5K6TE','2025-08-31 11:37:59.180000'),
('1e0s7tka7uvk6s6xabxo8kb2kuabo2dy','.eJxVjMsOwiAUBf-FtSFFKA-X7vsN5D5AqgaS0q6M_65NutDtmZnzEhG2tcStpyXOLC5CidPvhkCPVHfAd6i3JqnVdZlR7oo8aJdT4_S8Hu7fQYFevnVmst44xxZAg1YwhoSAI-kzQ_bBG52VQZ-t8oNBtCEADom0ymSsI_H-AAItOJU:1unipN:Y6o7K-JFc7IWFv6hwCfkJc86u9V87PzQ9uiFyTwueGc','2025-08-31 19:14:01.997000'),
('6egfykckmoasirmqo7boiywhfz7byzzj','.eJxVULluhDAQ_RfXCPnAxt4u6VNtEymK0DB4FysER9gkUhD_noGwBd3Tu-ZYWIoYYADEOI-5SRmyT-yyrAV7cDDn3o85IOQQx-bT5z525Hlb2D9ml3MLo2xmF1Fr7YxQhpdCciFswb6m-B06P1HiHuN98GSdw1YghK61tEY6LqWRxirNK7a-F2yf38zJT83uVOzEtYAfftwEGIaNLo8tyt1zyKl8Ol3xfKROVT2knnoqpSQqg067FmwtbzdhW9TGIria6wqthNqKDoVE6ITmANi1naHlPUe9lf6E1A8h0T_D7_5Ouo-aryQJTuCFgHsQisDrla3rH0adfn8:1upqec:_70adidC8AAH8PKwKhb5LpCxLgzO9VmtT9CGHHgBlAk','2025-09-06 15:59:42.357000'),
('kwalbj3l6n2afv0ctlopzqox3mgg815v','.eJxVj01uhTAMhO_iNULEIT-w67tGVSHj5D1QKalI6AZx9wZKF-ys8Tfj8QYx8EgTMYd1Tl1MlHyEdtsL-NdoTYOf08iUxjB3Xz4NwWXmfYO_Gdp7CmRvglYYpQU2AlWpTG1QFvC9hJ_R-SU7XiG8Jp_RdTwChFBGodXYVIgatZWqqmH_KOC8363RL91JSrhpPfGnn48FTdMhl1eL8mSudSzfbl88LtctaqA45JxaSmSpuVFNT9bg8ylsz0pbpsZUqmaLZKxwLJDJCVURseudzuV9xcrB_gt6AHBa:1uqXQH:Uwxt71Go0aKiGB9Z4xINvdAsdR2RQSSQWrRz2EFonHk','2025-09-08 13:39:45.948000'),
('u4wcag66es7zr5mezi3qqqb77uzkkti8','.eJxVjEEOwiAQRe_C2hBhCgWX7j0DGWZAqgaS0q6Md7dNutDtf-_9twi4LiWsPc1hYnERSpx-t4j0THUH_MB6b5JaXeYpyl2RB-3y1ji9rof7d1Cwl632jM7QkA2D9w5GGjVlnTQSqeRQ5QGiJtok6y0zgbIKEFjz2RgTs_h8AfjQOGI:1undvJ:os17dhThyNjx6PsX0H0J7pOObUX9-1AsdWur3vWw110','2025-08-31 13:59:49.807000'),
('uxc6uiu0h25ocmieb8bn114ipxj2fcu7','.eJxVjEEOwiAQRe_C2hBhCgWX7j0DGWZAqgaS0q6Md7dNutDtf-_9twi4LiWsPc1hYnERSpx-t4j0THUH_MB6b5JaXeYpyl2RB-3y1ji9rof7d1Cwl632jM7QkA2D9w5GGjVlnTQSqeRQ5QGiJtok6y0zgbIKEFjz2RgTs_h8AfjQOGI:1unbqX:5lQI-PRNkUdayTPR_5GrGMLEsIrKtS8X3Y4yOvavCB0','2025-08-31 11:46:45.323000'),
('vrdscw51ksj5c2qenuhrki2kbf8hbosz','.eJxVjMsOwiAUBf-FtSFFKA-X7vsN5D5AqgaS0q6M_65NutDtmZnzEhG2tcStpyXOLC5CidPvhkCPVHfAd6i3JqnVdZlR7oo8aJdT4_S8Hu7fQYFevnVmst44xxZAg1YwhoSAI-kzQ_bBG52VQZ-t8oNBtCEADom0ymSsI_H-AAItOJU:1unxzy:lxp0Ozu48rZ7dKDkAvPVmkg2pKUUN3mIe4fH3lt-JVc','2025-09-01 11:25:58.440000'),
('wl8xowpqpy1vli3dlum9kyc4yeo3p3qt','.eJytzbsKgzAUANB_uXMQIiY-5kJbOwg6FCki6fUqwWCsiXYQ_72F_kLnM5wdnEWtjEK06-Rb55UnB9kO5-dcl4OwVOdFecojyB47zItFcl8HYwc9AYNOeQXZtBrDYB6RWrQdtRstute0_ORgPBZChpGUIhAJD3nSMLjie6x6X2yvS3W79-V_gjSI05hL2RzHB10zSPE:1uoQAv:x60hJCTb-i9EUFj49zow2FQB8VaK2TKhWI3aIRwjFtE','2025-09-02 17:31:09.797000'),
('x4few89ck6kjryxag02hba45w6a1y426','.eJxVkEFuhTAMRO_iNUJJSEJg117hbypVFTJO_icqJRUJrVTE3RsoXbCzxjNPY68QA3kckSgsU-piwuQitOtWwL-GSxrclDxh8mHqPlwags2e1xX-ZmivFMjZBC2vlWayUUKVXEkhpSjgcw5f3ro5Rx4hPEaXvYvfCZyrWgmjRcOE0EKbSjEJ21sBR4FuiW7uDmcFF61HenfTvsBx3OXyrFEennMdy6fLGc9n6oIaMA6ZI6tKUKWpUU2Pphb3Ozc9KW0Im5opSUZgbbglLggtVwyRbG91Lu8YqR367eMw-pgf6n-OfwJnmfxyy7smDzfYtl_wiXt3:1uqCtb:nDvBHIcFwZ-xARI4BEeTi5HNa9T0KmS8KZkPmtU9Vz4','2025-09-07 15:44:39.214000'),
('zos4fx4qn43vy4i0okikk65ycalaf9gs','.eJxVkMtOhTAQht9l1oS0dHrh7PQVzsbEGFJKOTQiNbRoIuHdHRAX7Cb_5et0VkjRBTta5-Iy5SZlm32C27oV8K_ZJQ9-ysHZHOLUfPg8xI4yryv8zXC7UoC6GW5cS8WEUVyVwlRc8wI-5_gVOj9T4xHjY_QUXcIO4JwbNDVyRYVKCCGlULC9FXC83yzJz82RRLhorXXvftoNO467XJ5blEfmtFP5dPnF89m6oAabBuJUlcCOIXrBlNGOtY7pWqHC3rTSo7UVx14JrR0XHo2ptRWG1m9R9uhkRdDvkIYxJLpn-DnOCZwR-U4WlzS83GHbfgGsL3nV:1uqA2K:2Y6piwZiozU4iDfHikOlbuswsBY_fnXsib3qzhXVQ00','2025-09-07 12:41:28.097000');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_site` VALUES
(1,'http://127.0.0.1:8000/','localhost'),
(2,'https://127.0.0.1:8000/','https://127.0.0.1:8000/');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `orders_order`
--

DROP TABLE IF EXISTS `orders_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_order` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `city` varchar(100) NOT NULL,
  `address` varchar(50) NOT NULL,
  `cargo` varchar(50) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  `comment` longtext NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_order_user_id_e9b59eb1_fk_auth_user_id` (`user_id`),
  CONSTRAINT `orders_order_user_id_e9b59eb1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_order`
--

LOCK TABLES `orders_order` WRITE;
/*!40000 ALTER TABLE `orders_order` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `orders_order` VALUES
(1,'','','','','','',1999.00,'2025-08-18 11:41:40.010000',1,'','1'),
(2,'','','','','','',0.00,'2025-08-18 11:41:44.528000',1,'','1'),
(3,'amir','isen','isen.osman252@gmail.com','skopje','adad','Standard',1999.00,'2025-08-18 12:13:27.399000',1,'','1'),
(4,'amir','isen','isen.osman252@gmail.com','skopje','adad','Standard',0.00,'2025-08-18 12:14:29.458000',1,'','1'),
(5,'amir','isen','isen.osman252@gmail.com','skopje','adad','Standard',999.00,'2025-08-18 12:15:58.421000',1,'','1'),
(6,'amir','isen','isen.osman252@gmail.com','skopje','adad','Express',777.00,'2025-08-18 12:25:35.845000',1,'','1'),
(7,'amir','isen','isen.osman252@gmail.com','skopje','adad','Express',0.00,'2025-08-18 12:28:02.343000',1,'','1'),
(8,'amir','isen','isen.osman252@gmail.com','skopje','adad','Standard',499.00,'2025-08-18 12:35:18.338000',1,'','1'),
(9,'amir','isen','isen.osman252@gmail.com','skopje','adad','Standard',1000.00,'2025-08-18 12:39:47.057000',1,'','1'),
(10,'amir','isen','isen.osman252@gmail.com','skopje','adad','Standard',777.00,'2025-08-18 12:49:28.363000',1,'','1'),
(11,'amir','isen','isen.osman252@gmail.com','skopje','adad','Standard',777.00,'2025-08-18 12:50:03.325000',1,'','1'),
(12,'amir','isen','isen.osman252@gmail.com','skopje','adad','Express',500.00,'2025-08-18 12:50:41.157000',1,'','1'),
(13,'is','s','isen.osma2@mgail.com','Sk','Sad','Standard',1000.00,'2025-08-18 13:32:39.679000',1,'','1'),
(14,'Isco','Disco','sen.osma@gmail.com','Skopje','AD','Standard',2399.00,'2025-08-19 13:12:57.040000',1,'','1'),
(15,'ISSEEN','OSSSMANN','isen.os@gmail.com','SKo','SU','Standard',500.00,'2025-08-19 13:14:18.683000',1,'','1'),
(16,'сфсдф','фсфсдфсд','isdasds@gmai.com','Skopje','ulsafs','Standard',1900.00,'2025-08-23 15:25:58.095000',3,'','1'),
(17,'dasdasd','adsasd','asdasdas@gmail.com','Sko','ul','Standard',1000.00,'2025-08-23 15:26:56.810000',3,'','1'),
(18,'Amir','Osman','amirosman382@gmail.com','Skopje','Brsjacka','Standard',1499.00,'2025-08-24 12:31:07.128000',4,'','1'),
(19,'Amir','Osman','amirosman382@gmail.com','Skopje','Ul brsjacka','Standard',2098.00,'2025-08-24 12:32:52.779000',4,'','1'),
(20,'Amir','Osman','amirosman382@gmail.com','Skopje','Ul brsjacka','Standard',599.00,'2025-08-24 12:35:24.803000',4,'','1'),
(21,'Amir','Osman','amirosman382@gmail.com','Skopje','Skopje','Express',599.00,'2025-08-24 12:41:41.963000',4,'','1'),
(22,'afad','sdasd','asdasd@gmail.com','sko','sdsd','Standard',999.00,'2025-08-24 12:46:31.794000',3,'','1'),
(23,'afad','sdasd','asdasd@gmail.com','sko','sdsd','Standard',0.00,'2025-08-24 12:47:03.270000',3,'','1'),
(24,'sdasd','asdsd','asdasd@gmail.com','asdasd','asdasd','Standard',999.00,'2025-08-24 12:47:30.171000',3,'','1'),
(25,'adsasd','asdasd','adasd@gmail.com','adsad','asds','Standard',999.00,'2025-08-24 12:48:11.246000',3,'','1'),
(26,'k','l','kfsdf@gmail.com','asd','vsd','Standard',999.00,'2025-08-24 12:49:17.749000',3,'','1'),
(27,'asdasda','sdasd','asdasdasd@gmail.com','asdasd','asdas','Standard',999.00,'2025-08-24 13:10:12.181000',3,'','1'),
(28,'исен','адсасд','','адсасд','сад','',999.00,'2025-08-24 14:34:00.923000',3,'асд','сдаасд'),
(29,'Isen','osman','','Skopje','ands','',999.00,'2025-08-24 14:38:42.349000',3,'s','46453434'),
(30,'Isco','Disco','','Skopje','sods','',999.00,'2025-08-24 14:48:26.282000',3,'','009343'),
(31,'Isen','Osman','','Skopje','ul brsjakca','',599.00,'2025-08-24 14:55:22.774000',3,'','0753453'),
(32,'Isen','Osman','','Skopje','adds','',999.00,'2025-08-24 14:58:20.439000',3,'','074545'),
(33,'amir','isen','','skopje','adad','',999.00,'2025-08-24 15:34:34.832000',3,'','00000'),
(34,'isen','osman','','Skopje','uldsda','',2498.00,'2025-08-24 16:58:43.212000',3,'','0595394'),
(35,'asdsd','asdasd','','sda','Fiji','',2498.00,'2025-08-25 11:22:06.079000',3,'','9999'),
(36,'ISEN','OSMAN','','SKOPJE','ULWDWD','',999.00,'2025-08-25 11:42:25.768000',3,'','075650'),
(37,'isen','osam','','asdasd','zxcas','',999.00,'2025-08-25 12:02:43.929000',3,'','12413241'),
(38,'isco','diso','','isd','sods','',999.00,'2025-08-25 12:12:23.077000',3,'','09'),
(39,'asdasd','asdasd','','asdasd','asdasd','',999.00,'2025-08-25 12:21:25.896000',3,'','2543545'),
(40,'asdas','asd','','asdasd','asdasd','',999.00,'2025-08-25 12:30:01.150000',3,'','21'),
(41,'isne','sadda','','dasd','asd','',999.00,'2025-08-25 12:31:52.561000',3,'','079334916'),
(42,'asdsd','asdasd','','Берово','sdfsdf','',999.00,'2025-08-25 13:10:39.534000',3,'','079332123'),
(43,'Isen','Osman','','Берово','dadas','',999.00,'2025-08-25 13:39:45.943000',3,'','076332456');
/*!40000 ALTER TABLE `orders_order` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `orders_orderitem`
--

DROP TABLE IF EXISTS `orders_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_orderitem` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `quantity` int(10) unsigned NOT NULL CHECK (`quantity` >= 0),
  `price` decimal(10,2) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `size` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` (`order_id`),
  KEY `orders_orderitem_product_id_afe4254a_fk_app_product_id` (`product_id`),
  CONSTRAINT `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`),
  CONSTRAINT `orders_orderitem_product_id_afe4254a_fk_app_product_id` FOREIGN KEY (`product_id`) REFERENCES `app_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_orderitem`
--

LOCK TABLES `orders_orderitem` WRITE;
/*!40000 ALTER TABLE `orders_orderitem` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `orders_orderitem` VALUES
(1,1,1000.00,1,9,NULL),
(3,1,1000.00,3,9,NULL),
(8,1,1000.00,9,9,NULL),
(12,1,1000.00,13,9,NULL),
(13,1,1000.00,14,9,NULL),
(14,1,400.00,14,11,NULL),
(17,1,1500.00,16,10,NULL),
(18,1,400.00,16,11,NULL),
(19,1,1000.00,17,9,NULL),
(20,1,1499.00,18,10,NULL),
(21,1,1499.00,19,10,NULL),
(22,1,599.00,19,15,NULL),
(23,1,599.00,20,15,NULL),
(24,1,599.00,21,15,NULL),
(25,1,999.00,24,9,NULL),
(26,1,999.00,25,9,NULL),
(27,1,999.00,26,9,NULL),
(28,1,999.00,27,9,'L'),
(29,1,999.00,28,9,'M'),
(30,1,999.00,29,9,'S'),
(31,1,999.00,30,9,'XL'),
(32,1,599.00,31,15,'L'),
(33,1,999.00,32,9,'XS'),
(34,1,999.00,33,9,'XS'),
(35,1,999.00,34,9,'S'),
(36,1,1499.00,34,10,'S'),
(37,1,999.00,35,9,'XL'),
(38,1,1499.00,35,10,'XS'),
(39,1,999.00,36,9,'M'),
(40,1,999.00,37,9,'L'),
(41,1,999.00,38,9,'M'),
(42,1,999.00,39,9,'S'),
(43,1,999.00,40,9,'XS'),
(44,1,999.00,41,9,'L'),
(45,1,999.00,42,9,'XS'),
(46,1,999.00,43,9,'XS');
/*!40000 ALTER TABLE `orders_orderitem` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `socialaccount_socialaccount`
--

DROP TABLE IF EXISTS `socialaccount_socialaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(200) NOT NULL,
  `uid` varchar(191) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`extra_data`)),
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`),
  KEY `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` (`user_id`),
  CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialaccount`
--

LOCK TABLES `socialaccount_socialaccount` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialaccount` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `socialaccount_socialaccount` VALUES
(1,'google','115752862902262683504','2025-08-25 13:38:45.570000','2025-08-20 11:22:13.367000','{\"iss\": \"https://accounts.google.com\", \"azp\": \"440079371309-pssg4klrs1o43rfidq9jl2tkivvdofjl.apps.googleusercontent.com\", \"aud\": \"440079371309-pssg4klrs1o43rfidq9jl2tkivvdofjl.apps.googleusercontent.com\", \"sub\": \"115752862902262683504\", \"email\": \"isen.osman252@gmail.com\", \"email_verified\": true, \"at_hash\": \"GSXcJuezHesKp7AY26_GLg\", \"name\": \"Isenn Osman\", \"picture\": \"https://lh3.googleusercontent.com/a/ACg8ocL1T1FhIraCS91oIJPaTeBWVePLGWS_ji3VFna5lyXFX_Jx7xg=s96-c\", \"given_name\": \"Isenn\", \"family_name\": \"Osman\", \"iat\": 1756129125, \"exp\": 1756132725}',3),
(2,'google','111848941686123335536','2025-08-24 12:30:16.378000','2025-08-20 12:42:36.621000','{\"iss\": \"https://accounts.google.com\", \"azp\": \"440079371309-pssg4klrs1o43rfidq9jl2tkivvdofjl.apps.googleusercontent.com\", \"aud\": \"440079371309-pssg4klrs1o43rfidq9jl2tkivvdofjl.apps.googleusercontent.com\", \"sub\": \"111848941686123335536\", \"email\": \"amirosman382@gmail.com\", \"email_verified\": true, \"at_hash\": \"K51iqI-CMAL7TJBEUaC3mw\", \"name\": \"Amir Osman\", \"picture\": \"https://lh3.googleusercontent.com/a/ACg8ocJlUXJBikCE17TWFeVDVtxoQJKuYzUtdHsNw4lypOYBqMMndfee=s96-c\", \"given_name\": \"Amir\", \"family_name\": \"Osman\", \"iat\": 1756038616, \"exp\": 1756042216}',4);
/*!40000 ALTER TABLE `socialaccount_socialaccount` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `socialaccount_socialapp`
--

DROP TABLE IF EXISTS `socialaccount_socialapp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialapp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) NOT NULL,
  `name` varchar(40) NOT NULL,
  `client_id` varchar(191) NOT NULL,
  `secret` varchar(191) NOT NULL,
  `key` varchar(191) NOT NULL,
  `provider_id` varchar(200) NOT NULL,
  `settings` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`settings`)),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialapp`
--

LOCK TABLES `socialaccount_socialapp` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialapp` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `socialaccount_socialapp` VALUES
(1,'facebook','Facebook-login','778394211355420','ab7fd475c1ac7b222172f4cfc30f0d4b','','','{}'),
(2,'google','Google-login','440079371309-pssg4klrs1o43rfidq9jl2tkivv','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','','','{}');
/*!40000 ALTER TABLE `socialaccount_socialapp` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `socialaccount_socialapp_sites`
--

DROP TABLE IF EXISTS `socialaccount_socialapp_sites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialapp_sites` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `socialapp_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id`,`site_id`),
  KEY `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id`),
  CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc` FOREIGN KEY (`socialapp_id`) REFERENCES `socialaccount_socialapp` (`id`),
  CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialapp_sites`
--

LOCK TABLES `socialaccount_socialapp_sites` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialapp_sites` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `socialaccount_socialapp_sites` VALUES
(1,1,1),
(2,2,2);
/*!40000 ALTER TABLE `socialaccount_socialapp_sites` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `socialaccount_socialtoken`
--

DROP TABLE IF EXISTS `socialaccount_socialtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialtoken` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `token_secret` longtext NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `app_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`),
  KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`),
  CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialtoken`
--

LOCK TABLES `socialaccount_socialtoken` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialtoken` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `socialaccount_socialtoken` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `wishlist_wishlist`
--

DROP TABLE IF EXISTS `wishlist_wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `wishlist_wishlist` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `wishlist_wishlist_user_id_13f28b16_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishlist_wishlist`
--

LOCK TABLES `wishlist_wishlist` WRITE;
/*!40000 ALTER TABLE `wishlist_wishlist` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `wishlist_wishlist` VALUES
(1,1),
(3,3),
(2,4);
/*!40000 ALTER TABLE `wishlist_wishlist` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `wishlist_wishlist_products`
--

DROP TABLE IF EXISTS `wishlist_wishlist_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `wishlist_wishlist_products` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `wishlist_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wishlist_wishlist_products_wishlist_id_product_id_8df7c4d2_uniq` (`wishlist_id`,`product_id`),
  KEY `wishlist_wishlist_products_product_id_95aa7492_fk_app_product_id` (`product_id`),
  CONSTRAINT `wishlist_wishlist_pr_wishlist_id_ef5d74ba_fk_wishlist_` FOREIGN KEY (`wishlist_id`) REFERENCES `wishlist_wishlist` (`id`),
  CONSTRAINT `wishlist_wishlist_products_product_id_95aa7492_fk_app_product_id` FOREIGN KEY (`product_id`) REFERENCES `app_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishlist_wishlist_products`
--

LOCK TABLES `wishlist_wishlist_products` WRITE;
/*!40000 ALTER TABLE `wishlist_wishlist_products` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `wishlist_wishlist_products` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `wishlist_wishlistproduct`
--

DROP TABLE IF EXISTS `wishlist_wishlistproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `wishlist_wishlistproduct` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `size` varchar(5) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `wishlist_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wishlist_wishlistproduct_product_id_8e8c26f2_fk_app_product_id` (`product_id`),
  KEY `wishlist_wishlistpro_wishlist_id_9b8eed73_fk_wishlist_` (`wishlist_id`),
  CONSTRAINT `wishlist_wishlistpro_wishlist_id_9b8eed73_fk_wishlist_` FOREIGN KEY (`wishlist_id`) REFERENCES `wishlist_wishlist` (`id`),
  CONSTRAINT `wishlist_wishlistproduct_product_id_8e8c26f2_fk_app_product_id` FOREIGN KEY (`product_id`) REFERENCES `app_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishlist_wishlistproduct`
--

LOCK TABLES `wishlist_wishlistproduct` WRITE;
/*!40000 ALTER TABLE `wishlist_wishlistproduct` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `wishlist_wishlistproduct` VALUES
(1,'M',9,3);
/*!40000 ALTER TABLE `wishlist_wishlistproduct` ENABLE KEYS */;
UNLOCK TABLES;
commit;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-08-25 21:14:58
