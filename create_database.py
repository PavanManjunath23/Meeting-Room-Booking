import sqlite3

conn = sqlite3.connect('data.db')
print("Connected to database")
#conn.execute("DROP TABLE administrator")
#conn.execute("DROP TABLE users")
conn.execute('CREATE TABLE administrator (place_name TEXT,pid INT PRIMARY KEY,seat INT,location TEXT,image_name TEXT)')
conn.execute('CREATE TABLE users (cid INTEGER PRIMARY KEY AUTOINCREMENT,place_name TEXT,date DATE,start_time TIME,end_time Time,FOREIGN KEY (place_name) REFERENCES administrator(place_name))')
print("Created table")

conn.execute("INSERT INTO administrator (place_name,pid,seat,location,image_name) values ('ZOLO',36,6,'Mysore','meeting1.jpg')")
conn.execute("INSERT INTO administrator (place_name,pid,seat,location,image_name) values ('ARMANI',39,3,'Delhi','meeting2.jpeg')")
conn.execute("INSERT INTO users (place_name,date,start_time,end_time) values ('ZOLO','2023-01-01','19:00','21:00')")
conn.commit()
conn.close()
