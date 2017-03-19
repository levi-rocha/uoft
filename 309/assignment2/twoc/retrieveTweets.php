<?php

session_save_path('sess');
session_start();
header('Content-Type: application/json');

$counter=array();
$status=array();

ini_set('display_errors', 1);
require_once('TwitterAPIExchange.php');

$settings = array(
	'oauth_access_token' => "3957662427-9KBDRi9T6d56P80RoQG7JRbZDDgs2aTHTHvqwK0",
    'oauth_access_token_secret' => "vnfekl3cPweAtrLRZmk6IUqdShMw1s9wQ6qyDTEJOeAHy",
    'consumer_key' => "GN01JQPNOnjM7t48bWxPbv0mZ",
    'consumer_secret' => "baxYklJN6E2gAnbZZacgglmx6YbhqLlGpVBsAOmNSHnOSgkUeB"
);

$url = 'https://api.twitter.com/1.1/search/tweets.json';
$keyword = $_REQUEST['keyword'];
$getfield = '?q=' . $keyword . '&count=100&lang=en';
$requestMethod = 'GET';

$twitter = new TwitterAPIExchange($settings);
$result = $twitter->setGetfield($getfield)
             ->buildOauth($url, $requestMethod)
			 ->performRequest();

$jr = json_decode($result, true);

$count = 0;

foreach ($jr['statuses'] as $key=>$value) {
	$count++;
	$status[$count] = $value['text'];
}

$counter['****COUNT']=$count;

for ($i=1;$i<=$count;$i++) {
	$words = explode(" ", $status[$i]);
	$size = sizeof($words);
	
	for ($j=0;$j<=$size;$j++) {
		if (isset($words[$j])) {
			$word = strtolower($words[$j]);
			if (isset($counter[$word])) {
				$counter[$word]++;	
			} else {
				$counter[$word] = 1;	
			}
		}
	}
	
}

print json_encode($counter);

?>
