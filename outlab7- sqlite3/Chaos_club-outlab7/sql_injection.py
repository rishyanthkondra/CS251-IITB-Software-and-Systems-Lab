import sqlite3
import sys
        
tname = input()
mode = input()
cname = ""
if tname == "1":
    tname = "TEAM"
    cname = "team_name"
elif tname == "2":
    tname = "PLAYER"
    cname = "player_name"
elif tname == "3":
    tname = "MATCH"
    cname = "match_id"

inp = input()

if mode == "0":
    sql_stmt = ("DELETE FROM "+tname+" WHERE {} = {}").format(cname,'"'+inp+'"')
elif mode == "1":
    sql_stmt = ("DELETE FROM "+tname+" WHERE {} = ?").format(cname)
#print(sql_stmt)
mydb=sqlite3.connect('ipl.db')
my=mydb.cursor()
if mode == "0":
    my.execute(sql_stmt)
elif mode == "1":
    my.execute(sql_stmt, (inp, ))
mydb.commit()
mydb.close()
