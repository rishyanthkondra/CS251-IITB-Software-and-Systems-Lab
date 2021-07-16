import csv
import numpy as np
days = []
nights = []
readfile = csv.reader(open('info_day.csv'),delimiter=',',skipinitialspace = True)
for rows in readfile:
    days.append(rows)
readfile = csv.reader(open('info_night.csv'),delimiter=',',skipinitialspace = True)
for rows in readfile:
    nights.append(rows)

for x in range(1,5):
    days[0][x] = days[0][x] + '(Day)'
    nights[0][x] = nights[0][x] + '(Night)'
    
days = (np.array(days)).transpose()
nights = (np.array(nights)).transpose()

final = [days[0]]
for x in range(1,5):
    final.append(days[x])
    final.append(nights[x])
final= (np.array(final)).transpose()
final = [['{0: <18}'.format(x) for x in y] for y in final] 
writefile = csv.writer(open('info_combine.csv','w'),quoting=csv.QUOTE_NONE,delimiter='\t')
writefile.writerows(final)

