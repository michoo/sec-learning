<?php
session_start();

$msg = '';
$created = False;

checkAdmin();

function checkAdmin() {
	// Auto-login if we are from localhost so that we don't have to login every time
	$local = array(
		'127.0.0.1',
		'::1',
		$_SERVER['SERVER_ADDR']
	);
	if (in_array($_SERVER['REMOTE_ADDR'], $local)) {
		$_SESSION['token'] = "sommething secret";
	}
}

//X-Forwarded-For: 127.0.0.1

if (isset($_REQUEST['note'])) {
	addNote();
}

if (isset($_GET['reportUrl'])) {
	$url = parse_url($_GET['reportUrl']);
	if ($url['host'] != $_SERVER['SERVER_NAME']) {
		$msg = 'Report Url is no good!!';
	} else {
		$msg = 'The admin will check the note, thanks!!';
		// secret code that reports to the admin
	}
	blink($msg);
}

if (isset($_GET['createAccount'])) {
	$token = bin2hex(openssl_random_pseudo_bytes(16));
	$connection = new SQLite3('/var/www/db.sql');
	$connection->enableExceptions(true);
	$stmt = $connection->prepare('INSERT INTO tokens(token) VALUES(:token)');
	$stmt->bindValue(':token', $token, SQLITE3_TEXT);
	$cursor = $stmt->execute();
	$created = True;
	$_SESSION['token'] = $token;
	$_SESSION['loggedin'] = True;
}

function filterUrl($url) {
	$patterns = array('/http:/', '/https:/', '/\/\//', '/www/');
	$arr = array('http:', 'https:', '\/\/', 'www');

	foreach($arr as &$a) {
		if (stripos($url,$a) !== false) {
			$url2 = preg_replace($patterns, '', strtolower($url));
			return filterUrl($url2);
		}
	}
	return $url;
}

function filterNote($note) {
	$blacklist = array('<', '>');
	$note = str_replace($blacklist, '', $note);
	return $note;
}

function checkNoteType($type) {
	if ($type === 'public') {
		return 'public';
	}
	return 'private';
}

function blink($msg) {
	$redir = '/';
	if (isset($_GET['redir'])) {
		$redir = filterUrl($_GET['redir']);
	}
	echo '<link rel="stylesheet" href="style.css"><center><blink><h1>' .$msg. '</h1></blink></center>';
	header('Refresh: 3; URL=' . $redir);
	die();
}

function createJSON() {
	$connection = new SQLite3('/var/www/db.sql');
	$connection->enableExceptions(true);
	$stmt = $connection->prepare('SELECT note, id FROM notes WHERE type = "public"');
	$cursor = $stmt->execute();
	$json[] = '';
	while ($row = $cursor->fetchArray(SQLITE3_ASSOC)) {
		$json[] = ['note' => 'note', 'text' => $row['note'], 'id' => $row['id']];
	}
	$json = json_encode($json);
	$file = fopen('/var/www/html/notes.json', 'w');
	fwrite($file, $json);
	fclose($file);
}

function addNote() {
	$msg = '';
	if (!isset($_SESSION['token'])) {
		$msg = 'You must be logged in to add a note!!';
	} else if (!isset($_REQUEST['note'])) {
		$msg = 'Your note cannot be empty!!';
	} else if (!isset($_REQUEST['type'])) {
		$msg = 'Your note type cannot be empty!!';
	} else {
		$note = filterNote($_REQUEST['note']);
		$type = checkNoteType($_REQUEST['type']);
		$connection = new SQLite3('/var/www/db.sql');
		$connection->enableExceptions(true);
		$stmt = $connection->prepare('INSERT INTO notes(token, note, type) VALUES(:token, :note, :type)');
		$stmt->bindValue(':token', $_SESSION['token'], SQLITE3_TEXT);
		$stmt->bindValue(':note', $note, SQLITE3_TEXT);
		$stmt->bindValue(':type', $type, SQLITE3_TEXT);
		$cursor = $stmt->execute();
		createJSON();
		$msg = 'Note added!!';
	}
	blink($msg);
}

function getPrivateNotes() {
	$connection = new SQLite3('/var/www/db.sql');
	$connection->enableExceptions(true);
	$stmt = $connection->prepare('SELECT note FROM notes WHERE token = :token AND type = "private"');
	$stmt->bindValue(':token', $_SESSION['token'], SQLITE3_TEXT);
	$cursor = $stmt->execute();
	$json[] = '';
	while ($row = $cursor->fetchArray(SQLITE3_ASSOC)) {
		$json[] = ['note' => 'note', 'text' => $row['note']];
	}
	return json_encode($json);
}
//f4b5d66cdf47417558d78e903767f1fe

?>
<html>
<head>
	<link rel="stylesheet" href="style.css">
	<title>The Earthy Note</title>
</head>
<body>
<h1><center>The Earthy Note</center></h1>

<div align="left">
	<a href="./logout.php">Log out</a>
	<br>
	<br>
</div>

<div>
	I have created this website so anyone can anymously keep and share notes. No password needed, only your token!!
	<br>
	But be aware, any offending notes will be deleted. Feel free to report any offending notes.
	<br><br>
</div>

<?php
if ($created) {
	echo '<div>Your account token (don\'t forget it!!): ' .$token. '</div><br>';
}

if (!isset($_SESSION['token'])) {
	echo '
<div>
	Please enter your token to log in and post notes.
	<form action="login.php" method="post">
		<input type="text" name="token" id="token">
		<button type="submit">Log in</button>
	</form>
	<br>
	Don\'t have an account yet? <a href="index.php?createAccount">Create one now</a><br><br>
</div>';
} else {
	echo '<div>
	<h2>Add new note</h2>
	<form action="index.php" method="post">
		<textarea id="note" name="note" rows="4" cols="50"></textarea>
		<br><br>
		Public <input type="radio" id="type" name="type" value="public">
		Private <input type="radio" id="type" name="type" value="private">
		<br><br>
		<button type="submit">Create note</button>
	</form>
</div>

<h2>Your private notes</h2>
<div id="privateNotes" name="privateNotes">
</div>';

	$notes = getPrivateNotes();
	echo '<script>
		var notes = ' .$notes. '
		    for (var i = 0; i < notes.length; i++) {
			    document.getElementById("privateNotes").innerHTML += `      
	<table>
		<tr>
			<th style="width: 10%;">Note</th>
		</tr>
		<tr>
			<td></td>
			<td>${notes[i].text}</td>
		</tr>
		<br>
	</table>
	`};
	</script>
	';
}
?>
<br>
<h2>All public notes</h2>
<div id="publicNotes" name="publicNotes">
</div>
<script>
	window.addEventListener("DOMContentLoaded", function () {
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
	  if (this.readyState == 4 && this.status == 200) {
	    var notes = JSON.parse(this.responseText);
	    console.log(JSON.parse(this.responseText));
	    for (var i = 0; i < notes.length; i++) {
		    document.getElementById("publicNotes").innerHTML += `      
<table>
	<tr>
		<th style="width: 10%;">Note</th>
	</tr>
	<tr>
		<td></td>
		<td>${notes[i].text}</td>
		<td style="text-align: right"><a href="?reportUrl=http://earthy-notes.ctf/%3fnote%3d${notes[i].id}">Report</a></td>
	</tr>
	<br>
</table>
`;
	    }
	  }
	};
	xhr.open("GET", "/notes.json", true);
	xhr.send();
	})
	</script>
</body>
</html>

