function checkIfPrime(value){
  if (value<0){return false;}
  for (var i = 2;i<=Math.sqrt(value);i++){
    if (value%i === 0){
      return false;
    }
  }
  return true;
}
var largestPrimeCount = 0;
var largest_a = 0;
var largest_b = 0;
for (var a = -999; a < 1000;a++){
  for (var b = -999; b< 1000;b++){
    var primeCount = 0;
    var n = 0;
    while(checkIfPrime(n*n + a*n + b)){
      n++;
    }
    if (n>largestPrimeCount){
      largestPrimeCount =n;
      largest_a = a;
      largest_b = b;
    }
  }

}

console.log("a: " + largest_a);
console.log("b: " + largest_b);
console.log("number of primes: " + largestPrimeCount);
console.log("a x b: " + largest_a * largest_b);
