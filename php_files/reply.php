<?php

require 'vendor/autoload.php';
use Abraham\TwitterOAuth\TwitterOAuth;

define('CONSUMER_KEY', 'bCxG7qQNMx2NAnHFbIQrnBNWA');
define('CONSUMER_SECRET', '6C73JOkn7FaXcWGKHpsQdJmTiCmplOyZybsq7Am7BINShFH9CO');
define('ACCESS_TOKEN', '1337389163360866309-SrRo24ETqqD9MZ0N2YGiLwe7nsfeXq');
define('ACCESS_TOKEN_SECRET', '7YR6j2X7TCiUSe0B61DNboI0Xyab1Rt41plPVHJWbgdf1');

$connection = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET);
$content = $connection->get("account/verify_credentials");
$qtweet = $_REQUEST['reply'];
$tweetid = $_REQUEST['tweet_id'];
$connection->post('statuses/update', array('status' => $qtweet, 'in_reply_to_status_id' => $tweetid,'auto_populate_reply_metadata'=>'true'));
var_dump($connection->getLastHttpCode());
?>