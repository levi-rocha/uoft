<?php
	session_save_path('sess');
	session_start();
	header('Content-Type: application/json');
	$reply=array();
	$dbconn = pg_connect("host=localhost dbname=UTORID user=UTORID password=PASSWORD") or die('Could not connect: ' . pg_last_error());
	$username=$_REQUEST['username'];
	global $dbconn;
	$query = "select * from twocuser where username = '$username' limit 1;";
	$result = pg_query($dbconn, $query);
	if (pg_num_rows($result) > 0) {
		$reply['available']='false';
	} else {
		$reply['available']='true';
	}
	pg_close($dbconn);	
		
	print json_encode($reply);

?>
