from PIL import Image

import os
import json
import shutil
import glob

def inode():
    try:
        for dir in os.listdir():
            if dir != "formatted":
                os.chdir(dir)

                with open("inode.json", 'w') as f:
                    json.dump(os.listdir(), f)

                os.chdir("..")
    except NotADirectoryError:
        pass

def images():
    try:
        for dir in os.listdir():
            if dir != "formatted":
                for fold in os.listdir("formatted"):
                    i = 1
                    for image in os.listdir("formatted/" + fold):
                        name = image.split("_")
                        split_name = name[0].split()
                        joint_name = ''.join(split_name)

                        if joint_name == dir.split("_")[0]:
                            shutil.move("formatted/" + fold + "/" + image, dir + "/image" + str(i))

                            os.chdir(dir + "/image" + str(i))
                            size = 128, 128

                            for infile in glob.glob(image):
                                file, ext = os.path.splitext(infile)
                                image = Image.open(infile)
                                image.thumbnail(size, Image.ANTIALIAS)
                                image.save(file + ".thumbnail", "JPEG")

                            os.chdir("../..")

                        i += 1
    except NotADirectoryError:
        pass

def main():
    inode()
    images()


main()
