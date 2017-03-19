
<?php
session_save_path('sess');
session_start();

if (!isset($_SESSION['logged'])) {
	header("location: index.html");
}

?>

<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title> twoc home </title>
	<link rel="stylesheet" type="text/css" href="homestyle.css">
	<script src="jquery-2.1.0.js"></script>
	<script>
	
	var common = ["", "https:...", "http:...", "logo...", "your", "us", "what", "with", "this", "but", "if", "you're", "it", "be", "so", "was", "me", "is", "from", "by", "-", "when", "you", "an", "on", "is", "up", "are", "in", "a", "at", "i", "my", "how", "as", "****count", "to", "of", "the", "and", "or", "rt", "for"];
	var counter = {};
	
	function createCloud(keyword) {
	$.getJSON("retrieveTweets.php", {keyword: keyword}, function(data) {
		if (data['fail']=='true') {
			$('#debug').html("failed");
		} else {
			$('#cloud').append("<p>");
			$.each(data, function(word, count) {
				if ($.inArray(word.toLowerCase(), common) == -1 && count>5) {
					if (word.indexOf("'") === -1) {
						var built = "";
						built += "<span style='font-size:";
						if (count < 10) {
							built += 20;
						} else if (count < 20) {
							built += 28;
						} else if (count < 30) {
							built += 36;
						} else if (count < 45) {
							built += 42;
						} else if (count < 60) {
							built += 48;
						} else {
							built += 60;
						}
						built += "px;'>";	
						built += word;			
						built += "</span>   "; 
						$('#cloud').append(built);
					}
				}	
			});
			$('#cloud').append("</p>");
			$('#cloud').show();
			$('#sharebutt').show();
		}
	
	});
		
	
	}
	
	function getTimeline() {
		$('#timeline').html("");
		$.getJSON("retrieveTimeline.php", {}, function(data) {
			$.each(data, function(postid, prebuilt) {
				var pb = "";
				pb += "<div class=post>";
				pb += prebuilt;
				pb += "<button type=\"button\" id=\"" + postid + "\">Like</button>";
				pb += "</div>";
				$('#timeline').append(pb);
				$('#' + postid).on('click', function() {
					var id = $(this).attr('id');
					likePost(id);
				});
			});
		});
	}
	
	function likePost(postid) {
		$.getJSON("likePost.php", {id: postid}, function(data) {
			getTimeline();	
		});
	}
	
	function postToTimeline(html) {
		if ($('#cloud').html()=="" || $('#cloud').html()=="<p></p><p></p>") {
			alert("Nothing to share!");
			return false;
		}
		$.getJSON("postCloud.php", {html: html}, function(data) {
			if (data['created']=='true') {
				$('#errorDisplay').html("");
				$('#cloud').hide();
				$('#sharebutt').hide();
				$('#cloud').html("");
				getTimeline();
			} else {
				$('#errorDisplay').html("failed to post! <br>");
				var why = data['error'];
				$('#errorDisplay').append(why);
			}
		}); 
	}
	
	$(function() {
	
		$('#createbutt').on('click', function() {
			$('#cloud').html("");
			var key = $('#key').val();
			createCloud(key);
		});
		
		$('#sharebutt').on('click', function() {
			var content = $('#cloud').html();
			postToTimeline(content);
		});
		
		$('#new').keydown(function(event) {
			if(event.keyCode == 13) {
				event.preventDefault();
				$('#createbutt').click();
			}
		});
		
		getTimeline();
	
	});	
	
	</script>
</head>

<body>

<div id="top">
<?php
echo ("<img src='");
echo ($_SESSION['loggedpic']);
echo ("'></img><br>");
echo ("Hello, ");
echo ($_SESSION['logged']);
echo ("<br>");
?>
<a href="index.html">Log out</a>
</div>

<h2>Latest posts:</h2>

<div id="timeline">
</div>

<div id="new">
<form>
Enter a keyword to create a word cloud: <br> 
<input type="text" id="key" />
<button type="button" id="createbutt">Create</button>
</form>
<div id="cloud"></div>
<button type="button" id="sharebutt">Share it!</button>
<div id="errorDisplay"></div>
</div>


</body>
</html>
