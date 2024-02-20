-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 20, 2024 at 11:14 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `members_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `member_d`
--

CREATE TABLE `member_d` (
  `MEMID` varchar(50) NOT NULL,
  `FNAME` varchar(50) NOT NULL,
  `LNAME` date NOT NULL,
  `ADDRESS` varchar(50) NOT NULL,
  `PHONE` varchar(50) NOT NULL,
  `PHONE1` int(11) NOT NULL,
  `PHONE2` varchar(50) NOT NULL,
  `DEGRY` varchar(20) NOT NULL,
  `SALARY` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `member_doctor`
--

CREATE TABLE `member_doctor` (
  `MEMID` varchar(50) NOT NULL,
  `FNAME` varchar(50) NOT NULL,
  `LNAME` date NOT NULL,
  `ADDRESS` varchar(50) NOT NULL,
  `PHONE` varchar(50) NOT NULL,
  `PHONE1` int(11) NOT NULL,
  `PHONE2` varchar(50) NOT NULL,
  `DEGRY` varchar(20) NOT NULL,
  `SALARY` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `member_master`
--

CREATE TABLE `member_master` (
  `MEMID` varchar(50) NOT NULL,
  `FNAME` varchar(50) NOT NULL,
  `LNAME` date NOT NULL,
  `ADDRESS` varchar(50) NOT NULL,
  `PHONE` varchar(50) NOT NULL,
  `PHONE1` int(11) NOT NULL,
  `PHONE2` varchar(50) NOT NULL,
  `DEGRY` varchar(20) NOT NULL,
  `SALARY` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `member_mo`
--

CREATE TABLE `member_mo` (
  `MEMID` varchar(50) NOT NULL,
  `FNAME` varchar(50) NOT NULL,
  `LNAME` date NOT NULL,
  `ADDRESS` varchar(50) NOT NULL,
  `PHONE` varchar(50) NOT NULL,
  `PHONE1` int(11) NOT NULL,
  `PHONE2` varchar(50) NOT NULL,
  `DEGRY` varchar(20) NOT NULL,
  `SALARY` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member_mo`
--

INSERT INTO `member_mo` (`MEMID`, `FNAME`, `LNAME`, `ADDRESS`, `PHONE`, `PHONE1`, `PHONE2`, `DEGRY`, `SALARY`) VALUES
('2233445566', 'اماني الطاهر', '2003-10-10', 'درجة تاسعة', '2014-10-10', 6, 'معلم', 'بكالوريس', '600'),
('888262', 'خالد خالد', '2003-12-12', 'سابعة', '2020-10-10', 0, 'معلم', 'بكالوريس', '700');

-- --------------------------------------------------------

--
-- Table structure for table `member_tab`
--

CREATE TABLE `member_tab` (
  `MEMID` varchar(50) NOT NULL,
  `FNAME` varchar(50) NOT NULL,
  `LNAME` date NOT NULL,
  `ADDRESS` varchar(50) NOT NULL,
  `PHONE` varchar(50) NOT NULL,
  `PHONE1` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member_tab`
--

INSERT INTO `member_tab` (`MEMID`, `FNAME`, `LNAME`, `ADDRESS`, `PHONE`, `PHONE1`) VALUES
('1234567890', 'الخالدي احمد', '2024-12-12', 'تعديل', 'معلم', '2024-10-19'),
('22334455', 'alaahmed', '2009-10-10', 'khamsa', '2004-20-20', '0000-00-00'),
('224444', 'alaahmed', '2009-10-10', 'khamsa', '2004-20-20', '0000-00-00'),
('225', 'alaahmed', '2009-10-10', 'khamsa', '2004-20-20', '0000-00-00');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `name`, `password`) VALUES
(112233, 'admin', 'admin1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `member_d`
--
ALTER TABLE `member_d`
  ADD PRIMARY KEY (`MEMID`);

--
-- Indexes for table `member_doctor`
--
ALTER TABLE `member_doctor`
  ADD PRIMARY KEY (`MEMID`);

--
-- Indexes for table `member_mo`
--
ALTER TABLE `member_mo`
  ADD PRIMARY KEY (`MEMID`);

--
-- Indexes for table `member_tab`
--
ALTER TABLE `member_tab`
  ADD PRIMARY KEY (`MEMID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
