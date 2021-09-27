-- MariaDB dump 10.19  Distrib 10.6.4-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: db_users
-- ------------------------------------------------------
-- Server version	10.6.4-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `logins`
--

DROP TABLE IF EXISTS `logins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logins` (
  `login` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `BDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logins`
--

LOCK TABLES `logins` WRITE;
/*!40000 ALTER TABLE `logins` DISABLE KEYS */;
INSERT INTO `logins` VALUES ('admin','pass','1989-09-25'),('admin2','passw','2021-08-14'),('admin3','pas_admin','2020-06-12'),('ADMIN','parol','1983-10-17'),('new_user','user','1984-11-29'),('ann','1234','1997-05-15'),('user1234','123456','2000-11-02'),('drakon','0987','2003-04-15'),('user404','0000','1993-01-19');
/*!40000 ALTER TABLE `logins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `Name` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_520_ci DEFAULT NULL,
  `Telephone` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_520_ci DEFAULT NULL,
  `BDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Васин Василий','+7213345324','2000-06-04'),('Горина Анастасия','+7345675334','1995-08-05'),('Лебедев Иван','+7541611256','1986-09-17'),('Иванов Петр','+7954123388','1981-10-08'),('Оськина Екатерина','+7921457230','1997-08-14'),('Егоров Артем','+7176348999','1985-09-27'),('Шпагин Антон','+7111437752','2001-03-14'),('Астафьев Илья','+7954787008','1997-09-30'),('Борисов Денис ','+7900567811','2002-10-02'),('Мухоморов Дмитрий','+7980118674','1975-10-01'),('Просандеева Антонина','+7921768523','1996-10-06'),('Трухина Оксана','+7911567942','1975-08-26'),('Поляков Никита','+7935758007','1988-04-19'),('Кудрявцев Герман','+7911456970','1981-01-22'),('Теньков Дмитрий','+7935370738','1999-06-30'),('Соловьева Татьяна','+7911492670','1979-12-18'),('Хрущов Олег','+7935689564','1969-11-09'),('Яшина Яна','+7911785038','2021-09-26'),('Прусаков Павел','+7945768430','1990-07-23');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-27 13:59:14
