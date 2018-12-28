var i = 0;

function Transform() {

  let numrows = document.getElementsByTagName('tr');

  if (i % 2 == 1) {
    var numrowschanged = 0;

    //For Loop to change color to grey
    for (x = 0; x < numrows.length; x += 2) {
      numrows[x].style.backgroundColor = 'grey';
      numrowschanged += 1;
    }

    //Print number of rows changed
    document.getElementById('textarea').innerHTML = 'Number of rows changed: ' + numrowschanged;

    //Adds $ in front of textbox
    document.getElementById('dollar-value').placeholder = '$##,###.##';

    //Adds index of the lowest value in an array
    var array = [1, 6, 4, 1, 9, 10, 11, 123];
    var min = array.indexOf(Math.min(...array));
    document.getElementById('textarea').innerHTML += '<br><br>The minimum value is: ' + min

  }
  else {
    //For Loop to clear changes
    for (x = 0; x < numrows.length; x++){
      numrows[x].style.backgroundColor = 'initial';
    }
    document.getElementById('textarea').innerHTML = '';

    //Clears the $ in front of textbox
    document.getElementById('dollar-value').value = '';
  }
}


//Adds $ onclick of textbox
function DollarSign() {
  document.getElementById('dollar-value').value = '$';
  document.getElementById('textarea')
}






// print: document.getElementById("demo").innerHTML = 5 + 6;
