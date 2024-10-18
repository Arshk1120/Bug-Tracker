import sqlite3

conn = sqlite3.connect('bug_tracker.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM bugs")
print(cursor.fetchall())
conn.close()
