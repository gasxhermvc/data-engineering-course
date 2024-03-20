-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 14, 2023 at 05:15 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `final`
--

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `ID` bigint(20) NOT NULL,
  `CELL_STATUS` varchar(255) NOT NULL,
  `LATITUDE` double(16,6) NOT NULL,
  `LONGITUDE` double(16,6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`ID`, `CELL_STATUS`, `LATITUDE`, `LONGITUDE`) VALUES
(1, 'ACTIVE', 99.957221, 12.716940),
(2, 'ACTIVE', 99.957221, 12.716940),
(3, 'ACTIVE', 99.957221, 12.716940),
(4, 'ACTIVE', 99.951070, 12.658170),
(5, 'ACTIVE', 99.951070, 12.658170),
(6, 'ACTIVE', 99.951070, 12.658170),
(7, 'ACTIVE', 99.970718, 12.775495),
(8, 'ACTIVE', 99.970718, 12.775495),
(9, 'ACTIVE', 99.970718, 12.775495),
(10, 'ACTIVE', 99.963608, 12.795559),
(11, 'ACTIVE', 99.963608, 12.795559),
(12, 'ACTIVE', 99.963608, 12.795559),
(13, 'ACTIVE', 99.948865, 12.636692),
(14, 'ACTIVE', 99.951908, 12.815217),
(15, 'ACTIVE', 99.951908, 12.815217),
(16, 'ACTIVE', 99.959450, 12.670350),
(17, 'ACTIVE', 99.959450, 12.670350),
(18, 'ACTIVE', 99.952260, 12.643980),
(19, 'ACTIVE', 99.952260, 12.643980),
(20, 'ACTIVE', 99.952260, 12.643980),
(21, 'ACTIVE', 99.985278, 12.814152),
(22, 'ACTIVE', 99.985278, 12.814152),
(23, 'ACTIVE', 99.985278, 12.814152),
(24, 'ACTIVE', 99.937361, 12.824000),
(25, 'ACTIVE', 99.937361, 12.824000),
(26, 'ACTIVE', 99.937361, 12.824000),
(27, 'ACTIVE', 99.937361, 12.824000),
(28, 'ACTIVE', 99.952778, 12.686667),
(29, 'ACTIVE', 99.952778, 12.686667),
(30, 'ACTIVE', 99.952778, 12.686667),
(31, 'ACTIVE', 99.933259, 12.830848),
(32, 'ACTIVE', 99.931467, 12.831848),
(33, 'ACTIVE', 99.931467, 12.831848),
(34, 'ACTIVE', 99.941896, 12.816205),
(35, 'ACTIVE', 99.941896, 12.816205),
(36, 'ACTIVE', 99.952580, 12.703570),
(37, 'ACTIVE', 99.952580, 12.703570),
(38, 'ACTIVE', 99.952580, 12.703570),
(39, 'ACTIVE', 99.971806, 12.798111),
(40, 'ACTIVE', 99.971806, 12.798111),
(41, 'ACTIVE', 99.971806, 12.798111),
(42, 'ACTIVE', 99.946820, 12.671150),
(43, 'ACTIVE', 99.946820, 12.671150),
(44, 'ACTIVE', 99.946820, 12.671150),
(45, 'ACTIVE', 99.946820, 12.671150);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `location`
--
ALTER TABLE `location`
  MODIFY `ID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
