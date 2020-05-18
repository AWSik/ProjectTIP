import MySQLdb


conn = MySQLdb.connect('localhost', 'username', 'password', 'table_name')
cursor = conn.cursor()

cursor.execute("SELECT * FROM table_name")

# Получаем данные.
row = cursor.fetchone()
print(row)

# Разрываем подключение.
conn.close()
