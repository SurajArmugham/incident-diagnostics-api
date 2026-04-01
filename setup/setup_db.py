import sqlite3

conn = sqlite3.connect("../database/test.db")
conn.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER)")
conn.close()

print("DB setup complete")