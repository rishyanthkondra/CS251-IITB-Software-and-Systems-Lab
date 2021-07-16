import sqlite3

mydb = sqlite3.connect('pokedex.db')
curs = mydb.cursor()

curs.execute('''UPDATE ABILITIES SET generation_id=8 WHERE is_main_series=0''')

mydb.commit()
mydb.close()