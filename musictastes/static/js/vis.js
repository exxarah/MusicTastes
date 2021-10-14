function alignWidths(){
    const bars = document.querySelectorAll(".bar");
    const totalWidth = document.querySelector('#content').clientWidth;
    const totalHeight = document.querySelector('#content').clientHeight;
    document.querySelector('#vis-box').style.height = totalHeight.toString() + 'px';
    let allWidths = 0;
    // Get the maximum, to then iterate again and get the percentage
    bars.forEach(function (currentValue, currentIndex, listObj) {
        let data = currentValue.dataset.track;
        data = JSON5.parse(data);
        allWidths += data.track.popularity;
    })
    bars.forEach(function (currentValue, currentIndex, listObj) {
        let data = currentValue.dataset.track;
        data = JSON5.parse(data);
        let width = (data.track.popularity / allWidths) * totalWidth;
        currentValue.style.width = width.toString() + 'px';
    })
}

// https://lokeshdhakar.com/projects/color-thief for reference, this uses the dominant colour, but we can also
// get a colour palette from it if we want
function setColours(){
    const bars = document.querySelectorAll(".bar");
    const colorThief = new ColorThief();

    bars.forEach(function (currentValue, currentIndex, listObj){
        let data = currentValue.dataset.track;
        data = JSON5.parse(data);
        const imgUrl = data.track.album.images[1].url

        var img = new Image();
        img.addEventListener('load', function () {
            let imgColor = colorThief.getColor(img);
            listObj.item(currentIndex).style.backgroundColor = `rgb(${imgColor[0]}, ${imgColor[1]}, ${imgColor[2]})`;
        });
        img.crossOrigin = 'Anonymous';
        img.src = imgUrl;
    });
}

window.onload = function() {
  alignWidths();
  setColours();
};