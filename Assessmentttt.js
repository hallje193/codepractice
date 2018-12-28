
function Transform() {

  let numcols = document.getElementsByTagName('td');

  var numcolschanged = 0;

  //For Loop to change color to grey
  for (x = 1; x < numcols.length; x += 2) {
      numcols[x].style.backgroundColor = 'grey';
      numcolschanged += 1;
  }

  //Print number of rows changed
  console.log('Number of columns changed: ' + numcolschanged);

  //Adds $ in front of textbox    document.getElementById('dollar-value').placeholder = '$##,###.##';

  //Adds index of the lowest value in an array
  //var array = [1, 6, 4, 1, 9, 10, 11, 123];
  //var min = array.indexOf(Math.min(...array));
  //document.getElementById('textarea').innerHTML += '<br><br>The minimum value is: ' + min



}


//Adds $ onclick of textbox
//function DollarSign() {
//  document.getElementById('dollar-value').value = '$';
//  document.getElementById('textarea')
//}






// print: document.getElementById("demo").innerHTML = 5 + 6;
