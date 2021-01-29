var compteurImage=1;
var totalImage=10;

function silder(x){

var image=document.getElementById('img');
compteurImage=compteurImage + x;
image.src="./static/images/nullam"+compteurImage+".jpeg";
	if (compteurImage>=totalImage){compteurImage=1;}
	if (compteurImage<1){compteurImage=totalImage;}
	
}

function silderAuto(){

var image=document.getElementById('img');
compteurImage=compteurImage + 1;
image.src="./static/images/nullam"+compteurImage+".jpeg";
	if (compteurImage>=totalImage){compteurImage=1;}
	if (compteurImage<1){compteurImage=totalImage;}
	
}

window.setInterval(silderAuto,3000);

function silderAuto1(){

var image=document.getElementById('img1');
compteurImage=compteurImage + 1;
image.src="./static/images/nullam"+compteurImage+".jpeg";
	if (compteurImage>=totalImage){compteurImage=1;}
	if (compteurImage<1){compteurImage=totalImage;}
		
}
	
window.setInterval(silderAuto1,2000);
	
