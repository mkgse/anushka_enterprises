filterSelection("all")
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("column");
  if (c == "all") c = "";
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
  }
}

function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);     
    }
  }
  element.className = arr1.join(" ");
}


// Add active class to the current button (highlight it)
var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function(){
    var current = document.getElementsByClassName("active1");
    current[0].className = current[0].className.replace(" active1", "");
    this.className += " active1";
  });
}

//  Read More Js
function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn1");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}

function myFunction1() {
  var dots = document.getElementById("dots1");
  var moreText = document.getElementById("more1");
  var btnText = document.getElementById("myBtn2");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}
function myFunction2() {
  var dots = document.getElementById("dots2");
  var moreText = document.getElementById("more2");
  var btnText = document.getElementById("myBtn3");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}



// course page JS

function display(){
  var x = document.getElementById('SelectA').value;

  if (x=="aa"){
    document.getElementById('a').style.display="block";
    document.getElementById('b').style.display="none";
  }
   if (x=="bb"){
    document.getElementById('a').style.display="none";
    document.getElementById('b').style.display="block";
  }
   if (x=="cc"){
    document.getElementById('c').style.display="block";
    document.getElementById('d').style.display="none";
  }


  if (x=="dd"){
    document.getElementById('c').style.display="none";
    document.getElementById('d').style.display="block";
  }
  if (x=="ee"){
    document.getElementById('e').style.display="block";
    document.getElementById('f').style.display="none";
  }
   if (x=="ff"){
    document.getElementById('e').style.display="none";
    document.getElementById('f').style.display="block";
  }

  if (x=="gg"){
    document.getElementById('g').style.display="block";
    document.getElementById('h').style.display="none";
  }
   if (x=="hh"){
    document.getElementById('g').style.display="none";
    document.getElementById('h').style.display="block";
  }

  if (x=="ii"){
    document.getElementById('i').style.display="block";
    document.getElementById('j').style.display="none";
  }
   if (x=="jj"){
    document.getElementById('i').style.display="none";
    document.getElementById('j').style.display="block";
  }

  if (x=="kk"){
    document.getElementById('k').style.display="block";
    document.getElementById('l').style.display="none";
  }
   if (x=="ll"){
    document.getElementById('k').style.display="none";
    document.getElementById('l').style.display="block";
  }

  if (x=="mm"){
    document.getElementById('m').style.display="block";
    document.getElementById('n').style.display="none";
  }
   if (x=="nn"){
    document.getElementById('m').style.display="none";
    document.getElementById('n').style.display="block";
  }

  if (x=="oo"){
    document.getElementById('o').style.display="block";
    document.getElementById('p').style.display="none";
  }
   if (x=="pp"){
    document.getElementById('o').style.display="none";
    document.getElementById('p').style.display="block";
  }

  if (x=="qq"){
    document.getElementById('q').style.display="block";
    document.getElementById('r').style.display="none";
  }
   if (x=="rr"){
    document.getElementById('q').style.display="none";
    document.getElementById('r').style.display="block";
  }


  if (x=="ss"){
    document.getElementById('s').style.display="block";
    document.getElementById('t').style.display="none";
  }  

   if (x=="tt"){
    document.getElementById('s').style.display="none";
    document.getElementById('t').style.display="block";
   }  

   else if(x=="zz"){
    document.getElementById('z').style.display="block";
   }

} 