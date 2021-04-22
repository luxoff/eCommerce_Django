var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var prodId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', prodId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(prodId, action)
		}else{
			updateUserOrder(prodId, action)
		}
	})
}

function updateUserOrder(prodId, action){
	console.log('User is authenticated, sending data...')

		var url = '/updateItem/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			},
			body:JSON.stringify({'prodId':prodId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

function addCookieItem(prodId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[prodId] == undefined){
		cart[prodId] = {'quantity':1}

		}else{
			cart[prodId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[prodId]['quantity'] -= 1

		if (cart[prodId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[prodId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

	location.reload()
}

