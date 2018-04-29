<?php
      require "vendor/autoload.php";
    $db = new MysqliDb ('hackdb.cowzyzuil4nn.us-east-2.rds.amazonaws.com', 'root', 'rootroot', 'Galactik');

      $players = $db->get ("players");
      
      //Set the Content Type

function generatePlayerImg($player)
{
      $name =($player["player_name"]);
      $atk = ($player["player_attack"]);
      $deff = ($player["player_deffence"]);
      $stm = ($player["player_stamina"]);
      $ovl = ($player["player_overall"]);
      
  
      // Create Image From Existing File
      $jpg_image = imagecreatefrompng('/home/ubuntu/Galactik/StorePhpScripts/Races/'.$player['player_race'].'Player.png');

      // Allocate A Color For The Text
      $white = imagecolorallocate($jpg_image, 255, 255, 255);

      // Set Path to Font File
      $font_path = '/home/ubuntu/Galactik/StorePhpScripts/eu.ttf';

      // Set Text to Be Printed On Image
      

      // Print Text On Image
      imagettftext($jpg_image, 25, 0, 80, 740, $white, $font_path, $name);
      imagettftext($jpg_image, 25, 0, 138, 785, $white, $font_path, $ovl);
      imagettftext($jpg_image, 25, 0, 138, 817, $white, $font_path, $stm);
      imagettftext($jpg_image, 25, 0, 138, 849, $white, $font_path, $atk);
      imagettftext($jpg_image, 25, 0, 138, 881, $white, $font_path, $deff);

      // Send Image to Browser
      imagepng($jpg_image, 'outputs/player_'.$player['player_id'].'.png');

      // Clear Memory
      imagedestroy($jpg_image);
    }


foreach($players as $player)
generatePlayerImg($player);
