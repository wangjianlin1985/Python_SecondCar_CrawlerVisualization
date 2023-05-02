
CREATE DATABASE `base_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `data_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `car_brand` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `car_series` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `car_model` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `car_purchased` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `car_mileage` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `car_price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=788 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
