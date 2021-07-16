import sqlite3

mydb = sqlite3.connect('pokedex.db')
curs = mydb.cursor()

curs.execute('''DELETE FROM POKEMON WHERE identifier like 'rogue%';''')

mydb.commit()
mydb.close()
