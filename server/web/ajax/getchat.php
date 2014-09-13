<?
	include '../db.inc.php';
	include '../functions.php';
	header('Content-Type: application/json');
	$room=(int)g('r');
	$a=(int)g('a');
	$content=addslashes(g('c'));
	$sql = "SELECT * FROM chat WHERE (`rid`=$room) AND (`time`>$a) ORDER BY time ASC" ;
	$result = mysql_query($sql);
	$content=array();
	for($i=0;$i<50;$i++){
		if (!($row = mysql_fetch_array($result))) break;
		$content[$row['id']]='<dl id="chatline_'.$row['id'].'"><dt><span class="icon icon--info fa fa-user"></span><span class="name clickable">'.$row['user'].'</span><time>'.date('H:i:s',$row['time']).'</time></dt><dd>'.htmlspecialchars($row['content']).'</dd></dl>';
	}
	echo json_encode(array(count($content),$content));
?>