import json
import os

file_name = 'participants.json'
parent_dir = ''

with open(file_name) as f:
	data = json.load(f)

def main():	
    dirs = []
    
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
                    os.mkdir(parentdir + '/' + fullpath)
                except:
                    os.rmdir(parentdir + '/' + fullpath)
                    os.mkdir(parentdir + '/' + fullpath)
			
		dirs.append(fullpath)
                
                
main()

with open('inode.json', 'w') as f:
    json.dump(dirs, f)
      
