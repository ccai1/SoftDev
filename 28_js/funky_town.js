// Indigo Ink
// Cathy Cai, Sophia Xia
// SoftDev1 pd6
// K28 -- Sequential Progression
// 2018-12-28

var gcd = function (a,b) {


  // this means the previous modulo (a % b) was 0, so b divided into a
  if (b == 0) {
    return a
  }

  // finds the smallest interval between the two numbers,
  // passes in the smaller of a and b with the interval
  else {
    return gcd(b, a % b)
  }
}
