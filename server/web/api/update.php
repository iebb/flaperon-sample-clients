<?
	include '../db.inc.php';
	include '../functions.php';
	$r = (int)g('r');
	$line = mysql_escape_string(g('c'));
	echo $sql = "REPLACE INTO console VALUES ($r,'$line')";
	$result = mysql_query($sql);
?>