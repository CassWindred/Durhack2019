console.log("WHAT  ");
const Http = new XMLHttpRequest();
const url = window.location.host;


function initMap() {
    // The location of Uluru
    let rundle = {lat: -34.922785, lng: 138.602589};
    // The map, centered at Uluru
    let map = new google.maps.Map(
        document.getElementById('map'), {zoom: 14, center: rundle});
    let placeService = new google.maps.places.PlacesService(map);

    google.maps.event.addListener(map, 'click', function (event) {
        onClick(event, map, placeService);
        event.stop() //Prevents the event from propogating to that the standard popup does not appear
    });


}

function onClick(event, map, placeService) { //Triggers on a click event
    if ("placeId" in event) { //If the click was on an existing place, the event will contain "placeId"
        let placeId = event.placeId;
        console.log("A place was clicked! ID: " + placeId);
        let request = {
            placeId: placeId,
            fields: ['name', 'geometry']
        };

        placeService.getDetails(request, function (place, status) {
          let pathTarget;
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var contentString = '<div id="content">' +
                '<div id="siteNotice">' +
                '</div>' +
                '<h1 id="firstHeading" class="firstHeading">' + place.name + '</h1>' +
                '<div id="bodyContent">' +
                '<p>TESTCONTENT</p>' +
                '</div>' +
                '</div>';
            var infowindow = new google.maps.InfoWindow({
              content: contentString,
              position: place.geometry.location
            });
            infowindow.open(map);
            let pathTarget = "/getPlaceInfo/" + placeId;
            console.log(pathTarget);
            Http.open("GET", pathTarget);
            Http.send();

            Http.onreadystatechange = (e) => {
              console.log("HTTP RESPONSE RECEIVED");
              console.log(Http.responseText);
              contentString='<div id="content">' +
                '<div id="siteNotice">' +
                '</div>' +
                '<h1 id="firstHeading" class="firstHeading">' + place.name + '</h1>' +
                '<div id="bodyContent">' +
                '<p>Place ID: '+placeId +'</p>' +
                '<p>'+ Http.responseText + '</p></div>' +
                '<a href="submit/' + placeId + '">Submit more info</a>' + '</div>' +
                '</div>';
              infowindow.setContent(contentString)
            }

          }
        })
    } else {
        console.log("A click was detected, but, well, I dont think it was a place");
    }
}

