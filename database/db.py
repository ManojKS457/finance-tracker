import sqlite3

conn = sqlite3.connect("database/finance.db", check_same_thread=False)
cursor = conn.cursor()