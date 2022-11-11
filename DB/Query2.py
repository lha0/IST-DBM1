import psycopg2 as db
import csv
import pandas as pd

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

query = "SELECT F_bid, Num_of_used,T_time,T_distance FROM Locations WHERE Num_of_used = (SELECT MAX(Num_of_used) from Locations)"
cur.execute(query)

conn.commit()

df1 = pd.read_sql(query, conn)
print(df1.head())