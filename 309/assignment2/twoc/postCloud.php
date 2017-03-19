<?php	
	session_save_path('sess');
	session_start();
	header('Content-Type: application/json');

	$dbconn = pg_connect("host=localhost dbname=UTORID user=UTORID password=PASSWORD") or die('Could not connect: ' . pg_last_error());
	$reply=array();
	
	global $dbconn;
	
	$content = $_REQUEST['html'];
	$user = $_SESSION['logged'];
	$picture = $_SESSION['loggedpic'];
	
	$query = "insert into post (username, picture, content, likes) values ('$user', '$picture', '$content', 0);";
	$result = pg_query($dbconn, $query);
	if (pg_affected_rows($result)>0) {
		$reply['created']='true';
	} else {
		$reply['created']='false';
		$reply['error']=pg_last_error();
	}
	
	pg_close($dbconn);

	print json_encode($reply);
	
?>
