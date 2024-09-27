import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# # Query all data with condition
# cursor.execute("SELECT * FROM events WHERE date='2042.02.28'")
# rows = cursor.fetchall()
# print(rows)

# # Query certain column of data with condition
# cursor.execute("SELECT band, date FROM events WHERE date='2042.02.28'")
# rows = cursor.fetchall()
# print(rows)

# # Insert new rows to data 
# new_rows = [('Cats band', 'Cat city', '2042.02.25'), 
#             ('Dogs band', 'Dog city', '2042.02.24')]
# cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
# connection.commit()

# # Query all data
# cursor.execute("SELECT * FROM events")
# rows = cursor.fetchall()
# print(rows)

# # Delete database
# cursor.execute("DROP TABLE events")
# rows = cursor.fetchall()
# print(rows)

# Create events Table
cursor.execute("CREATE TABLE events('band', 'city', 'date')")
