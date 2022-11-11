import psycopg2 as db
import csv

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Station;") 

cur.execute("""CREATE TABLE Station (
                Stid VARCHAR(30),
                Sname VARCHAR(60),
                Addr VARCHAR(90),
                District VARCHAR(60),
                Location_x VARCHAR(60),
                Location_y VARCHAR(60),
                Install_day VARCHAR(60),
                Department VARCHAR(30)
                );
			""")

with open('data/Station.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO Station (Stid, Sname, Addr, District, Location_x, Location_y, Install_day, Department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        row
        )

conn.commit()
