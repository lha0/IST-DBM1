import psycopg2 as db
import csv

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

cur.execute("DROP TABLE Employee;") 

cur.execute("""CREATE TABLE Employee (
                Department VARCHAR(30),
                District VARCHAR(30),
                SName VARCHAR(60),
                Stid VARCHAR(30),
                Stid_temp VARCHAR(60)
                );
			""")

with open('data/Employee.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO Employee (Department, District, SName, Stid, Stid_temp) VALUES (%s, %s, %s, %s, %s)",
        row
        )

conn.commit()
