Webcam.set({
  width: 320,
  height: 240,
  image_format: 'jpeg',
  jpeg_quality: 90
});
Webcam.attach( '#preview' );

var visionAPI = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyC4favvvJpRvUqFjmPkpLJzJJ5-pRThpnY'

function take_snapshot() {
  // take snapshot and get image data
  Webcam.snap(function(data_uri) {
    var request = {
      'requests': [{
        'image': {
        	'content': data_uri.substring(data_uri.indexOf("base64,") + 7),
        },
        'features':{
        	'type': 'TEXT_DETECTION',
        	'maxResults': 50,
        }
      }],
    }
    console.log(request);
    $.ajax({
      type: "POST",
      url: visionAPI,
      data: JSON.stringify(request),
      contentType: 'application/json',
      dataType:"json",
      success: function(data){
      	var items = data.responses[0].textAnnotations;
      	for( var i = 0; i < items.length; i++){
      	  $("#output").append("<div>"+items[i].description+"</div>");
      	}
      },
      error: function(data){
      	console.log(data);
      }
    });
  });
}