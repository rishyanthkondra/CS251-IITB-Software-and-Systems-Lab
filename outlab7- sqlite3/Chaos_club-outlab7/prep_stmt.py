import sqlite3
def process(z):
    if z == "":
        return "NULL"
    elif z == "NULL":
        return "NULL"
    elif z == "N/A":
        return "NULL"
    else :
        return "'"+z+"'"

tname = input()
tup = ""
num_col = 0
if tname == "1":
    tname = "TEAM"
    num_col = 2
elif tname == "2":
    tname = "PLAYER"
    num_col = 6
elif tname == "3":
    tname = "MATCH"
    num_col = 15
elif tname == "4":
    tname = "PLAYER_MATCH"
    num_col = 7
elif tname == "5":
    tname = "BALL_BY_BALL"
    num_col = 10

for i in range(num_col):
    tup += process(input())+","


sql_stmt = ("INSERT INTO "+tname+" VALUES "+"{}").format("("+tup[:-1]+")")
#print(sql_stmt)
mydb=sqlite3.connect('ipl.db')
my=mydb.cursor()
my.execute(sql_stmt)
mydb.commit()
mydb.close()