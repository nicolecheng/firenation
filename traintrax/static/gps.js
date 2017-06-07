function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition,
            function(failure) {
                $.getJSON('https://ipinfo.io/geo', function(response) {
                  var loc = response["loc"].split(',');
                  console.log(loc);
                  window.location = "/gps/" + loc[0] + "+" + loc[1] + "/";
                });
            }
        );
    } else {
        alert("Geolocation is not supported by this browser.");
    }
};

function showPosition(position) {
    window.location = "/gps/" + position.coords.latitude + "+" + position.coords.longitude + "/";
};
