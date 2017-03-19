<?php	
	session_save_path('sess');
	session_start();
	header('Content-Type: application/json');

	$dbconn = pg_connect("host=localhost dbname=UTORID user=UTORID password=PASSWORD") or die('Could not connect: ' . pg_last_error());
	$reply=array();
	
	global $dbconn;
	
	$query = "select * from post order by timestamp desc limit 12";
	$result = pg_query($dbconn, $query);
	$numrows = pg_numrows($result);
	
	for ($i = 0; $i < $numrows; $i++) {
		$html = "<span id=";
		$row = pg_fetch_array($result, $i);
		$html .= "'post";
		$html .= $row['id'];
		$html .= "'>";
		$html .= "<img src='";
		$html .= $row['picture'];
		$html .= "'></img><br>";
		$html .= $row['username']; 
		$html .= "<br> <div class='content'>";
		$html .= $row['content'];
		$html .= "</div><br>Likes: ";
		$html .= $row['likes']; 
		$html .= "</span>";
		$reply[$row['id']] = $html;
	}
	
	pg_close($dbconn);

	print json_encode($reply);
	
?>
