
console.log("WHAT  ");


function initMap() {
  // The location of Uluru
  let uluru = {lat: -25.344, lng: 131.036};
  // The map, centered at Uluru
  let map = new google.maps.Map(
      document.getElementById('map'), {zoom: 4, center: uluru});
  // The marker, positioned at Uluru
  let marker = new google.maps.Marker({position: uluru, map: map});
  let placeService = new google.maps.places.PlacesService(map);

    google.maps.event.addListener(map, 'click', function(event) {
    onClick(event, map, placeService);
    event.stop() //Prevents the event from propogating to that the standard popup does not appear
  });



}

function onClick(event, map, placeService) { //Triggers on a click event
  if ("placeId" in event) { //If the click was on an existing place, the event will contain "placeId"
    let placeId = event.placeId;
    console.log("A place was clicked! ID: "+placeId);
    let request = {
  placeId: placeId,
  fields: ['name', 'rating', 'formatted_phone_number', 'geometry']
};

placeService.getDetails(request, callback);



  } else {
    console.log("A click was detected, but, well, I dont think it was a place");
  }
}

function callback(place, status) {
  if (status === google.maps.places.PlacesServiceStatus.OK) {
      var contentString = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h1 id="firstHeading" class="firstHeading">' + place.name + '</h1>'+
      '<div id="bodyContent">'+
      '<p>TESTCONTENT</p>'+'</div>'+
      '</div>';
    alert("You clicked on "+place.name+"!");
  }
}