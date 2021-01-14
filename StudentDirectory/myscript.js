var participants

var active_tab = document.getElementById("tab-holder").children[0];

var API_PATH = "/api/"

var test_images = [
	"/thumbnailer/artWebsite/bani/bani_poster1/(320, 320).jpg",
	"/thumbnailer/artWebsite/nandini/nandini_cover1/(320, 320).jpg",
	"/thumbnailer/artWebsite/Taesha/Taesha_still-life/(320, 320).jpg"
]

fetchFromAPI = async (path,func) => {
	await fetch(API_PATH+path).
	then (str => str.json()).
	then (obj => func(obj))
}

getSortedParticipants = grade => {
	elegibleParticipants = participants[grade]

	keys = Object.keys(elegibleParticipants)
	var sortedParticipants = []

	for (key of keys) {
		var group = key
		var participantsInGroup = elegibleParticipants[group]

		for (participant of participantsInGroup) {
			//create an object representing each participant
			var participant = {
				"group" : group,
				"name" : participant,
				"artwork" : []
			}

			sortedParticipants.push(participant)
		}
		/*
		old code fpr shuffling, never know when it might be used
		sortedParticipants = shuffle(sortedParticipants)
		sortedParticipants = shuffle(sortedParticipants)
		*/

		sortedParticipants.sort(function(a, b) {
			var textA = a.name.toUpperCase();
			var textB = b.name.toUpperCase();
			return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;
		});
	}
	return sortedParticipants

}

shuffle = a => {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
}

generateShowcase = participants => {
	HTML = `<div class="image-column">`
	
	participant_rows = divideArray(participants,3)

	participant_rows.forEach (participant_row => {
		HTML += `<div class="image-row">`

		participant_row.forEach (participant => {
			console.log(participant)
			HTML += `<div class="image">
			<img src='https://wolper.com.au/wp-content/uploads/2017/10/image-placeholder.jpg'>
			<h6 style="padding-top: 0.5rem; padding-left: 0.5rem; padding-right: 0.5rem">${participant.name}</h6>
			<p style="padding: 0 0.5rem ">${participant.group}</p>
			<div class="view-more">
				View more
			</div>
			</div>`
		})
		HTML += `</div>`
	})

	HTML += '<div>'

	return HTML
}

divideArray = (arr,num) => {
	rows = [[], [], []]
	for (var i=0; i< arr.length; i++) {
		remainder = i%3
		if (remainder == 0) {
			rows[0].push(arr[i])
		} else if (remainder == 1) {
			rows[1].push(arr[i])
		} else {
			rows[2].push(arr[i])
		}
	}

	return rows
}

initialiseParticipantButtonAction = () => {
	var btns = Array.prototype.slice.call(document.getElementsByClassName("view-more"))
	console.log(btns)
	btns.forEach(btn => {

		btn.authorName = btn.textContent;

		btn.onclick = function (){
			openPortfolio(this.authorName)
		}
	})
}


openPortfolio = name => {
	window.open("/Portfolio?p="+name)
}


initialise_participants = async () => {
	await fetchFromAPI("participants.json", p => {
		participants = p
	})
}

executeDropdownBehaviour = tag => {
	var groups = Object.keys(tag.dropdown_content)

	if (document)

	div = document.createElement("div");
	div.id = this.class + "-dropdown"
	inner_html = ""

	groups.forEach( group => {
		inner_html += `
			<div>
			</div>
		`
	} )
}

getAndDisplayOpeningDialogue = () => {
	display = document.getElementById("data_display")

	fetch ("./introduction.html").
	then (response => response.text()).
	then (data => {
		display.innerHTML = data
		active_tab.classList.remove("active-tab");
		this.classList.add("active-tab");
		active_tab = this;
	})

}

(async function() {
	var tabs = document.getElementById('tab-holder');
	var children = Array.prototype.slice.call(tabs.children);

	await initialise_participants()

	children.forEach(child => {
		if (!child.textContent.includes("<")) {
			child.onclick = function () {
				this.class = this.textContent
				this.dropdown_content = participants[this.textContent]
	
				//executeDropdownBehaviour(this)
				
				grade = this.textContent
				this.sortedParticipants = getSortedParticipants(grade)
	
				HTML = generateShowcase(this.sortedParticipants)
	
				console.log(this.sortedParticipants)
				
				document.getElementById("data_display").innerHTML = HTML;
				initialiseParticipantButtonAction()
				active_tab.classList.remove("active-tab");
				this.classList.add("active-tab");
	
				active_tab = this;
				
			}
		}
	})
	
	getAndDisplayOpeningDialogue()

})();
