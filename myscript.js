startBackgroundRotation = async (images, delay) => {
	rotation_index = 0

	function rotate(imgs, index) {
		document.getElementById("slideshow").style.backgroundImage = `url(${imgs[index%imgs.length]})`

		return index + 1
	}

	setInterval(() => {
		rotation_index = rotate(images, rotation_index) 
	}, delay);
}

(function() {
	images = [
		"https://i.pinimg.com/originals/03/a5/c0/03a5c0ebf4564272f44745728f61e873.jpg",
		"https://www.pixelstalk.net/wp-content/uploads/2016/05/Neon-Genesis-Evangelion-Background.jpg",
		"https://wallup.net/wp-content/uploads/2017/11/17/349484-JoJos_Bizarre_Adventure-mask.jpg",
		"https://wallup.net/wp-content/uploads/2016/01/165936-abstract-minimalism-fantasy_art-white_background.jpg",
	]
	startBackgroundRotation(images,10000)

})()