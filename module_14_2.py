import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#cursor.execute('DELETE FROM Users WHERE id = ?', ('6',))

# cursor.execute("SELECT * FROM Users WHERE age != ?", ("60",))
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя:{user[1]}|Почта:{user[2]}|Возраст:{user[3]}|Баланс:{user[4]}')

cursor.execute('SELECT COUNT (*) FROM Users')
all_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_balance = cursor.fetchone()[0]

cursor.execute('SELECT AVG(balance) FROM Users')
average_balance = cursor.fetchone()[0]
print(average_balance)

connection.commit()
connection.close()