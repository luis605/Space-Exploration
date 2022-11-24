import json
import os
my_path = "archivements.json"

dictionary = {
    "first time": False,
    "reset": False,
    "10 minutes": False,
    }

if os.path.exists(my_path) and os.path.getsize(my_path) > 0:
    print("Archivements already exist")
else:
    print("Creating Archivements")
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
     
    # Writing to sample.json
    with open("archivements.json", "w+") as outfile:
        outfile.write(json_object)
