import psycopg2 as db
import csv

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Bicycle;") 

cur.execute("""CREATE TABLE Bicycle (
                Bid VARCHAR(30));
			""")

with open('data/Bicycle.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO Bicycle (Bid) VALUES (%s)",
        row
        )

conn.commit()
