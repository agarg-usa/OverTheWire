<?php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

$decodedSecret = base64_decode(strrev(hex2bin($encodedSecret)));

echo $decodedSecret;
echo "<br>";
echo encodeSecret($decodedSecret)
?>