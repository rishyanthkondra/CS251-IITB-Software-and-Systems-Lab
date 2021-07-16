
import sqlite3

mydb = sqlite3.connect('pokedex.db')
curs = mydb.cursor()

curs.execute('''CREATE TABLE POKEMON
         (id INT,
         identifier  TEXT   ,
         species_id INT,
         height INT,
         weight INT,
         base_experience INT,
         'order' INT,
         is_default INT);''')

curs.execute('''CREATE TABLE ABILITIES
         (id INT,
         identifier TEXT,
         generation_id INT,
         is_main_series INT);''')

curs.execute('''CREATE TABLE POKEMON_ABILITIES
         (pokemon_id INT ,
         ability_id INT,
         is_hidden INT,
         slot INT);''')
mydb.commit()
mydb.close()
