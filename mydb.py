import psycopg2

# connection establishment
conn = psycopg2.connect(
database="postgres",
	user='postgres',
	password='06011999',
	host='localhost',
	port= '5432'
)

conn.autocommit = True

# Creating a cursor object
cursor = conn.cursor()

# query to create a database
sql = ''' CREATE database mycompanydb '''

# executing above query
cursor.execute(sql)
print("Database has been created successfully !!")

# Closing the connection
conn.close()
