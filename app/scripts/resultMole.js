
(function() {
  'use strict';


  /* 
  *
  * resultMole
  *
  *
  */


   var message = document.getElementById('message');
   var resultMole = localStorage.resultMole | 0;
   if(resultMole == 0)
        message.innerHTML = "You have nothing to worry about" + "<p/>";
    else 
        message.innerHTML = "We recomnded you to visit your doctor" + "<p/>";
 //document.getElementById('chartValue').innerHTML = '40%';
  
//     saveResult.addEventListener('click', function(event){
//       window.location.href = "http://127.0.0.1:8080/history.html";
//    })

//   history.addEventListener('click', function(event){

//   })
})();
