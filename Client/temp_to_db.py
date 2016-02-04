
#!/usr/bin/python
#
# Reads all 1Wire sensors and outputs to db
#

import MySQLdb as mdb
import sys

def WriteTempToDB(temperature,name):
	try:
		con = mdb.connect('192.168.10.8','xbmc','xbmc','temperature')
		with con:
			cur = con.cursor()
			cur.execute("insert into temperatures (devicename,curtemp) values ('{0}',{1})".format(name,temperature))
	except:
		print sys.exc_info()
		sys.exit(1)
	finally:
		if con:
			con.close()

def ReadTemperature(sensor):
	try:
		filename = '/sys/bus/w1/devices/'+sensor.strip()+'/w1_slave'
		with open(filename,'r') as fs:
			text = fs.read()
			secondline = text.split('\n')[1]
			temperaturedata = secondline.split(' ')[9]
			WriteTempToDB(int(temperaturedata[2:]),sensor.strip())
	except:
		print sys.exc_info()
		sys.exit(1)
		
with open('/sys/bus/w1/devices/w1_bus_master1/w1_master_slaves','r') as f:
	for line in f:
		ReadTemperature(line)
