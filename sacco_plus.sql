-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Nov 28, 2018 at 01:23 PM
-- Server version: 5.7.23
-- PHP Version: 7.1.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sacco_plus`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `memno` int(11) NOT NULL,
  `amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`memno`, `amount`) VALUES
(71205758, 0);

-- --------------------------------------------------------

--
-- Table structure for table `beneficiaries`
--

CREATE TABLE `beneficiaries` (
  `id` int(11) NOT NULL,
  `MemNo` int(11) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Member_Memno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `contribution`
--

CREATE TABLE `contribution` (
  `contno` text NOT NULL,
  `memno` varchar(10) NOT NULL,
  `contdate` text NOT NULL,
  `amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `contribution`
--

INSERT INTO `contribution` (`contno`, `memno`, `contdate`, `amount`) VALUES
('CONT61636', '11957740', '2018-11-21', 5000),
('CONT21423', '11957740', '2018-11-30', 8000),
('CONT31142', '71205758', '2018-11-29', 2007);

-- --------------------------------------------------------

--
-- Table structure for table `contributions`
--

CREATE TABLE `contributions` (
  `memno` int(11) NOT NULL,
  `cont_no` varchar(45) DEFAULT NULL,
  `amount` varchar(45) DEFAULT NULL,
  `cont_date` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `loan`
--

CREATE TABLE `loan` (
  `loanid` varchar(11) NOT NULL,
  `memno` varchar(11) NOT NULL,
  `date` text NOT NULL,
  `amount` float NOT NULL,
  `status` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `loan`
--

INSERT INTO `loan` (`loanid`, `memno`, `date`, `amount`, `status`) VALUES
('31190949', '11957740', '2018-11-30', 4000, 'waiting'),
('51638820', '11957740', '2018-11-29', 308, 'waiting'),
('28173545', '71205758', '2018-11-28', 5000, 'waiting');

-- --------------------------------------------------------

--
-- Table structure for table `loanapplication`
--

CREATE TABLE `loanapplication` (
  `Loan_id` int(11) NOT NULL,
  `Status` varchar(45) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Amount` int(11) DEFAULT NULL,
  `Appproved_amount` int(11) DEFAULT NULL,
  `Guarantors` varchar(45) DEFAULT NULL,
  `Balance` varchar(45) DEFAULT NULL,
  `Memno` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `loanprocessing`
--

CREATE TABLE `loanprocessing` (
  `id` int(11) NOT NULL,
  `status` varchar(45) DEFAULT NULL,
  `DisqualificationReason` varchar(45) DEFAULT NULL,
  `LoanType_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `loanrepayment`
--

CREATE TABLE `loanrepayment` (
  `id` int(11) NOT NULL,
  `Amount` int(11) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Balance` int(11) DEFAULT NULL,
  `LoanType_id` int(11) NOT NULL,
  `LoanType_LoanApplication_Loan_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `loantype`
--

CREATE TABLE `loantype` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `min_amount` int(11) DEFAULT NULL,
  `Max_amount` int(11) DEFAULT NULL,
  `period` date DEFAULT NULL,
  `LoanApplication_Loan_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `management`
--

CREATE TABLE `management` (
  `Official_no` int(11) NOT NULL,
  `Position` varchar(45) DEFAULT NULL,
  `Memno` int(11) DEFAULT NULL,
  `Term_start` datetime DEFAULT NULL,
  `Term_end` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `Memno` int(11) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `Description` varchar(45) DEFAULT NULL,
  `credibility` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`Memno`, `Name`, `Email`, `Phone`, `Description`, `credibility`) VALUES
(11034530, 'coni nico', 'nicodemusopon@gmail.com', '707584688', 'nio', 23);

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `Memno` varchar(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `phone` text NOT NULL,
  `description` text NOT NULL,
  `credibility` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`Memno`, `name`, `email`, `phone`, `description`, `credibility`) VALUES
('11957740', 'nicopon', 'nicopon@gmail.com', '707584488', 'test user', 18),
('71205758', 'john', 'john@gmail.com', '707674688', 'none', 18);

-- --------------------------------------------------------

--
-- Table structure for table `member_has_contributions`
--

CREATE TABLE `member_has_contributions` (
  `Member_Memno` int(11) NOT NULL,
  `Contributions_memno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `organization`
--

CREATE TABLE `organization` (
  `No` int(11) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Phone` varchar(8) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Website` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `total_contributions`
--

CREATE TABLE `total_contributions` (
  `memno` varchar(11) NOT NULL,
  `amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `total_contributions`
--

INSERT INTO `total_contributions` (`memno`, `amount`) VALUES
('11957740', 13000),
('71205758', 2007);

-- --------------------------------------------------------

--
-- Table structure for table `total_dividends`
--

CREATE TABLE `total_dividends` (
  `memno` varchar(11) NOT NULL,
  `amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `total_dividends`
--

INSERT INTO `total_dividends` (`memno`, `amount`) VALUES
('11957740', 86.6262),
('71205758', 13.3738);

-- --------------------------------------------------------

--
-- Table structure for table `total_loans`
--

CREATE TABLE `total_loans` (
  `memno` varchar(11) NOT NULL,
  `amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `total_loans`
--

INSERT INTO `total_loans` (`memno`, `amount`) VALUES
('11957740', 4308),
('71205758', 5000);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(86) NOT NULL,
  `password` varchar(86) NOT NULL,
  `role` varchar(86) NOT NULL,
  `memno` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `password`, `role`, `memno`) VALUES
('nicopon', '860643fc84b6de4de58aae9bc85f3173', 'User', '11957740'),
('john', '527bd5b5d689e2c32ae974c6229ff785', 'User', '71205758');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `beneficiaries`
--
ALTER TABLE `beneficiaries`
  ADD PRIMARY KEY (`id`,`Member_Memno`),
  ADD KEY `fk_Beneficiaries_Member1_idx` (`Member_Memno`);

--
-- Indexes for table `contributions`
--
ALTER TABLE `contributions`
  ADD PRIMARY KEY (`memno`);

--
-- Indexes for table `loanapplication`
--
ALTER TABLE `loanapplication`
  ADD PRIMARY KEY (`Loan_id`);

--
-- Indexes for table `loanprocessing`
--
ALTER TABLE `loanprocessing`
  ADD PRIMARY KEY (`id`,`LoanType_id`),
  ADD KEY `fk_LoanProcessing_LoanType1_idx` (`LoanType_id`);

--
-- Indexes for table `loanrepayment`
--
ALTER TABLE `loanrepayment`
  ADD PRIMARY KEY (`id`,`LoanType_id`,`LoanType_LoanApplication_Loan_id`),
  ADD KEY `fk_LoanRepayment_LoanType1_idx` (`LoanType_id`,`LoanType_LoanApplication_Loan_id`);

--
-- Indexes for table `loantype`
--
ALTER TABLE `loantype`
  ADD PRIMARY KEY (`id`,`LoanApplication_Loan_id`),
  ADD KEY `fk_LoanType_LoanApplication1_idx` (`LoanApplication_Loan_id`);

--
-- Indexes for table `management`
--
ALTER TABLE `management`
  ADD PRIMARY KEY (`Official_no`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`Memno`);

--
-- Indexes for table `member_has_contributions`
--
ALTER TABLE `member_has_contributions`
  ADD PRIMARY KEY (`Member_Memno`,`Contributions_memno`),
  ADD KEY `fk_Member_has_Contributions_Contributions1_idx` (`Contributions_memno`),
  ADD KEY `fk_Member_has_Contributions_Member_idx` (`Member_Memno`);

--
-- Indexes for table `organization`
--
ALTER TABLE `organization`
  ADD PRIMARY KEY (`No`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `beneficiaries`
--
ALTER TABLE `beneficiaries`
  ADD CONSTRAINT `fk_Beneficiaries_Member1` FOREIGN KEY (`Member_Memno`) REFERENCES `member` (`Memno`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `loanprocessing`
--
ALTER TABLE `loanprocessing`
  ADD CONSTRAINT `fk_LoanProcessing_LoanType1` FOREIGN KEY (`LoanType_id`) REFERENCES `loantype` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `loanrepayment`
--
ALTER TABLE `loanrepayment`
  ADD CONSTRAINT `fk_LoanRepayment_LoanType1` FOREIGN KEY (`LoanType_id`,`LoanType_LoanApplication_Loan_id`) REFERENCES `loantype` (`id`, `LoanApplication_Loan_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `loantype`
--
ALTER TABLE `loantype`
  ADD CONSTRAINT `fk_LoanType_LoanApplication1` FOREIGN KEY (`LoanApplication_Loan_id`) REFERENCES `loanapplication` (`Loan_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `member_has_contributions`
--
ALTER TABLE `member_has_contributions`
  ADD CONSTRAINT `fk_Member_has_Contributions_Contributions1` FOREIGN KEY (`Contributions_memno`) REFERENCES `contributions` (`memno`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Member_has_Contributions_Member` FOREIGN KEY (`Member_Memno`) REFERENCES `member` (`Memno`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
