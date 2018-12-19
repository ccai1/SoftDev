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
