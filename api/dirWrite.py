import json
import os

file_name = 'participants.json'

with open(file_name) as f:
    data = json.load(f)

def names_and_numbers():
    names = []
    number_of_images = []

    for dir in os.listdir("formatted"):
        parts = os.listdir("formatted/" + dir)[0].split("_")
        names.append(parts[0])
        number_of_images.append(len(os.listdir("formatted/" + dir)))

    return names, number_of_images

def file_structure(students, image_list):
    for item in data.items():
        path = ""
        path = path + item[0]

        for participant in item[1].items():
            halfpath = ""
            halfpath = path + "_" + participant[0]

            for name in participant[1]:
                split_name = name.split(" ")
                joint_name = ''.join(split_name)

                fullpath = ""
                fullpath = joint_name + "_" + halfpath

                # check if the given directory can be made
                # if not then recreate after deleting the directory
                try:
                    os.mkdir(fullpath)
                except FileExistsError:
                    print("file exists")
                    return None

                os.chdir(fullpath)

                with open("inode.json", 'w') as f:
                    pass

                i = 0

                for student in students:
                    if name.strip() == student:
                        students.pop(i)
                        images = image_list.pop(i)

                        for j in range(images):
                            os.mkdir("image" + str(j + 1))

                    i += 1

                os.chdir("..")

def main():
    participants, images = names_and_numbers()
    file_structure(participants, images)


if __name__ == "__main__":
    main()
