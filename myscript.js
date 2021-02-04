startBackgroundRotation = async (images, delay) => {
	rotation_index = 0

	function rotate(imgs, index) {
		document.getElementById("slideshow").style.backgroundImage = `url(./staticAssets/banner/${index%imgs.length}.jpg)`

		return index + 1
	}

	setInterval(() => {
		rotation_index = rotate(images, rotation_index) 
	}, delay);
}

(function() {
	
	startBackgroundRotation(images,10000)

})()