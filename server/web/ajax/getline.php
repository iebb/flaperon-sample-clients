<?
	include '../db.inc.php';
	include '../functions.php';
	header('Content-Type: application/json');
	$room=(int)g('r');
	$a=(int)g('a');
	$content=addslashes(g('c'));
	$sql = "SELECT * FROM console WHERE (`id`=$room)" ;
	$result = mysql_query($sql);
	if ($row = mysql_fetch_array($result))
	echo $row['text'];
?>