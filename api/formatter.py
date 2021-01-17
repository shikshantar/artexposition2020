import os
import json
from PIL import Image

def main ():
    # move all the images from directories to this directory

    mypath = "."
    files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and " " in f]


    directories = []

    for f in files:
        try:
            dirname = constructDirectoriesAndJson(os.path.join(mypath, f), f.split("_"), f)
            if dirname != None:
                directories.append(dirname)
        except  :
            print(f)

    print(directories)

    for directory in directories:
        print("l")
        createInode(directory)


# path is the path to the given picture
# name_vars is basically all the data in the name
def constructDirectoriesAndJson (img_path, name_vars, file_name):
    THUMBNAIL_SIZE = (757,757)
    directory = None


    dirname = "./pictures/"+name_vars[0] + "_" + name_vars[1]

    if not os.path.isdir(dirname):
        os.mkdir(dirname)
        print(dirname)
        directory = dirname

    project_name = name_vars[2]

    project_path = os.path.join(dirname,project_name)
    os.mkdir(project_path)

    img = Image.open(img_path)
    img.thumbnail(THUMBNAIL_SIZE)
    img.save(os.path.join(project_path,"thumbnail.jpg"))

    os.rename(img_path,os.path.join(project_path,file_name))

    return directory

def createInode(path):
    data = json.dumps(os.listdir(path))
    inode = open(os.path.join(path,"inode.json"), "w+")
    inode.write(data)
    inode.close()


main()
