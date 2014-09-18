<?
	include '../db.inc.php';
	include '../functions.php';
	header('Content-Type: application/json');
	$server = g('server');
	$command = g('command');
	$interval = g('interval');
	$repeat = g('repeat',1);
	$ts=mktime();
	echo $sql = "INSERT INTO commands VALUES(0,$server,$ts,'$command',-1,$interval,$repeat,0)";
	$result = mysql_query($sql);
	echo json_encode($row);
?>