import psycopg2 as db
import csv

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Bicycle_management;") 

cur.execute("""CREATE TABLE Bicycle_management (
                Bid VARCHAR(30),
                Department VARCHAR(30));
			""")

with open('data/Bicycle_management.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO Bicycle_management (Bid, Department) VALUES (%s, %s)",
        row
        )

conn.commit()
