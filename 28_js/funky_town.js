var gcd = function (a,b) {


  // this means the previous modulo was 0, so a divided into b
  if (b == 0) {
    return a
  }

  // finds the smallest interval between the two numbers,
  // if that interval fully divides into b, that is the gcd
  else {
    return gcd(b, a % b)
  }
}
