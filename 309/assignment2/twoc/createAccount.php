<?php
	session_save_path('sess');
	session_start();
?>

<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title> create account </title>
</head>

<body>

<?php

if ($_FILES['file']['size']==0) {
	$dbconn = pg_connect("host=localhost dbname=UTORID user=UTORID password=PASSWORD") or die('Could not connect: ' . pg_last_error());	
	$username = $_REQUEST['login'];
	echo ($_REQUEST['pass']);
	echo ("<br>");
	$password = md5($_REQUEST['pass']);
	echo ($password);
	global $dbconn;
	$query = "insert into twocuser values ('$username','$password','img/me.jpg');";
	$result = pg_query($dbconn, $query);
	if (pg_affected_rows($result)>0) {
		$_SESSION['logged']=$username;
		$_SESSION['loggedpic']='img/me.jpg';
		header("location: home.php");
	} else {
		echo("Could not create account.");
	}
	pg_close($dbconn);
} else {

$target = "img/" . basename($_FILES['file']['name']);

$valid = array('jpg', 'jpeg');
$temp = explode(".", $_FILES['file']['name']);
$extension = end($temp);

if(
	($_FILES['file']['type'] == "image/jpg" || $_FILES['file']['type'] == "image/jpeg") &&
	(in_array($extension,$valid)) &&
	($_FILES['file']['size']<52000)
) {
	if ($_FILES['file']['error'] > 0) {
		echo ($_FILES['file']['error']);
		echo ("<a href='signup.html'>Back to sign-up page</a>");
	} else {
		move_uploaded_file($_FILES['file']['tmp_name'], $target);
		chmod ($target,644);
		$dbconn = pg_connect("host=localhost dbname=UTORID user=UTORID password=PASSWORD") or die('Could not connect: ' . pg_last_error());	
		$username = $_REQUEST['login'];
		$password = md5($_REQUEST['pass']);
		global $dbconn;
		$query = "insert into twocuser values ('$username','$password','$target');";
		$result = pg_query($dbconn, $query);
		if (pg_affected_rows($result)>0) {
			$_SESSION['logged']=$username;
			$_SESSION['loggedpic']=$target;
			header("location: home.php");
		} else {
			echo("Could not create account.");
		}
		pg_close($dbconn);
	}
} else {
	echo ("Could not upload the file. Please check file type and size. <br>");
	echo ("<a href='signup.html'>Back to sign-up page</a>");
}
}
?>

</body>
</html>
