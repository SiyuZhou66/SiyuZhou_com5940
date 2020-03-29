-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 26, 2020 at 06:37 PM
-- Server version: 5.7.26
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hkphoto`
--

-- --------------------------------------------------------

--
-- Table structure for table `hkphoto`
--

CREATE TABLE `hkphoto` (
  `ID` int(2) DEFAULT NULL,
  `Name` varchar(32) DEFAULT NULL,
  `Photo` varchar(111) DEFAULT NULL,
  `Address` varchar(78) DEFAULT NULL,
  `NearStation` varchar(16) DEFAULT NULL,
  `Unique` varchar(139) DEFAULT NULL,
  `InstagramNo` int(5) DEFAULT NULL,
  `Region` varchar(16) DEFAULT NULL,
  `Image_url` varchar(93) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `hkphoto`
--

INSERT INTO `hkphoto` (`ID`, `Name`, `Photo`, `Address`, `NearStation`, `Unique`, `InstagramNo`, `Region`, `Image_url`) VALUES
(1, ' LOK WAH SOUTH ESTATE', '1.jpg (https://dl.airtable.com/.attachments/24d60cd7b03e773d86dd9af849a0f9f2/812874ac/1.jpg)', 'G/F, On Wah House, Lok Wah (South) Estate, Ngau Tau Kok, Kowloon, Ngau Tau Kok', 'Ngau Tau Kok', 'overlay-ed square ', 2264, 'Kowloon', 'https://dl.airtable.com/.attachments/24d60cd7b03e773d86dd9af849a0f9f2/812874ac/1.jpg'),
(2, 'PING SHEK ESTATE', '2.jpg (https://dl.airtable.com/.attachments/c1ca24df7bbdc0051648eb34981a36f6/486d8672/2.jpg)', '2 Clear Water Bay Rd, Ping Shan', 'Choi Hung', 'trippy condo stack', 1455, 'New Territories', 'https://dl.airtable.com/.attachments/c1ca24df7bbdc0051648eb34981a36f6/486d8672/2.jpg'),
(3, 'CHOI HUNG ESTATE', '3.jpg (https://dl.airtable.com/.attachments/25ab3aaf60707a2d9759feb931bd1467/f647008b/3.jpg)', '2 Tse Wai Ave, Choi Hung Estate', 'Choi Hung', 'colourful condo and basketball court combo', 17637, 'New Territories', 'https://dl.airtable.com/.attachments/25ab3aaf60707a2d9759feb931bd1467/f647008b/3.jpg'),
(4, 'CHI LIN NUNNERY', '4.jpg (https://dl.airtable.com/.attachments/96bcb95edf62589b820e6754a94338af/464a6883/4.jpg)', '5 Chi Lin Dr, Diamond Hill', 'Diamond Hill', 'elegant wooden buildings', 14666, 'New Territories', 'https://dl.airtable.com/.attachments/96bcb95edf62589b820e6754a94338af/464a6883/4.jpg'),
(5, 'YUEN PO BIRD GARDEN', '6.jpg (https://dl.airtable.com/.attachments/548c6ec44eb24fc5dead2201e69d8faa/33c4f25f/6.jpg)', 'Yuen Po Street, Mong Kok, Prince Edward', 'Prince Edward', 'exotic birds, bamboo cages', 136, 'Kowloon', 'https://dl.airtable.com/.attachments/548c6ec44eb24fc5dead2201e69d8faa/33c4f25f/6.jpg'),
(6, 'FLOWER MARKET', '7.png (https://dl.airtable.com/.attachments/fd9882d52faa2b50ca7837b6acbb768e/8b3f88c6/7.png)', 'Flower Market Rd, Prince Edward', 'Prince Edward', 'tons of flower shops', 645, 'Kowloon', 'https://dl.airtable.com/.attachments/fd9882d52faa2b50ca7837b6acbb768e/8b3f88c6/7.png'),
(7, 'MAN MO TEMPLE', '9.jpg (https://dl.airtable.com/.attachments/18265c75fe07ceef69e0f5d9172c277b/5254d3ed/9.jpg)', '124-126 No. Hollywood Rd, Sheung Wan', 'Sheung Wan', 'gorgeous transitional temple', 22918, 'Hong Kong Island', 'https://dl.airtable.com/.attachments/18265c75fe07ceef69e0f5d9172c277b/5254d3ed/9.jpg'),
(8, ' TANK LANE', '10.jpg (https://dl.airtable.com/.attachments/8a8818ca066e6d94f507cb2b18bfecc9/e84250dd/10.jpg)', '1 U Lam Terrace, Sheung Wan', 'Sheung Wan', 'street art', 307, 'Hong Kong Island', 'https://dl.airtable.com/.attachments/8a8818ca066e6d94f507cb2b18bfecc9/e84250dd/10.jpg'),
(9, 'NAM SHAN ESTATE PLAYGROUND', 'Nam SHan.jpg (https://dl.airtable.com/.attachments/6601e3c57c3e3d3938d0738e4678f413/82d9161c/NamSHan.jpg)', 'Nam Shan Chuen Rd, Kowloon Tsai', 'Kowloon Tong', 'the playground area, promises symmetry, perfect lighting and all-round coolness.', 3020, 'Kowloon', 'https://dl.airtable.com/.attachments/6601e3c57c3e3d3938d0738e4678f413/82d9161c/NamSHan.jpg'),
(10, 'LAI TAK TSUEN', 'LAI TAK.jpg (https://dl.airtable.com/.attachments/ac9c9cda166dbe60253e9d5060eb2b85/ed2a37fb/LAITAK.jpg)', 'Lai Tak Tsuen Rd, Tai Hang', 'Tin Hau', 'the estate’s blue colour echoes the warmness of a summer sky', 1533, 'Hong Kong Island', 'https://dl.airtable.com/.attachments/ac9c9cda166dbe60253e9d5060eb2b85/ed2a37fb/LAITAK.jpg'),
(11, 'JOCKEY CLUB INNOVATION TOWER', 'JOCKEY CLUB.jpg (https://dl.airtable.com/.attachments/20f78de8cecf5be33157bf20165f1f0a/a770c16b/JOCKEYCLUB.jpg)', 'The Hong Kong Polytechnic University, Hung Hom', 'Hung Hom Station', 'The white interiors and crisscrossing staircases emit a sleek and chic feel.', 809, 'Kowloon', 'https://dl.airtable.com/.attachments/20f78de8cecf5be33157bf20165f1f0a/a770c16b/JOCKEYCLUB.jpg'),
(12, 'SAI WAN SWIMMING SHED', 'SAi WAn.jpg (https://dl.airtable.com/.attachments/63ecf6498ffdff6e1c7330281647d0d8/780c72d5/SAiWAn.jpg)', 'Victoria Rd, Mount Davis', 'Kennedy Town', 'this gem offers a picturesque view of crashing waves and seaside views.', 3769, 'Hong Kong Island', 'https://dl.airtable.com/.attachments/63ecf6498ffdff6e1c7330281647d0d8/780c72d5/SAiWAn.jpg'),
(13, 'WAI YIP STREET PEDESTRIAN BRIDGE', 'WAI YIP.jpg (https://dl.airtable.com/.attachments/1a4a10c0e6447e6afa3ff41af12d681c/8aa9c1b9/WAIYIP.jpg)', 'Tsun Yip St, Kwun Tong', 'Ngau Tau Kok', 'the spot is hailed for its cool views on the outside, brushed concrete streaked with colour on the inside and generally endless photo ops. ', 174, 'Kowloon', 'https://dl.airtable.com/.attachments/1a4a10c0e6447e6afa3ff41af12d681c/8aa9c1b9/WAIYIP.jpg');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
