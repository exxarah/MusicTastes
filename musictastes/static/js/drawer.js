function openDrawer() {
	const drawer = document.querySelector("#drawer");
	console.log('opening')

	drawer.style.width = "500px";
}

function closeDrawer() {
	const drawer = document.querySelector("#drawer");
	console.log("closing")

	drawer.style.width = "0px"
}

window.addEventListener('mouseup',function(event){
	const drawer = document.querySelector("#drawer");
	console.log('mouseup')
	if(event.target != drawer && event.target.parentNode != drawer){
		 closeDrawer();
	}
});