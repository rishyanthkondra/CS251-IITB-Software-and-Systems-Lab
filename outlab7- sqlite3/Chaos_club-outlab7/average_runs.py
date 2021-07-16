import sqlite3,pandas
mydb=sqlite3.connect('ipl.db')
my=mydb.cursor()


A=my.execute('''SELECT a.venue_name, sum(b.runs_scored)*1.0/count(distinct b.match_id)*1.0 FROM MATCH a 
	INNER JOIN BALL_BY_BALL b ON b.match_id=a.match_id  GROUP BY a.venue_name''')
lis=sorted(A,key = lambda x: x[1],reverse= True)
for i in range(0,len(lis)):
	print("{},{}".format(lis[i][0],lis[i][1]))
mydb.commit()
mydb.close()
