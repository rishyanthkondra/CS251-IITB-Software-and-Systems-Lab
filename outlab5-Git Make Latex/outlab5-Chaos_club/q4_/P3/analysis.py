import csv
import numpy as np
readfile = csv.reader(open('info_day.csv'),delimiter=',')
temp = []
hum = []
lig = []
co2 = []
for row in readfile :
    temp.append(row[1])
    hum.append(row[2])
    lig.append(row[3])
    co2.append(row[4])
tempnp = np.array([float(x) for x in temp[1:]])
humnp = np.array([float(x) for x in hum[1:]])
lignp = np.array([float(x) for x in lig[1:]])
co2np = np.array([float(x) for x in co2[1:]])
alldata = np.array([tempnp,humnp,lignp,co2np])

mean = []
std = []

for x in alldata:
    mean.append(np.mean(x))
    std.append(np.std(x))

mean = ['{0:<20}'.format(str(x)) for x in mean]
std = ['{0:<20}'.format(str(x)) for x in std]

print ('{0:<20}'.format("Field") ,'{0:<20}'.format("Mean"),'{0:<20}'.format("Std. Dev."))
print ('{0:<20}'.format("Temperature") ,mean[0],std[0])
print ('{0:<20}'.format("Humidity") ,mean[1],std[1])
print ('{0:<20}'.format("Light") ,mean[2],std[2])
print ('{0:<20}'.format("CO2") ,mean[3],std[3])
