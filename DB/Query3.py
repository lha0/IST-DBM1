import psycopg2 as db
import csv
import pandas as pd

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

query = "SELECT F_sid, COUNT(F_bid) AS Num_of_bicycle FROM Locations GROUP BY F_sid HAVING COUNT(F_bid) >= ALL (SELECT COUNT(F_bid) FROM Locations GROUP BY F_sid)"
cur.execute(query)

conn.commit()

df1 = pd.read_sql(query, conn)
print(df1.head())