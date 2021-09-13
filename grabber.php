<?php
/*
The "send to" page for ScreenView.

@author: The Ultimate War Machine
*/
$input = file_get_contents("php://input");
file_put_contents("screenshot.txt",$input);
?>