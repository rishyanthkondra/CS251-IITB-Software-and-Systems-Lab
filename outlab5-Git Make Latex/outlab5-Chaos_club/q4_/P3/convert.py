import csv
import numpy as np

def con(k):
    return (9*k/5) + 32

readfile = csv.reader(open('info_day.csv'),delimiter=',',quotechar='|')
head = []
temp = []
hum = []
lig = []
co2 = []
for row in readfile :
    head.append(row[0])
    temp.append(row[1])
    hum.append(row[2])
    lig.append(row[3])
    co2.append(row[4])
temp[1:] = [con(float(x)) for x in temp[1:]]
alldata = (np.array([head,temp,hum,lig,co2])).transpose()
writefile = csv.writer(open('transformed.csv','w',newline=''),quotechar='|',quoting=csv.QUOTE_MINIMAL)
writefile.writerows(alldata)
