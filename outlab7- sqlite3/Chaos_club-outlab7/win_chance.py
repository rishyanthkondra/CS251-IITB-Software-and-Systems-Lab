import sqlite3

mydb=sqlite3.connect('ipl.db')
my=mydb.cursor()

denomi = my.execute('''SELECT COUNT(match_id) FROM MATCH WHERE battedfirst IS NOT
NULL''')
denomi = int(denomi.fetchone()[0])
bf1 = my.execute('''SELECT COUNT(match_id) FROM MATCH WHERE battedfirst =
match_winner AND battedfirst is NOT NULL''')
bf1 = int(bf1.fetchone()[0])
bf2 = my.execute('''SELECT COUNT(match_id) FROM MATCH WHERE battedsecond =
match_winner AND battedfirst is NOT NULL''')
bf2 = int(bf2.fetchone()[0])
print(round(bf1/denomi,3))
print(round(bf2/denomi,3))
mydb.commit()
mydb.close()

