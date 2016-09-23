
(function() {
  'use strict';
  /* 
  *
  * main
  *
  *
  */


   var photograph = document.getElementById('photograph');
   //var appointment = document.getElementById('appointment');
   //var history = document.getElementById('history');
  
   photograph.addEventListener('click', function(event){
     window.location.href = "http://192.168.0.59:8080/camera.html";
  })
})();
