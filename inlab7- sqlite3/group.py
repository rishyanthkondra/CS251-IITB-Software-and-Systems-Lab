import sqlite3

mydb = sqlite3.connect('pokedex.db')
curs = mydb.cursor()

curs.execute('''SELECT  max(base_experience),species_id FROM POKEMON GROUP BY species_id ORDER BY base_experience DESC LIMIT 3;''')
result = curs.fetchall()

for row in result:
  print(row[0])

mydb.commit()
mydb.close()
