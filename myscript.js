startBackgroundRotation = async (totalImages, delay) => {
	rotation_index = 0

	function rotate(totalImages, index) {
		document.getElementById("slideshow").style.backgroundImage = `url(./staticAssets/banner/${index%totalImages}.jpg)`
		console.log(index)
		return index + 1
	}

	setInterval(() => {
		rotation_index = rotate(totalImages, rotation_index)
	}, delay);
}

(function() {

	startBackgroundRotation(5,3000)

})()
