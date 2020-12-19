import sqlite3
from distutils.util import execute

conn = sqlite3.connect("teste.db")

c = conn.cursor()


def createtable ():
    conn.connect
    new_table = "CREATE TABLE books(id integer primary key AUTOINCREMENT, hq varchar, author text)"
    c.execute(new_table)    
    conn.commit()
    

# insert = "INSERT INTO books values(1,'Chainsaw Man', 'Tatsuki Fujimoto')"
# c.execute(insert)
# conn.commit()

# get_query = "SELECT * FROM hq"
# selected = c.execute(get_query)