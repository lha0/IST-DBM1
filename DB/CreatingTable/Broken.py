import psycopg2 as db
import csv

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Broken;") 

cur.execute("""CREATE TABLE Broken (
                Bid VARCHAR(30),
                Receipt_date VARCHAR(30),
                Broken_part VARCHAR(30),
                primary key(Bid, Receipt_date, Broken_part));
			""")

with open('data/Broken.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO Broken (Bid, Receipt_date, Broken_part) VALUES (%s, %s, %s)",
        row
        )

conn.commit()
