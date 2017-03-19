
<?php	
	session_save_path('sess');
	session_start();
	header('Content-Type: application/json');
	$reply=array();

	$dbconn = pg_connect("host=localhost dbname=UTORID user=UTORID password=PASSWORD") or die('Could not connect: ' . pg_last_error());

	global $dbconn;
	
	$user = $_REQUEST['user'];
	$pass = md5($_REQUEST['pass']);
	$query = "select * from twocuser where username = '$user';";
	$result = pg_query($dbconn, $query);
	if (pg_num_rows($result) > 0) {
		$row = pg_fetch_row($result);
		if ($pass === $row[1]) {
			$reply['user']=$row[0];
			$reply['picture']=$row[2];
			$reply['login']='true';
			$_SESSION['logged']=$row[0];
			$_SESSION['loggedpic']=$row[2];
		} else {
			$reply['login']='false';
			$reply['error']='wrong password';
		}
	} else {
		$reply['login']='false';
		$reply['error']='user not found';
	}
	pg_close($dbconn);	
	
	print json_encode($reply);
	
?>


