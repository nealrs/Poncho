document.addEventListener('DOMContentLoaded', function () {
  console.log("set src url: " + localStorage["id"]);
 	
	if (localStorage["id"] && localStorage["id"] != ""){
    document.getElementById("pframe").src = ("http://poncho.is/s/"+localStorage["id"]);
  } else { 
  		 document.getElementById("pframe").src = ("http://poncho.is/s/RW5pQ");
  	}
});