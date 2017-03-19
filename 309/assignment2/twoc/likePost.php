<?php	
	session_save_path('sess');
	session_start();
	header('Content-Type: application/json');

	$dbconn = pg_connect("host=localhost dbname=UTORID user=UTORID password=PASSWORD") or die('Could not connect: ' . pg_last_error());
	$reply=array();
	
	global $dbconn;
	
	$id = $_REQUEST['id'];
	
	$query = "update post set likes = likes + 1 where id = $id";
	$result = pg_query($dbconn, $query);
	if (pg_affected_rows($result)>0) {
		$reply['updated']='true';
	} else {
		$reply['updated']='false';
	}
	
	pg_close($dbconn);

	print json_encode($reply);
	
?>
