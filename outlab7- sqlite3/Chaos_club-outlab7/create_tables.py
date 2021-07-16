import sqlite3
mydb=sqlite3.connect('ipl.db')
my=mydb.cursor()

my.execute('''CREATE TABLE TEAM (team_id INT PRIMARY KEY NOT NULL,
	team_name TEXT NOT NULL)''')

my.execute('''CREATE TABLE PLAYER (player_id INT PRIMARY KEY NOT NULL,
player_name TEXT NOT NULL,
dob TIMESTAMP NOT NULL,
batting_hand TEXT NOT NULL,
bowling_skill TEXT ,--is it okay to not keep anything??NULL
country_name TEXT NOT NULL)''')

my.execute('''CREATE TABLE MATCH (match_id INT PRIMARY KEY NOT NULL,
season_year INT NOT NULL,
team1 int NOT NULL,
team2 int NOT NULL,
battedfirst INT ,--is it okay to not keep anything??NULL
battedsecond INT ,
venue_name TEXT ,--is it okay to not keep anything??NULL
city_name TEXT NOT NULL,
country_name TEXT NOT NULL,
toss_winner INT ,
match_winner INT, --is it okay to not keep anything??NULL
toss_name text ,
win_type TEXT ,
man_of_match INT ,
win_margin INT,
FOREIGN KEY(team1) REFERENCES TEAM(team_id),
FOREIGN KEY(team2) REFERENCES TEAM(team_id),
FOREIGN KEY(battedfirst) REFERENCES TEAM(team_id),
FOREIGN KEY(battedsecond) REFERENCES TEAM(team_id) )''')


my.execute('''CREATE TABLE PLAYER_MATCH (playermatch_key BIGINT PRIMARY KEY NOT NULL,
match_id INT,
player_id INT ,
batting_hand TEXT NOT NULL,
bowling_skill TEXT ,--is it okay to not keep anything??NULL
role_desc TEXT NOT NULL,
team_id INT,
FOREIGN KEY (team_id) REFERENCES TEAM(team_id),
FOREIGN KEY (player_id) REFERENCES PLAYER(player_id),
FOREIGN KEY (match_id) REFERENCES MATCH(match_id) )''')

my.execute('''CREATE TABLE BALL_BY_BALL (match_id INT NOT NULL,
innings_no INT,
over_id INT,
ball_id INT,
striker_batting_position INT ,
runs_scored INT,
extra_runs INT,
out_type TEXT NOT NULL,
striker INT NOT NULL,
non_striker INT NOT NULL,
bowler INT NOT NULL,
FOREIGN KEY (match_id) REFERENCES MATCH(match_id),
FOREIGN KEY (striker) REFERENCES PLAYER(player_id),
FOREIGN KEY (non_striker) REFERENCES PLAYER(player_id),
FOREIGN KEY (bowler) REFERENCES PLAYER(player_id),
PRIMARY KEY (match_id, innings_no, over_id,ball_id) )''')
mydb.commit()
mydb.close()





















