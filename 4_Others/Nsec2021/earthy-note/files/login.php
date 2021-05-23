<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	if (isset($_POST['token'])) {
		// no need to verify the token, 16 bytes cannot be bruteforced or guessed
		$_SESSION['token'] = $_POST['token'];
		$_SESSION['loggedin'] = True;
		header('Location: ./');
		die();
	}
}

?>
