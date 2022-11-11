import psycopg2 as db
import csv
import pandas as pd

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

query1 = "SELECT F_bid FROM Locations WHERE T_time > 60 AND Num_of_used = 4"
cur.execute(query1)

query2 = "SELECT Co2, Exercise FROM Users WHERE Age = '30대' AND Sex = 'F' AND Types = '정기'"
cur.execute(query2)

conn.commit()

df1 = pd.read_sql(query1, conn)
print(df1.head())

df2 = pd.read_sql(query2, conn)
print(df2.head())