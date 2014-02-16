document.addEventListener('DOMContentLoaded', function () {
 	console.log("set src url: " + localStorage["id"]);
	document.getElementById("pframe").src = ("http://poncho.is/s/"+localStorage["id"]);
});