function openDrawer() {
	const drawer = document.querySelector("#drawer");
	drawer.style.width = "500px";
}

function updateDrawer(clickedObj, drawerObj) {
	if (clickedObj.tagName != 'BUTTON') { return; }
	console.log(clickedObj.dataset.track);
}

function closeDrawer() {
	const drawer = document.querySelector("#drawer");
	drawer.style.width = "0px"
}

window.addEventListener('mouseup',function(event){
	const drawer = document.querySelector("#drawer");
	if(event.target != drawer && event.target.parentNode != drawer){
		 closeDrawer();
	}
});

window.addEventListener('click', function(event) {
	const drawer = document.querySelector("#drawer");
	const button = event.target;

	updateDrawer(button, drawer)
});
