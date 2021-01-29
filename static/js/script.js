var compteurImage=1;
var totalImage=6;

function silder(x){

var image=document.getElementById('img');
compteurImage=compteurImage + x;
image.src="images/nullam"+compteurImage+".jpeg";
	if (compteurImage>=totalImage){compteurImage=1;}
	if (compteurImage<1){compteurImage=totalImage;}
	
}
function silderAuto(){

var image=document.getElementById('img');
compteurImage=compteurImage + 1;
image.src="images/nullam"+compteurImage+".jpeg";
	if (compteurImage>=totalImage){compteurImage=1;}
	if (compteurImage<1){compteurImage=totalImage;}
	
}

window.setInterval(silderAuto,3000);