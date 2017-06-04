function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    window.location = "/gps/" + position.coords.latitude + "+" + position.coords.longitude + "/";
}
