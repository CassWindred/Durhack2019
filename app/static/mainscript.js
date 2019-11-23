alert("mainscript.js loaded!");
console.log("WHAT  ");




function initMap() {
  // The location of Uluru
  var uluru = {lat: -25.344, lng: 131.036};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 4, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});

    google.maps.event.addListener(map, 'click', function(event) {
    onClick(event, map);
  });
}

function onClick(event) {
  if ("placeId" in event) {
    let placeId = event.placeId;
    console.log("A place was clicked! ID: "+placeId);
  } else {
    console.log("A click was detected, but, well, I dont think it was a place");
  }

}
