import psycopg2 as db
import csv
import pandas as pd

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

query = "SELECT District, COUNT(Stid) AS Num_of_station FROM Employee GROUP BY District HAVING COUNT(Stid) >= ALL (SELECT COUNT(Stid) FROM Employee GROUP BY District)"
cur.execute(query)

conn.commit()

df1 = pd.read_sql(query, conn)
print(df1.head())