import sqlite3
conn = sqlite3.connect('company.db')
print("Open database successfully")

conn.execute('''CREATE TABLE COMPANY
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            ADDRESS        CHAR(50),
            SALARY         REAL);''')
print("Table created successfully")
conn.close()

