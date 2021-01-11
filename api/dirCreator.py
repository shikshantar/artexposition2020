import json
import os

file_name = 'participants.json'

with open(file_name) as f:
	data = json.load(f)

def main():	
    
    for item in data.items():
        path = ""
        path = path + item[0]
        
        for thing in item[1].items():
            halfpath = ""
            halfpath = path + "_" + thing[0]
            
            for name in thing[1]:
                split_name = name.split(" ")
                joint_name = ''.join(split_name)
                
                fullpath = ""
                fullpath = joint_name + "_" + halfpath
                
                os.mkdir(fullpath)
                
                
main()
                
                
                
                
    
                
    
            

        
    