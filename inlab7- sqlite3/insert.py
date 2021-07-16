import csv,sqlite3

mydb = sqlite3.connect('pokedex.db')
curs = mydb.cursor()

with open('pokemon.csv','rt') as poke:
	readdata = csv.DictReader(poke)
	pokemon = [(i['id'], i['identifier'], i['species_id'], i['height'], i['weight'], i['base_experience'], i['order'],i['is_default'])
	for i in readdata]
curs.executemany("INSERT INTO POKEMON (id,identifier,species_id,height,weight,base_experience,'order',is_default) VALUES(?,?,?,?,?,?,?,?);" ,pokemon)

with open('abilities.csv','rt') as abi:
	readdata = csv.DictReader(abi)
	abilities = [(i['id'], i['identifier'], i['generation_id'],i['is_main_series'])
	for i in readdata]
curs.executemany("INSERT INTO ABILITIES (id,identifier,generation_id,is_main_series) VALUES(?,?,?,?);" ,abilities)

with open('pokemon_abilities.csv','rt') as pokabi:
	readdata = csv.DictReader(pokabi)
	pokeabil = [(i['pokemon_id'], i['ability_id'], i['is_hidden'], i['slot']) for i in readdata]
curs.executemany("INSERT INTO POKEMON_ABILITIES (pokemon_id,ability_id,is_hidden,slot) VALUES(?,?,?,?);" ,pokeabil)
mydb.commit()
mydb.close()
