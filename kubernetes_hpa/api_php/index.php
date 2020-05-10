<?php 
if (isset($_GET['kolicinaMemorije'])) {
    $mem = $_GET['kolicinaMemorije'];

    $niz = str_repeat('x', $mem * 1024 * 1024);
    sleep(10);
    $niz = null;

    echo 'OK';
}
?>