<?
	include '../db.inc.php';
	include '../functions.php';
	header('Content-Type: application/json');
	$room=(int)g('r');
	$a=(int)g('a');
	$time=mktime();
	$user=$_SERVER["REMOTE_ADDR"];
	$content=addslashes(g('c'));
	$sql = "INSERT INTO chat VALUES(0,$room,$time,'$user','$content') ";
	$result = mysql_query($sql);
	$sql = "SELECT * FROM chat WHERE (rid=$room) AND (time>$a) ORDER BY time DESC" ;
	$result = mysql_query($sql);
	$content=array();
	for($i=0;$i<50;$i++){
		if (!($row = mysql_fetch_array($result))) break;
		$content[$row['id']]='<dl id="chatline_'.$row['id'].'"><dt><span class="icon icon--info fa fa-user"></span><span class="name clickable">'.$row['user'].'</span><time>'.date('H:i:s',$row['time']).'</time></dt><dd>'.htmlspecialchars($row['content']).'</dd></dl>';
	}
	echo json_encode(array(count($content),$content));
?>