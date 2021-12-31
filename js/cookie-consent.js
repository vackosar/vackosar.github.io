window.addEventListener('load', (event) => {

  checkCookie_eu();

  function getScript(scriptUrl, callback) {
    const script = document.createElement('script');
    script.src = scriptUrl;
    script.onload = callback;

    document.body.appendChild(script);
  }

  function checkCookie_eu() {
    var consent = getCookie_eu("cookies_consent");
    if (consent) {
      accept()

    } else {
      // show notification bar
      document.getElementById('cookie_directive_container').style.display = 'block';
    }

  }

  function setCookie_eu(c_name, value, exdays) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value = escape(value) + ((exdays == null) ? "" : "; expires=" + exdate.toUTCString());
    document.cookie = c_name + "=" + c_value + "; path=/; Secure; SameSite=Strict";
    document.getElementById('cookie_directive_container').style.display = 'none';
  }

  function getCookie_eu(c_name) {
    var i, x, y, ARRcookies = document.cookie.split(";");
    for (i = 0; i < ARRcookies.length; i++) {
      x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
      y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
      x = x.replace(/^\s+|\s+$/g, "");
      if (x === c_name) {
        return unescape(y);
      }
    }
  }

  function accept() {
    setCookie_eu("cookies_consent", 1, 30);
    execute();

  }

   function reject() {
     setCookie_eu("cookies_consent", 0, 30);

   }

  function execute() {
    <!-- Google Analytics -->
    getScript('https://www.googletagmanager.com/gtag/js?id=UA-165114534-1', function () {
      window.dataLayer = window.dataLayer || [];

      function gtag() {
        dataLayer.push(arguments);
      }

      gtag('js', new Date());
      gtag('config', 'UA-165114534-1');

    });
    <!-- end of Google Analytics-->

  }

  document.getElementById('cookie_accept').onclick = accept;
  document.getElementById('cookie_reject').onclick = reject;
});