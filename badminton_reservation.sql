-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 26, 2023 at 05:26 PM
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
-- Database: `badminton_reservation`
--

-- --------------------------------------------------------

--
-- Table structure for table `player_information`
--

CREATE TABLE `player_information` (
  `player_name` varchar(40) NOT NULL,
  `court_number` varchar(30) NOT NULL,
  `number_of_players` int(20) NOT NULL,
  `number_of_hours` int(20) NOT NULL,
  `total_cost` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `player_information`
--

INSERT INTO `player_information` (`player_name`, `court_number`, `number_of_players`, `number_of_hours`, `total_cost`) VALUES
('hairiena', 'C2', 16, 3, 400),
('ifa', 'C2', 1, 2, 20),
('hairiena', 'C4', 1, 3, 75),
('hairiena', 'C4', 1, 3, 75),
('umairah', 'C2', 2, 6, 228),
('siti', 'C3', 3, 3, 75),
('om', 'C2', 1, 7, 299),
('Y', 'C4', 5, 6, 81),
('Y', 'C4', 2, 4, 60);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
