# Bases de datos #

## SQLite ##

	import sqlite3
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	c.execute('''
		CREATE TABLE player
			(
			name text,
			max_life int,
			current_life int,
			)
		''')
	conn.commit()
	conn.close()
	

	def dict_factory(cursor, row):
    	d = {}
    	for idx, col in enumerate(cursor.description):
        	d[col[0]] = row[idx]
    	return d
	conn.row_factory = dict_factory

## PostgreSQL ## 

	import psycopg2
	conn = psycopg2.connect("dbname=test user=postgres")
	cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
	cur.execute('''
    CREATE TABLE player
        (
        id serial PRIMARY KEY,
				name varchar,
        max_life integer,
        current_life integer,
        );
    ''')
	conn.commit()
	cur.close()
	conn.close()

	
## Mongo ## 

	from pymongo import Connection
	connection = Connection()
	db = connection.dbname
	collection = db.collection


## SQLAlchemy ## 

<http://docs.sqlalchemy.org/en/latest/orm/tutorial.html>

