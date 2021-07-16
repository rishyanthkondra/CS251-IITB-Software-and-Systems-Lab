import sqlite3

mydb = sqlite3.connect('pokedex.db')
curs = mydb.cursor()

pustera =curs.execute('''SELECT POKEMON_ABILITIES.pokemon_id, POKEMON_ABILITIES.ability_id, POKEMON.identifier as pokemon_identifier, ABILITIES.identifier as ability_identifier
	FROM POKEMON_ABILITIES
	INNER JOIN POKEMON ON POKEMON_ABILITIES.pokemon_id = POKEMON.id
	INNER JOIN ABILITIES ON POKEMON_ABILITIES.ability_id = ABILITIES.id;''')
respuesta ={}

for a in pustera:
	respuesta.setdefault(a[2],[]).append(a[3])
for b in respuesta:
	respuesta[b].sort()
respuesta =  sorted(respuesta.items())
for c in respuesta:
	print("%s=[%s]"% (c[0],(','.join(c[1]))))

mydb.commit()
mydb.close()
