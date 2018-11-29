import sqlite3

data_base = sqlite3.connect(database="db_password")
cursor = data_base.cursor()
cursor.execute('''CREATE TABLE resources (
                   id INTEGER PRIMARY KEY,
                   name_resource VARCHAR(150))''')

data_base.commit()




data_base.close()