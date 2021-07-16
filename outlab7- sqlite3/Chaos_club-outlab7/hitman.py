import sqlite3
from operator import itemgetter
conn=sqlite3.connect('ipl.db')
c=conn.cursor()
var = c.execute('''SELECT BALL_BY_BALL.striker,
	PLAYER.player_name,
	sum(BALL_BY_BALL.runs_scored/6),
	count(*),
	sum(BALL_BY_BALL.runs_scored/6)*1.0/(count(*)*1.0) 
	FROM (BALL_BY_BALL INNER JOIN PLAYER ON BALL_BY_BALL.striker = PLAYER.player_id)
	GROUP BY BALL_BY_BALL.striker''')
answer=[]                 
for row in var:
	answer.append([row[0],row[1],row[2],row[3],row[4]])
answer.sort(key=itemgetter(4),reverse=True)
for i in range(len(answer)):
	print(str(answer[i][0])+","+answer[i][1]+","+str(answer[i][2])+","+str(answer[i][3])+","+str(answer[i][4]))
conn.commit()
conn.close()
