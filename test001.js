const myNoun = "dog";
const myAdjective = "big";
const myVerb = "ran";
const myAdverb = "quickly";

const wordBlanks ="this noun " + myNoun + "followed by my verb " + myVerb + "then my adjective" + myAdjective + "and my adverb " + myAdverb + "." ;

function wordBlanks(myNoun, myAdjective, myVerb, myAdverb) {
  var result = "";
  
  
const myArray = [["John", 23], ["cat", 2]];
  myArray.push(["dog", 3]) ;
  
  
  const myArray = [["John", 23], ["cat", 2]];

// Only change code below this line
var removedFromMyArray = myArray.pop();
myArray.pop[1] ;

  
  // Setup Manipulate Arrays With shift()
const myArray = [["John", 23], ["dog", 3]];

// Only change code below this line
myArray.shift[0];
const removedFromMyArray = myArray.shift(1);

  
//  *******************************************************
  
  var processed = 0;

function processArg(num) {
  return (num + 3) / 5;
}

processed = processArg(7);
  //processed should be equal to 2.
  
  //*******************************************************
    
    //Untested
    
    function nextInLine(arr, item) {
  // Only change code below this line
      arr.push(item);
    return arr.shift();
  return item;
  // Only change code above this line
}

// Setup
let testArr = [1, 2, 3, 4, 5];

// Display code
console.log("Before: " + JSON.stringify(testArr));
console.log(nextInLine(testArr, 6));
console.log("After: " + JSON.stringify(testArr));
  
    //*******************************************************
      
      
      function orderMyLogic(val) {
  if (val < 10) {
    return "Less than 10";
  } else if (val < 5) {
    return "Less than 5";
  } else {
    return "Greater than or equal to 10";
  }
}
  
  //correct line to fulfill request below
  
  function orderMyLogic(val) {
  if (val < 5) {
    return "Less than 5";
  } else if (val < 10) {
    return "Less than 10";
  } else {
    return "Greater than or equal to 10";
  }
}

orderMyLogic(7);

orderMyLogic(7);
  orderMyLogic(4);
  orderMyLogic(6);
  orderMyLogic(11);
  
  //*******************************************************
    
    //Chained else if statement
    
    function testSize(num) {

  if (num < 5) {
    return "Tiny";
  } 
  else if (num < 9) {
    return "Small";
  } 
  else if (num < 15) {
    return "Medium";
  }
  else if (num < 19) {
    return "Large";
  }
  else {
    return "Huge";
  }
}
/*
testSize(0) should return the string Tiny
Passed:testSize(4) should return the string Tiny
Passed:testSize(5) should return the string Small
Passed:testSize(8) should return the string Small
Passed:testSize(10) should return the string Medium
Passed:testSize(14) should return the string Medium
Passed:testSize(15) should return the string Large
Passed:testSize(17) should return the string Large
Passed:testSize(20) should return the string Huge
Passed:testSize(25)
*/
  
  
  //*******************************************************
    //how does this work? is "===" absolutely necessary? why the minus sign in between strokes and par??
    // https://github.com/EQuimper/CodeChallenge/blob/master/javascript/FreeCodeCamps/Basic%20JavaScript/Golf%20Code.md
  function golfScore(par, strokes) {

  if (strokes === 1) return "Hole-in-one!";

  else if ((strokes - par) <= -2) return 'Eagle';

  else if ((strokes - par) === -1) return 'Birdie';

  else if (strokes === par) return 'Par';

  else if ((strokes - par) === 1) return 'Bogey';

  else if ((strokes - par) === 2) return 'Double Bogey';

  else return 'Go Home!';

}

// Change these values to test
golfScore(5, 1);
  
