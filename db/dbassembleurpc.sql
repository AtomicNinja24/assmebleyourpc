-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 06, 2021 at 09:06 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dbassembleurpc`
--

-- --------------------------------------------------------

--
-- Table structure for table `tblassemble`
--

CREATE TABLE IF NOT EXISTS `tblassemble` (
  `asId` int(11) NOT NULL AUTO_INCREMENT,
  `cEmail` varchar(50) NOT NULL,
  `req` varchar(50) NOT NULL,
  `disId` int(11) NOT NULL,
  `hddId` int(11) NOT NULL,
  `proId` int(11) NOT NULL,
  `ramId` int(11) NOT NULL,
  `total` bigint(20) NOT NULL,
  `status` varchar(50) NOT NULL,
  `odate` datetime NOT NULL,
  PRIMARY KEY (`asId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `tblassemble`
--

INSERT INTO `tblassemble` (`asId`, `cEmail`, `req`, `disId`, `hddId`, `proId`, `ramId`, `total`, `status`, `odate`) VALUES
(1, 'shilpa@gmail.com', 'Basic use', 1, 1, 1, 1, 15093, 'delivered', '0000-00-00 00:00:00'),
(2, 'shilpa@gmail.com', 'Basic use', 1, 1, 1, 1, 15093, 'passed to courier', '0000-00-00 00:00:00'),
(3, 'shilpa@gmail.com', 'Basic use', 1, 1, 1, 1, 15093, 'ordered', '2020-03-17 17:31:21'),
(4, 'shilpa@gmail.com', 'Basic use', 1, 1, 1, 1, 15093, 'ordered', '2020-03-18 10:26:53'),
(5, 'shilpa@gmail.com', 'Basic use', 1, 1, 1, 1, 15093, 'Delivered', '2020-03-18 10:54:04'),
(6, 'shilpa@gmail.com', 'Office use', 2, 2, 2, 2, 17082, 'ordered', '2020-03-20 01:50:57'),
(7, 'shilpa@gmail.com', 'Basic use', 1, 1, 1, 1, 15093, 'ordered', '2020-03-20 01:57:19'),
(8, 'shilpa@gmail.com', 'Office use', 2, 2, 2, 2, 17082, 'ordered', '2020-03-20 02:14:33'),
(9, 'binil@gmail.com', 'Basic use', 1, 1, 1, 1, 15093, 'ordered', '2021-02-05 15:23:45');

-- --------------------------------------------------------

--
-- Table structure for table `tblbrand`
--

CREATE TABLE IF NOT EXISTS `tblbrand` (
  `brandId` int(11) NOT NULL AUTO_INCREMENT,
  `brandName` varchar(50) NOT NULL,
  `brandStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`brandId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `tblbrand`
--

INSERT INTO `tblbrand` (`brandId`, `brandName`, `brandStatus`) VALUES
(1, 'Dell', '1'),
(2, 'Crucial', '1'),
(3, 'HP', '1'),
(4, 'Seagate', '1'),
(5, 'AMD', '1'),
(6, 'Intel', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblcart`
--

CREATE TABLE IF NOT EXISTS `tblcart` (
  `cartId` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `pid` int(11) NOT NULL,
  `odate` date NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`cartId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tblcart`
--

INSERT INTO `tblcart` (`cartId`, `email`, `pid`, `odate`, `status`) VALUES
(1, 'binil@gmail.com', 2, '2021-02-05', 'delivered');

-- --------------------------------------------------------

--
-- Table structure for table `tblcategory`
--

CREATE TABLE IF NOT EXISTS `tblcategory` (
  `catId` int(11) NOT NULL AUTO_INCREMENT,
  `catName` varchar(50) NOT NULL,
  `catStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`catId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tblcategory`
--

INSERT INTO `tblcategory` (`catId`, `catName`, `catStatus`) VALUES
(1, 'PC', '1'),
(2, 'Laptop', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tbldisplay`
--

CREATE TABLE IF NOT EXISTS `tbldisplay` (
  `dsId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `size` varchar(50) NOT NULL,
  `resolution` varchar(50) NOT NULL,
  `panel` varchar(50) NOT NULL,
  `speciality` varchar(50) NOT NULL,
  `bid` int(11) NOT NULL,
  `rate` bigint(20) NOT NULL,
  PRIMARY KEY (`dsId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tbldisplay`
--

INSERT INTO `tbldisplay` (`dsId`, `name`, `size`, `resolution`, `panel`, `speciality`, `bid`, `rate`) VALUES
(1, 'Dell 19.5 inch (49.41 cm) LED Backlit', '19.5inch', '4324', 'gfbdrg', 'Basic use', 1, 4500),
(2, 'HP 23.8-inch (60.45 cm) Edge to Edge', '23.8inch', '3423', 'fgver', 'Office use', 3, 4500);

-- --------------------------------------------------------

--
-- Table structure for table `tblhdd`
--

CREATE TABLE IF NOT EXISTS `tblhdd` (
  `hid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `capacity` varchar(50) NOT NULL,
  `speed` varchar(50) NOT NULL,
  `speciality` varchar(100) NOT NULL,
  `bid` int(11) NOT NULL,
  `rate` bigint(20) NOT NULL,
  PRIMARY KEY (`hid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tblhdd`
--

INSERT INTO `tblhdd` (`hid`, `name`, `capacity`, `speed`, `speciality`, `bid`, `rate`) VALUES
(1, 'HP F6V97AA#ACJ', '2Tb', '4324', 'Basic use', 3, 3750),
(2, 'Seagate Barracuda 2TB HDD', '2Tb', '4324', 'Office use', 4, 4500);

-- --------------------------------------------------------

--
-- Table structure for table `tbllogin`
--

CREATE TABLE IF NOT EXISTS `tbllogin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbllogin`
--

INSERT INTO `tbllogin` (`username`, `password`, `utype`, `status`) VALUES
('shilpa@gmail.com', 'shilpa@123', 'customer', '1'),
('admin@gmail.com', 'admin', 'admin', '1'),
('shon@123', 'shon@123', 'customer', '1'),
('binil@gmail.com', 'binil@123', 'customer', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblprocessor`
--

CREATE TABLE IF NOT EXISTS `tblprocessor` (
  `proId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `cache` varchar(50) NOT NULL,
  `speed` varchar(50) NOT NULL,
  `speciality` varchar(50) NOT NULL,
  `bid` int(11) NOT NULL,
  `rate` bigint(20) NOT NULL,
  PRIMARY KEY (`proId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tblprocessor`
--

INSERT INTO `tblprocessor` (`proId`, `name`, `cache`, `speed`, `speciality`, `bid`, `rate`) VALUES
(1, 'Intel Core 2 Duo E8500 Dual-Core', '534', '45345', 'Basic use', 6, 2343),
(2, 'AMD RYZEN 5 3500 3RD Gen', '423', '45353', 'Office use', 5, 4332);

-- --------------------------------------------------------

--
-- Table structure for table `tblproducts`
--

CREATE TABLE IF NOT EXISTS `tblproducts` (
  `pId` int(11) NOT NULL AUTO_INCREMENT,
  `catId` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `speciality` varchar(50) NOT NULL,
  `img` varchar(100) NOT NULL,
  `rate` varchar(50) NOT NULL,
  PRIMARY KEY (`pId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tblproducts`
--

INSERT INTO `tblproducts` (`pId`, `catId`, `name`, `description`, `speciality`, `img`, `rate`) VALUES
(1, 2, 'erfgtesr', 'sdbrsdtgrt', 'Basic use', '/media/71Kl8IPrRyL._SX355__D6cd4cK.jpg', '45000'),
(2, 2, 'k', 'kj', 'Budget friendly', '/media/b2.jpg', '45000');

-- --------------------------------------------------------

--
-- Table structure for table `tblram`
--

CREATE TABLE IF NOT EXISTS `tblram` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `size` varchar(50) NOT NULL,
  `speed` varchar(50) NOT NULL,
  `speciality` varchar(100) NOT NULL,
  `bid` int(11) NOT NULL,
  `rate` bigint(20) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tblram`
--

INSERT INTO `tblram` (`rid`, `name`, `size`, `speed`, `speciality`, `bid`, `rate`) VALUES
(1, 'ADATA 8GB DDR4', '8GB', '453', 'Basic use', 1, 4500),
(2, 'Crucial 8GB DDR4', '8GB', '423', 'Office use', 2, 3750);

-- --------------------------------------------------------

--
-- Table structure for table `tblregistration`
--

CREATE TABLE IF NOT EXISTS `tblregistration` (
  `uName` varchar(50) NOT NULL,
  `uAddress` varchar(100) NOT NULL,
  `uContact` varchar(50) NOT NULL,
  `uEmail` varchar(50) NOT NULL,
  PRIMARY KEY (`uEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblregistration`
--

INSERT INTO `tblregistration` (`uName`, `uAddress`, `uContact`, `uEmail`) VALUES
('Binil', 'jnh', '8547961023', 'binil@gmail.com'),
('Shilpa', 'sergser\r\nsght', '9512364781', 'shilpa@gmail.com'),
('shon', 'uuyiyity', '9856321475', 'shon@123');
