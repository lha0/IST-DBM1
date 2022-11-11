import psycopg2 as db
import csv

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS History;") 

cur.execute("""CREATE TABLE History (
                Bid VARCHAR(30),
                Date_start VARCHAR(30),
                Station_start VARCHAR(60),
                Date_end VARCHAR(30),
                Station_end VARCHAR(30),
                Use_time INT,
                Use_distance FLOAT);
			""")

with open('data/History_random.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO History (Bid, Date_start, Station_start, Date_end, Station_end, Use_time, Use_distance) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        row
        )

conn.commit()
