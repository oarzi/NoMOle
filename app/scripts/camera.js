/*!
 *
 *  Web Starter Kit
 *  Copyright 2015 Google Inc. All rights reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *    https://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License
 *
 */
/* eslint-env browser */
(function() {
  'use strict';

  // Check to make sure service workers are supported in the current browser,
  // and that the current page is accessed from a secure origin. Using a
  // service worker from an insecure origin will trigger JS console errors. See
  // http://www.chromium.org/Home/chromium-security/prefer-secure-origins-for-powerful-new-features
  var isLocalhost = Boolean(window.location.hostname === 'localhost' ||
      // [::1] is the IPv6 localhost address.
      window.location.hostname === '[::1]' ||
      // 127.0.0.1/8 is considered localhost for IPv4.
      window.location.hostname.match(
        /^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/
      )
    );

  if ('serviceWorker' in navigator &&
      (window.location.protocol === 'https:' || isLocalhost)) {
    navigator.serviceWorker.register('service-worker.js')
    .then(function(registration) {
      // updatefound is fired if service-worker.js changes.
      registration.onupdatefound = function() {
        // updatefound is also fired the very first time the SW is installed,
        // and there's no need to prompt for a reload at that point.
        // So check here to see if the page is already controlled,
        // i.e. whether there's an existing service worker.
        if (navigator.serviceWorker.controller) {
          // The updatefound event implies that registration.installing is set:
          // https://slightlyoff.github.io/ServiceWorker/spec/service_worker/index.html#service-worker-container-updatefound-event
          var installingWorker = registration.installing;

          installingWorker.onstatechange = function() {
            switch (installingWorker.state) {
              case 'installed':
                // At this point, the old content will have been purged and the
                // fresh content will have been added to the cache.
                // It's the perfect time to display a "New content is
                // available; please refresh." message in the page's interface.
                break;

              case 'redundant':
                throw new Error('The installing ' +
                                'service worker became redundant.');

              default:
                // Ignore
            }
          };
        }
      };
    }).catch(function(e) {
      console.error('Error during service worker registration:', e);
    });
  }




  // Your custom JavaScript goes here


    /* 
  *
  * picture 
  *
  *
  */



  // The width and height of the captured photo. We will set the
  // width to the value defined here, but the height will be
  // calculated based on the aspect ratio of the input stream.

  var width = 320;    // We will scale the photo width to this
  var height = 0;     // This will be computed based on the input stream

  // |streaming| indicates whether or not we're currently streaming
  // video from the camera. Obviously, we start at false.

  var streaming = false;

  // The various HTML elements we need to configure or control. These
  // will be set by the startup() function.

  var video = null;
  var canvas = null;
  var photo = null;
  var startbutton = null;
  var cancelPicture = null;
  var nextPicture = null;
  var buttensPicture = null;
  var imageData = null;
  var backHome = null;

  function startup() {
    cancelPicture = document.getElementById('cancelPicture');
    nextPicture = document.getElementById('nextPicture');
    buttensPicture = document.getElementById('buttensPicture'); 
    video = document.getElementById('video');
    canvas = document.getElementById('canvas');
    photo = document.getElementById('photo');
    backHome = document.getElementById('backHome');
    startbutton = document.getElementById('startbutton');

    canvas.setAttribute("hidden", true);
    buttensPicture.setAttribute("hidden", true);

    cancelPicture.addEventListener('click', function(event){
          canvas.setAttribute("hidden", true);
          buttensPicture.setAttribute("hidden", true);
          backHome.removeAttribute("hidden");
          startbutton.removeAttribute("hidden");
          video.removeAttribute("hidden");

    })
    nextPicture.addEventListener('click', function(event){
            var httpPost = new XMLHttpRequest(),
        path = "http://192.168.0.52:7891/image/";

        var xhr_open_base = httpPost.open;
        // native XmlHttpRequest.open() signature from XmlHttpRequest API
        httpPost.open = function (method, url, async, user, password) {
        xhr_open_base.apply(this, arguments);
        httpPost.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      }

    httpPost.onreadystatechange = function(err) {
            if (httpPost.readyState == 4 && httpPost.status == 200){
                localStorage.resultMole = httpPost.responseText;
                console.log(httpPost.responseText);
                window.location.href = "http://192.168.0.59:8080/resultMole.html";r
            } else {
                console.log(err);
            }
        };
    // Set the content type of the request to json since that's what's being sent
    //httpPost.setHeader('Content-Type', 'application/json');
    //httpPost.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    httpPost.open("POST", path, true);
    httpPost.send("file="+ encodeURIComponent(imageData));

    })  
    

    navigator.getMedia = ( navigator.getUserMedia ||
                           navigator.webkitGetUserMedia ||
                           navigator.mozGetUserMedia ||
                           navigator.msGetUserMedia);

    navigator.getMedia(
      {
        video: true,
        audio: false
      },
      function(stream) {
        if (navigator.mozGetUserMedia) {
          video.mozSrcObject = stream;
        } else {
          var vendorURL = window.URL || window.webkitURL;
          video.src = vendorURL.createObjectURL(stream);
        }
        video.play();
      },
      function(err) {
        console.log("An error occured! " + err);
      }
    );

    video.addEventListener('canplay', function(ev){
      if (!streaming) {
        height = video.videoHeight;
        width = video.videoWidth;//(video.videoHeight / (video.videoWidth/width));
      
        // Firefox currently has a bug where the height can't be read from
        // the video, so we will make assumptions if this happens.
      
        if (isNaN(height)) {
          height = width / (4/3);
        }
      
        video.setAttribute('width', width);
        video.setAttribute('height', height);
        canvas.setAttribute('width', width);
        canvas.setAttribute('height', height);
        streaming = true;
      }
    }, false);

    startbutton.addEventListener('click', function(ev){
      canvas.removeAttribute("hidden");
      takepicture();
      ev.preventDefault();
    }, false);
    
    clearphoto();
  }

  // Fill the photo with an indication that none has been
  // captured.

  function clearphoto() {
    var context = canvas.getContext('2d');
    context.fillStyle = "#AAA";
    context.fillRect(0, 0, canvas.width, canvas.height);

    imageData = canvas.toDataURL('image/jpg');
    photo.setAttribute('src', imageData);
  }
  
  // Capture a photo by fetching the current contents of the video
  // and drawing it into a canvas, then converting that to a PNG
  // format data URL. By drawing it on an offscreen canvas and then
  // drawing that to the screen, we can change its size and/or apply
  // other changes before drawing it.

  function takepicture() {
    var context = canvas.getContext('2d');
    if (width && height) {
      canvas.width = width;
      canvas.height = height;
      context.drawImage(video, 0, 0, width, height);
      imageData = canvas.toDataURL('image/png');
      photo.setAttribute('src', imageData);
      photo.setAttribute("hidden", true);
      video.setAttribute("hidden", true);
      buttensPicture.removeAttribute("hidden");
      startbutton.setAttribute("hidden", true);
      backHome.setAttribute("hidden", true);
      
    } else {
      clearphoto();
    }
  }

  // Set up our event listener to run the startup process
  // once loading is complete.
window.addEventListener('load', startup, false);


})();
