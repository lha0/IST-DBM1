import psycopg2 as db
import csv
import pandas as pd

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

query1 = "CREATE INDEX Bid_hash ON Locations USING HASH (F_bid);"
cur.execute(query1)

query2 = "CREATE INDEX Bid_b_tree ON Locations(F_bid);"
cur.execute(query2)

conn.commit()

df1 = pd.read_sql(query1, conn)
df2 = pd.read_sql(query2, conn)
print(df1.head())
print(df2.head())