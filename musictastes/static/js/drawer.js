function openDrawer(obj) {
	obj.setAttribute('data-width', obj.style.width);
	obj.setAttribute("data-selected", true)
	obj.style.width = '500px';
	updateDrawer(obj)
	const drawerObj = document.querySelector("#drawer");
	obj.innerHTML = drawerObj.innerHTML;
	// const drawer = document.querySelector("#drawer");
	// drawer.style.width = "500px";
}

function updateDrawer(clickedObj) {
	if (clickedObj.tagName != 'BUTTON') { return; }
	const drawerObj = document.querySelector("#drawer");
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
	obj.innerHTML = "";
	// const drawer = document.querySelector("#drawer");
	// drawer.style.width = "0px"
}

window.addEventListener('onmouseleave',function(event){
	closeDrawer();
});

window.addEventListener('resize', function () {
    closeDrawer();
})
