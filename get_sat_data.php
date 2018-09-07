<?php
$argv[2] = $_GET['name'];
$argv[3] = $_GET['lat'];
$argv[4] = $_GET['lon'];
$argv[5] = $_GET['ele'];
$argv[1] = $_GET['key'];

header('Content-Type: application/json');
$result = exec('/home/hamsatsp/pyephem/bin/python /home/hamsatsp/public_html/pyephem.py ' . $argv[1] . ' ' . $argv[2] . ' ' . $argv[3] . ' ' . $argv[4] . ' ' . $argv[5]);
echo $result;
$date = date('Y-m-d H:i:s');
$myfile = file_put_contents('requests.txt', $_SERVER['REMOTE_ADDR'].' ' .$date.PHP_EOL , FILE_APPEND | LOCK_EX);
?>
