function alignHeights(){
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
    console.log(allHeights)
    console.log('hi')

}

window.onload = function() {
  alignHeights();
};