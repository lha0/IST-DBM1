import psycopg2 as db
import csv

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Users;") 

cur.execute("""CREATE TABLE Users (
                Age VARCHAR(30),
                Sex VARCHAR(30),
                Types VARCHAR(60), 
                Co2 VARCHAR(30),
                Exercise VARCHAR(30),
                Num_of_use VARCHAR(30));
			""")

with open('data/Users_final.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO Users (Age, Sex, Types, Co2, Exercise, Num_of_use) VALUES (%s, %s, %s, %s, %s, %s)",
        row
        )

conn.commit()
