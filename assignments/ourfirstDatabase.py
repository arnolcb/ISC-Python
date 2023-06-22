import sqlite3

# Create a database in RAM
db = sqlite3.connect(':memory:')

# Get a cursor object
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)''')


cursor.execute('''DELETE FROM Ages''')

# Insert users
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Stefany', 24)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Olubanke', 23)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Heyden', 17)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Rai', 24)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Aronas', 32)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Kisha', 19)''')

#Select user
cursor.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X''')

#retrieve the first row
user1 = cursor.fetchone()
#Print the first column retrieved(user's name)
print("The first row in the resulting record set : "+user1[0])

#Commit changes into database
db.commit()
#Close database
db.close()