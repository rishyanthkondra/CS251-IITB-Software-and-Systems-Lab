import sqlite3
from operator import itemgetter
conn=sqlite3.connect('ipl.db')
c=conn.cursor()
var = c.execute('''SELECT BALL_BY_BALL.striker,PLAYER.player_name,count(*)*1.0/(count(distinct match_id)*1.0)
                   FROM (BALL_BY_BALL INNER JOIN PLAYER ON BALL_BY_BALL.striker = PLAYER.player_id) 
                   GROUP BY BALL_BY_BALL.striker''')
answer=[]                 
for row in var:
	answer.append([row[0],row[1],row[2]])
answer.sort(key=itemgetter(2),reverse=True)
for i in range(len(answer)):
	if i < 10 or answer[i][2] == answer[9][2]:
		print(str(answer[i][0])+","+answer[i][1]+","+str(answer[i][2]))
conn.commit()
conn.close()