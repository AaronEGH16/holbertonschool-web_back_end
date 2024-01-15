export default function concatArrays(array1, array2, string) {
  var array3 = Array.from(string);
  return array1.concat(array2, array3);
}
