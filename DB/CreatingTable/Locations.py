import psycopg2 as db
import csv

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Locations;") 

cur.execute("""CREATE TABLE Locations (
                F_bid VARCHAR(30),
                F_sid VARCHAR(30),
                T_time INT,
                T_distance FLOAT,
                Num_of_used INT);
			""")

with open('data/Locations.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO Locations (F_bid, F_sid, T_time, T_distance, Num_of_used) VALUES (%s, %s, %s, %s, %s)",
        row
        )

conn.commit()
