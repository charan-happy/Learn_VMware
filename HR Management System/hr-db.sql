Drop TABLE IF EXISTS `departments`;

CREATE TABLE `departments`(
    `departmentcode` varchar(10) NOT NULL,
    `city` varchar(50) NOT NULL,
    `departmentname` varchar(50) NOT NULL,
    PRIMARY KEY (`departmentcode`)
);

DROP TABLE IF EXISTS `employees`;
CREATE TABLE `employees` (
  `employeeNumber` int(11) NOT NULL,
  `lastName` varchar(50) NOT NULL,
  `firstName` varchar(50) NOT NULL,
  `departmentCode` varchar(10) NOT NULL,
  `JobTitle` varchar(50) NOT NULL,
  `salary` int(8) NOT NULL,
  PRIMARY KEY (`employeeNumber`),
  KEY `departmentCode` (`departmentCode`);
  CONSTRAINT `employee_ibfk_2` FOREIGN KEY (`departmentCode`) REFERENCES `departments`(`departmentCode`)
  );