

function CheckCode(code) {
  var results = 0;

  //Convert integer to string
  code = code.toString();

  //Evaluate last digit of card number
  var lastdigit = code[code.length-1];
  lastdigit = parseInt(lastdigit)

  //Evaluate card number without last digit
  code = code.slice(0, -1);

  for (var x = 1; x <= code.length; x++) {

    if (x % 2 == 1) {
      results += parseInt(code[x-1] * 1);

    } else {
      results += parseInt(code[x-1] * 3);
    }
  }


  //calculate 10-remainder = 'finalCheck'
  var remainder = results % 10;
  var finalCheck = 10 - remainder;


  //Print 'True' or 'False'
  if (finalCheck == lastdigit) {
    console.log('True')
  } else {
    console.log('False')
  }
}


//Run the code
CheckCode(2210528857729);
