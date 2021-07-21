<?php
/*
The reverse of XOR is XOR!
5^3 = 6
6^3 = 5
*/
function xor_encrypt($in, $key) {
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}


$defaultData = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$hackedData =  array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$defaultDataJson = json_encode($defaultData);
$hackedDataJson = json_encode($hackedData);

$defaultDataB64EncryptedJson = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
//default cookie is base64 encoded and xor encrypted

$defaultDataEncryptedJson = base64_decode($defaultDataB64EncryptedJson);
// key ^ defaultDataEncrypted = defaultDataJson
// key = defaultDataJson ^ defaultDataEncrypted

$key = xor_encrypt($defaultDataJson, $defaultDataEncryptedJson);
// echo $key; //qw8J is the key
$hackedDataEncryptedJson = xor_encrypt($hackedDataJson, "qw8J");
$hackedDataB64EncryptedJson = base64_encode($hackedDataEncryptedJson);
echo $hackedDataB64EncryptedJson;
?>
