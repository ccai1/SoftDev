//Indigo Ink
//Cathy Cai, Sophia Xia
//SoftDev1 pd6
//K28 -- Sequential Progression
//2018-12-28

var fibb = function(n){

    // base case 0
    if(n == 0){
	     return 0;
    }

    // base case 1
    else if (n == 1){
	     return 1;
    }

    // add prev two
    else{
	     return fibb(n -1) + fibb(n -2);
    }

};

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

var stulist = ["james", "tyler", "lauren", "becky", "oliver", "frank"];

var randstu = function(){

    // random num in range
    var num = Math.floor(Math.random() * stulist.length);

    // index that
    return stulist[num];
}

var fibbut = document.getElementById("fib");
var gcdbut = document.getElementById("gcd");
var randbut = document.getElementById("rand");

var fibdis = function() {
  console.log(fibb(7));
  console.log(fibb(6));
  document.getElementById("p0").innerHTML = fibb(7);
  // document.getElementById("p0").innerHTML = fibb(6);
};

var gcddis = function() {
  console.log(gcd(5, 25));
  console.log(gcd(21, 14));
  document.getElementById("p1").innerHTML = gcd(5, 25);
  // document.getElementById("p1").innerHTML = gcd(21, 14);
};

var randdis = function() {
  console.log(randstu());
  console.log(randstu());
  document.getElementById("p2").innerHTML = randstu();
  // document.getElementById("p2").innerHTML = randstu();
};


fibbut.addEventListener('click', fibdis)
gcdbut.addEventListener('click', gcddis)
randbut.addEventListener('click', randdis)
