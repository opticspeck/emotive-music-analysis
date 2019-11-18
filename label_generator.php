<?php
// this was written by reddit user CodeGuy1322 in help for my project. thanks again!
$hl = file(dirname(__FILE__) . '/have.txt');

$have = array();

foreach ($hl as $idx => $l) {
$t = explode(' ', str_replace('@attribute     ', '', $l));

$have[] = $t[0];
}

$out = [];
$arr = json_decode(file_get_contents(dirname(__FILE__) . '/test.json'), true);

function enum_arr($arr, $have, $prefix = null, $depth = 0) {
global $out;
$sep = '.';

foreach ($arr as $k => $v) {
if (is_array($v)) {
enum_arr($v, $have, (!empty($prefix) ? $prefix . $sep : '') . $k, ($depth+1));
} else {
$key = (!empty($prefix) ? $prefix . $sep : '') . $k;

//if (!in_array($key, $have)) {
if (is_numeric($v)) {
if (!isset($_GET['opl'])) {
$out[$key] = $v;
} else {
echo $key . '<br>';
}
//echo (!empty($prefix) ? $prefix . $sep : '') . $k . '<br>';
}

}
}
}

enum_arr($arr, $have);

echo json_encode($out);
?>