var i = 0;

function Transform() {

  let numrows = document.getElementsByTagName('tr');

  if (i % 2 == 1) {
    var numrowschanged = 0;

    for (x = 0; x < numrows.length; x += 2) {
      numrows[x].style.backgroundColor = 'grey';
      numrowschanged += 1;
    }

    document.getElementById('textarea').innerHTML = 'Number of rows changed: ' + numrowschanged;
  }
  else {
    for (x = 0; x < numrows.length; x++){
      numrows[x].style.backgroundColor = 'initial';
    }
    document.getElementById('textarea').innerHTML = '';
  }
}


// print: document.getElementById("demo").innerHTML = 5 + 6;
