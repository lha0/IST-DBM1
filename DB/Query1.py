import psycopg2 as db
import csv
import pandas as pd

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

query_start = "SELECT Station_start, COUNT(Bid) AS Num_of_bicycle FROM History GROUP BY Station_start HAVING COUNT(Bid) >= ALL (SELECT COUNT(Bid) FROM History GROUP BY Station_start)"
cur.execute(query_start)

query_end = "SELECT Station_end, COUNT(Bid) AS Num_of_bicycle FROM History GROUP BY Station_end HAVING COUNT(Bid) >= ALL (SELECT COUNT(Bid) FROM History GROUP BY Station_end)"
cur.execute(query_end)

conn.commit()

df1 = pd.read_sql(query_start, conn)
df2 = pd.read_sql(query_end, conn)
print(df1.head())
print(df2.head())