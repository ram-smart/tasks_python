import sqlite3

data_base = sqlite3.connect(database="db_password.db")
cursor = data_base.cursor()
cursor.execute('''CREATE TABLE COMMON_TABLE
(ID INT PRIMARY KEY NOT NULL,
NAME_SITE TEXT NOT NULL,
ADDRESS_SITE TEXT NOT NULL);''')

data_base.commit()

cursor.execute('''INSERT INTO COMMON_TABLE (ID, NAME_SITE, ADDRESS_SITE) \
     VALUES(1, 'ПСБанк-брокер', 'https://ib.psbank.ru/')''');

data_base.close()

