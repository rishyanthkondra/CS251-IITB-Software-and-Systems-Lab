import json
import csv

csv_file = open('infinity_stones.csv','w')
csv.register_dialect('custom',delimiter = '|',quoting= csv.QUOTE_NONE)

with open("infinity_stones.json",'rb') as read_file:
    raw_data = (json.load(read_file))['Infinity Stones']
    field_names = ['Stone Name','Stone Color','Containment Unit']
    csv_write = csv.DictWriter(csv_file,fieldnames=field_names,dialect='custom')
    csv_write.writeheader()
    csv_write.writerows(raw_data)
