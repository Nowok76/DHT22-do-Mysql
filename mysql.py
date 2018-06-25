#!/usr/bin/python

import serial
import MySQLdb
import time
from datetime import datetime

while True:
	db = MySQLdb.connect("localhost","user","password","basename" )
	cursor = db.cursor()

	ser = serial.Serial('/dev/ttyACM0', 9600, 8)
	odczyt = (ser.readline().strip('\n'))
	linia = odczyt.split('\n')
	wartosc = linia[0].split(';')


	t = wartosc[0]
	h = wartosc[1]
	d = wartosc[2]
	c = wartosc[3]
	r = wartosc[4]
	p = wartosc[5]


	sql = "INSERT INTO sensors (Data,Temp,Hum,DefPoint,Clouds,Rain,Presurre) VALUES ('%s', %s, %s, %s, %s, %s, %s);" % (str(datetime.now()), t, h, d, c, r, p)
	cursor.execute(sql)
	db.commit()
	db.close()
	time.sleep(600)

