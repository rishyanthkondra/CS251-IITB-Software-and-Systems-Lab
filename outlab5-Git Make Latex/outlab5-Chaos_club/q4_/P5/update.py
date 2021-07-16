import json

with open("infinity_stones.json",'rb') as read_file:
    raw_data = (json.load(read_file))['Infinity Stones']
    for dict in raw_data:
        dict["Containment Unit"] = "Infinity Gauntlet"
    final_data = {"Infinity Stones" : raw_data}
    write_file = open('update_stones.json','w')
    json.dump(final_data,write_file,indent=4)
