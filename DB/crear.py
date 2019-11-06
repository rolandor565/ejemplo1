import sqlite3

con = sqlite3.connect('Practicas.db')

cursor = con.cursor()

cursor.execute("INSERT INTO personas VALUES('Daniela','Rodriguez','Martinez',243)")

con.commit()

con.close