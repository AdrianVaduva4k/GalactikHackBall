DROP TABLE IF EXISTS `users`;
CREATE TABLE `Galactikhackball`.`users` (
  `user_id` BIGINT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL,
  `user_teamname` VARCHAR(45) NULL,
  `user_email` VARCHAR(45) NULL,
  `user_password` VARCHAR(55) NULL,
  PRIMARY KEY (`user_id`));