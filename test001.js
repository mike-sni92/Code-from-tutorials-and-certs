//** _test ** test code in IDE

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
  // _test add an array onto js obj
  const myDog = {
  "name": "Happy Coder",
  "legs": 4,
  "tails": 1,
  "friends": ["freeCodeCamp Campers"]
};

myDog.bark = "bork";
  
  //  *******************************************************
  
  var processed = 0;

function processArg(num) {
  
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
  

  //*******************************************************
    
  function caseInSwitch(val) {
  let answer = "";
    
  switch (val) {
  case 1:
  answer = "alpha";
  break;
  case 2:
  answer = "beta";
  break;
  case 3:
  answer = "gamma";
  break;
  case 4:
  answer = "delta";
  break;
  }

  // Only change code above this line
  return answer;
}

caseInSwitch(1);
  return (num + 3) / 5;
}

processed = processArg(7);
  //processed should be equal to 2.
  
  //*******************************************************
  

  // NEED TO TEST IN IDE  _test
function abTest(a, b) {


  if (a < 0 || b < 0) return undefined;

/*
abTest(2, 2) should return a number
Passed:abTest(2, 2) should return 8
Passed:abTest(-2, 2) should return undefined
Passed:abTest(2, -2) should return undefined
Passed:abTest(2, 8) should return 18
Passed:abTest(3, 3) should return 12
Passed:abTest(0, 0) should return 0
*/

  return Math.round(Math.pow(Math.sqrt(a) + Math.sqrt(b), 2));
}

abTest(2,2);
  
    //*******************************************************
// _to review
  // combination of usage of if/else and switch =  https://github.com/EQuimper/CodeChallenge/blob/master/javascript/FreeCodeCamps/Basic%20JavaScript/Counting%20Cards.md
  
  var count = 0;

function cc(card) {
  // Only change code below this line

  var msg = '';

  switch (card) {
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
      count++;
      break;
    case 7:
    case 8:
    case 9:
      count = count;
      break;
    case 10:
    case "J":
    case "Q":
    case "K":
    case "A":
      count--;
      break;
  }

  if (count === 5) msg = "5 Bet";
  else if (count === 0) msg = "0 Hold";
  else if (count === -5) msg = "-5 Hold";
  else if (count === -1) msg = "-1 Hold";
  else if (count === 1) msg = "1 Bet";


  return msg;
  // Only change code above this line
}

// Add/remove calls to test your function.
// Note: Only the last will display
cc(2); cc(3); cc(7); cc('K'); cc('A');
  
      //*******************************************************

  //JS Objects
  const myDog = {

name: "Fido",
legs: 4,
tails: 3,
friends: ["Phelix", "Doug", "Scooby"]
    
    //*******************************************************
    // dot notation & Accessing Object Properties with Variables
    
    const testObj = {
  "hat": "ballcap",
  "shirt": "jersey",
  "shoes": "cleats"
};

const hatValue = testObj.hat;      // Change this line
const shirtValue = testObj.shirt;    // Change this line
//hatvalue will return "ballcap" / shirtvalue will return "jersey"
  

const testObj = {
  12: "Namath",
  16: "Montana",
  19: "Unitas"
};

const playerNumber = 16;  
const player = testObj[playerNumber]

/* conditions playerNumber should be a number
Passed:The variable player should be a string
Passed:The value of player should be the string Montana
Passed:You should use bracket notation to access testObj
Passed:You should not assign the value Montana to the variable player directly.
Passed:You should be using the variable playerNumber in your bracket notation
*/

  //*******************************************************
