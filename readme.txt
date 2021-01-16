HOW IT WILL WORK ---------------------
the way how the website works can be broken in to 2 parts,
the first is the GUI, or the HTML pages, the second being the API or all the data

when the HTML pages are "fetched" by the browser, the JS goes to the API path (which has not been set for github yet)
the website will not work on the public domain ... yet,

Now back to the API path which is "/api/" as of now, as you will see inside the folder it has a json file containing all the data we have benn provided
now I plan to create inodes for each "node", the plan is to create a directory structure in the API path, and have JSON serving as inodes or nodes of a tree
which will ease the work of the JS in the website transversing through the data,

what I mean is 
/api/
- participants.json    # <- contains all the participants
- dir1/
- dir2/
- image.png
- inode.json           # <- this will contain all the subdirectories of the path /api/

in the given scenario, inode.json should look something like this:

= inode.json ========
"directories" : [
	"dir1",
	"dir2"
],

"files" : [
	"participants.json"
],

"images" : [
	"image.png"
]
====================

also every image will have a different directory, to ease the JS work

for thumbnailing refer to python3's lib PIL or PILLOW


DIRECTORY STRUCTURE ---------------

all the directories are paths of the website (like "StudentDirectory" and "Portfolio")
the only important directories are
- /api/ 
	this directory will contain all the data in a pseudo filesystem, with inodes
- /preProcessing/
	this will contain python code for doing all the preprocessing before activating the site
	like thumbnailing, inode generation etc

please update the readme.txt on any changes on the directory structure


TESTING ---------------------------

If on bash, or any linux like machine use "./start_server.sh"

or else go on the terminal and type "python3 -m http.server 9000"

if the above line does not function check if python3 is exported, and is accessible by the terminal/IDE, 
or try "py -3 -m http.server 9000", incase python is exported incorrectly by the OS

THE WEBSITE WILL ONLY FUNCTION ON LOCALHOST, due to it relying on APIs
