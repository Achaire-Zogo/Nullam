var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var ticketId = this.dataset.ticket
		var action = this.dataset.action
		console.log('ticketId:', ticketId, 'Action:', action)
		updateUserOrder(ticketId, action)
		
	})
}

function updateUserOrder(ticketId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_ticket/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'ticketId':ticketId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}
