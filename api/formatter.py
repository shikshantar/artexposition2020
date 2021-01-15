import os
from PIL import Image

def main ():
    # move all the images from directories to this directory 
    os.system("mv ./formatted/*_*/* .")
    
    mypath = "."
    files = [f for f in os.listdir(mypath) if os.isfile(os.join(mypath, f) and f.endswith("jpg")]

    for f in files:
        constructDirectoriesAndJson(os.join(mypath, f), name.split("_"), file_name)
    
    createInode(my_path)


# path is the path to the given picture
# name_vars is basically all the data in the name
def constructDirectoriesAndJson (img_path, name_vars, file_name):
    THUMBNAIL_SIZE = (757,757)    


    dirname = "./pictures/"+name_vars[0] + "_" + name_vars[1]

    if not os.path.isdir(dirname):
        os.mkdir(dirname)

    project_name = name_vars[2]

    project_path = os.join(dirname,project_name)
    os.mkdir(project_path)

    img = Image.open(img_path)
    img.thumbnail(THUMBNAIL_SIZE)
    img.save(os.join(project_path,"thumbnail.jpg"))

    os.rename(img_path,os.join(project_path,file_name))

def createInode(path):
    inode = {
        "directories" : []
        "files" : []
    }
    for f in os.listdir():
        if os.isdir(f):
            inode["directories"].append(f)
        else:
            inode["files"].append(f)

    json.dump(inode,open("inode.json", "w+"))
