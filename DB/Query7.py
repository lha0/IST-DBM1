import psycopg2 as db
import csv
import pandas as pd

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

query = "SELECT F_bid, (T_distance/T_time)/60 AS Avg_speed_M_per_S FROM (SELECT F_bid, T_distance, T_time from Locations WHERE T_time != 0) AS Locations_1(F_bid, T_distance, T_time) ORDER BY (T_distance/T_time)/60 DESC LIMIT 1"
cur.execute(query)

conn.commit()

df1 = pd.read_sql(query, conn)
print(df1.head())