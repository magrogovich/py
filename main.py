from random import*
import mysql.connector
import requests

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='toor', host='127.0.0.1', database='cards')

   #Creating a cursor object using the cursor() method
sql1 =f"INSERT INTO card1 (lat, lng, speed, sat, realtime) values ({lat1},{lng1},{speed1},{sat1},now())"
cursor = conn.cursor()

n = int(input("enter number of cards:"))
with open('code.txt','r') as code:
    for i in range(n):
        x = randint(100000000,999999999)
        data = code.read()
        if (data.find(str(x)) == -1):
            with open('code.txt','a') as codes:
                codes.write(f'{x}\n')
                    cursor.execute(sql3)
                    conn.commit()
                    time.sleep(5)