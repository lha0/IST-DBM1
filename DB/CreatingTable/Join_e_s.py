import psycopg2 as db
import csv

conn_string="dbname='python_dataengineering' host='127.0.0.1' user='postgres' password='data'"
conn=db.connect(conn_string)
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS new_Station;")

query1 = "SELECT * FROM employee"
query2 = "SELECT * FROM Station_temp"
cur.execute(query1)
cur.execute(query2)

query3 = "SELECT Station_temp.Stid, Station_temp.Sname, Station_temp.Addr, Station_temp.District, Station_temp.Location_x, Station_temp.Location_y, Station_temp.Install_day, Employee.Department INTO new_Station FROM Station_temp JOIN Employee ON Station_temp.Stid = Employee.Stid"
cur.execute(query3)
conn.commit()

f = open('fromdb.csv', 'w')
cur.copy_to(f, 'new_Station', sep=",")
f.close()
