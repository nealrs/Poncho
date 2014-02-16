function loadOptions() {
	console.log("load options: " + localStorage["id"]);
	document.getElementById("refid").value = localStorage["id"];
}

function saveOptions() {
	localStorage["id"] = document.getElementById("refid").value;
	console.log("save options: " + localStorage["id"]);
	document.getElementById("msg").style.visibility = 'visible';
}

// event listeners.
document.addEventListener('DOMContentLoaded', function () {
  loadOptions();
  getGIF();
  document.getElementById('savebut').addEventListener('click', saveOptions);
});

// giphy API call
function getGIF(){
	request = new XMLHttpRequest;
	request.open('GET', 'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=cats', true);

	request.onload = function() {
	  if (request.status >= 200 && request.status < 400){
	    data = JSON.parse(request.responseText).data.image_url;
	    console.log(data);
	    document.getElementById("catbox").innerHTML = '<center><img style="text-align:center;" src = "'+data+'"  title="Cats via Giphy"></center>';
	  } else {
	  		console.log('reached giphy, but it returned an error');
	   }
	};

	request.onerror = function() {
	  console.log('connection error');
	};

	request.send();
}