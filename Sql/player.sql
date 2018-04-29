DROP TABLE IF EXISTS `players`;
CREATE TABLE `Galactikhackball`.`players` (
  `player_id` BIGINT NULL AUTO_INCREMENT,
  `player_name` VARCHAR(45) NULL,
  `player_race` VARCHAR(20) NULL,
  `player_stamina` INT NULL,
  `player_deffence` INT NULL,
  `player_attack` INT NULL,
  `player_overall` INT NULL,
  PRIMARY KEY (`player_id`));