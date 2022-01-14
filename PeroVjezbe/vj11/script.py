import sqlite3

connect = sqlite3.connect('myBase.db')

cursor = connect.cursor()

command1 = """CREATE TABLE IF NOT EXISTS odjeli(odjeliID INTEGER PRIMARY KEY, imeOdjela TEXT)"""

command2 = """CREATE TABLE IF NOT EXISTS zaposlenici(zaposleniciID INTEGER PRIMARY KEY, ime TEXT, prezime TEXT, odjeliID INTEGER, FOREIGN KEY(odjeliID) REFERENCES departments(departmentID))"""

cursor.execute(command1)
cursor.execute(command2)

cursor.execute("INSERT INTO departments VALUES (1, 'Prvi odjel')")
cursor.execute("INSERT INTO departments VALUES (2, 'Drugi odjel')")
cursor.execute("INSERT INTO departments VALUES (3, 'Treci odjel')")

cursor.execute("INSERT INTO zaposlenici VALUES (1, 'Jurica', 'Juric', 1)")
cursor.execute("INSERT INTO zaposlenici VALUES (2, 'Perica', 'Peric', 2)")
cursor.execute("INSERT INTO zaposlenici VALUES (3, 'Marko', 'Maric', 3)")

results = cursor.execute("SELECT * FROM departments")
results = cursor.fetchall()
print(results)

results = cursor.execute("SELECT * FROM zaposlenici")
results = cursor.fetchall()
print(results)