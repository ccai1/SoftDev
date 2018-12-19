// Indigo Ink
// Cathy Cai, Sophia Xia
// SoftDev1 pd6
// K28 -- Sequential Progression
// 2018-12-28

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
