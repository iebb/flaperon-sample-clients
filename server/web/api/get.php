<?
	include '../db.inc.php';
	include '../functions.php';
	header('Content-Type: application/json');
	$server = g('server');
	$status = g('status',-1);
	$modify = g('modify');
	$order = g('order',1)?"ASC":"DESC";
	$sql = "SELECT * FROM commands WHERE (server = $server) AND (status <= $status) AND (remain>0) ORDER BY time $order ";
	$result = mysql_query($sql);
	$row = mysql_fetch_object($result);
	echo json_encode($row);
?>