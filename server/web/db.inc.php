<?
	static 	$DB_HOST="localhost";
	static 	$DB_NAME="givedbnamepls";
	static 	$DB_USER="hereistheusername";
	static 	$DB_PASS="nowtypeinpassword";
	mysql_pconnect($DB_HOST,$DB_USER,$DB_PASS);
	mysql_select_db($DB_NAME);

?>