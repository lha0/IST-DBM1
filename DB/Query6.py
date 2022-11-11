import psycopg2 as db
import csv
import pandas as pd

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

query = "SELECT F_bid, AVG(T_time) AS Moving_time, AVG(T_distance) AS Moving_distance FROM Locations JOIN Broken on Locations.F_bid = Broken.Bid GROUP BY F_bid ORDER BY Moving_time DESC"
cur.execute(query)

conn.commit()

df1 = pd.read_sql(query, conn)
print(df1.head())