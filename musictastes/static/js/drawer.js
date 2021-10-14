function openDrawer(obj) {
	obj.setAttribute('data-width', obj.style.width);
	obj.setAttribute("data-selected", true)
	obj.style.width = '500px';
	// const drawer = document.querySelector("#drawer");
	// drawer.style.width = "500px";
}

function updateDrawer(clickedObj, drawerObj) {
	if (clickedObj.tagName != 'BUTTON') { return; }
	var data = clickedObj.dataset.track;
	data = JSON5.parse(data);
	drawerObj.querySelector('#track-name').innerHTML = data.track.name;
	drawerObj.querySelector('#track-artist').innerHTML = data.track.artists[0].name;
	drawerObj.querySelector('#track-album').innerHTML = data.track.album.name;
	drawerObj.querySelector('#track-date').innerHTML = data.track.album.release_date;
	drawerObj.querySelector('#track-link').setAttribute('href', data.track.external_urls.spotify);
	drawerObj.querySelector('#track-image').setAttribute('src', data.track.album.images[1].url);
}

function closeDrawer() {
	const obj = document.querySelector('[data-selected=true]')
	obj.style.width = obj.dataset.width;
	obj.removeAttribute('data-selected');
	// const drawer = document.querySelector("#drawer");
	// drawer.style.width = "0px"
}

window.addEventListener('mouseup',function(event){
	closeDrawer();
});

window.addEventListener('click', function(event) {
	const drawer = document.querySelector("#drawer");
	const button = event.target;

	updateDrawer(button, drawer)
});
