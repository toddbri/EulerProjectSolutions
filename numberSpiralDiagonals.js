// this solution is based on the pattern the sum of the diagonals follow
//for a 3X3 the diagonals are 1 + 3 + 5 + 7 + 9
//for a 5X5 the diagonals are 1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25
//every additional size matrix (ie: 7x7 then 9X9) adds for more number that are the previous number + an incrementor
//the incrementor increases by 2 for each level.
//So the pattern is 1 + (4 more where the next value is the last + 2) + (4 more where the next value is the last + 4) +. repeat that pattern


var total = 0;

var spiralSize = 1001;
var counter = spiralSize*2 -1;
var incrementor = 0;
var last = 1;

for (var i=1;i<=counter;i++){
  var next = last + incrementor;
  total += next;
  last = next;
  if ((i-1)%4 ===0){
    incrementor +=2;
  }

}

console.log("diagonal total: " + total);
