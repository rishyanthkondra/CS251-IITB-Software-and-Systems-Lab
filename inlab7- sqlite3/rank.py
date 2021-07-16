import sqlite3

mydb = sqlite3.connect('pokedex.db')
curs = mydb.cursor()

curs.execute('''SELECT  identifier FROM POKEMON ORDER BY base_experience DESC LIMIT 3;''')
result = curs.fetchall()

for row in result:
  print(row[0])

mydb.commit()
mydb.close()