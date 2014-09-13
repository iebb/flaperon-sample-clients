<?
	
	function g($s,$de=0){
		if (isset($_GET[$s])) return $_GET[$s];
		if (isset($_POST[$s])) return $_POST[$s];
		return $de;
	}

?>