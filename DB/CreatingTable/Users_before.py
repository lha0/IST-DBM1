import psycopg2 as db
import csv

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Users_before;") 

cur.execute("""CREATE TABLE Users_before (
                Age VARCHAR(30),
                Sex VARCHAR(30),
                Types VARCHAR(60), 
                Co2 FLOAT,
                Exercise FLOAT,
                Num_of_use INT);
			""")

with open('data/Users.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO Users_before (Age, Sex, Types, Co2, Exercise, Num_of_use) VALUES (%s, %s, %s, %s, %s, %s)",
        row
        )

conn.commit()
