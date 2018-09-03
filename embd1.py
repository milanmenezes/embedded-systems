
import datetime as d
import time

data=[1,2,3,4]
f=open("log.txt","a")

def access_log(id):
	f.write(str(id)+": "+str(d.datetime.now())+'\n')

def door_open():
	id=int(raw_input())
	if id in data:
		access_log(id)
		print "Door Open"
		print "Door Closed"
		return True
	return False

def alarm():
	print "Alarm Started\nSleeping for 5 seconds"
	time.sleep(5)
		
count=0
while True:
	print "waiting for fingerprint"
	if(not door_open()):
		f.write("unauthorized: "+str(d.datetime.now()))
		print "Door Closed"
		count+=1
	if count==5:
		alarm()
		count=0
		
