from threading import Timer
import time
import calendar
import json	
#def timeout():
def changedte():
 Time={}
 Time['date']=(str)(dte)
 Time['month']=mth
 Time['year']=yr
 with open("time.txt","w") as tm:
  var=json.dumps(Time)
  tm.write(var) 
 print "Date is updated"
#Zeroisezation of the daily activities 
def changemth():
 Time={}
 Time['date']=(str)(dte)
 Time['month']=mth
 Time['year']=yr
 with open("time.txt","w") as tm:
  var=json.dumps(Time)
  tm.write(var) 
 print "Month is updated"
#Zeroisezation of the monthly activities
def changeyr():
 Time={}
 Time['date']=(str)(dte)
 Time['month']=mth
 Time['year']=yr
 with open("time.txt","w") as tm:
  var=json.dumps(Time)
  tm.write(var) 
 print "year is updated"
#Zeroisezation of the yealy activities

dte=time.strftime("%d")
dte=(int)(dte)+1
mth=time.strftime("%m")
yr=time.strftime("%Y")
print "date =",dte,"month =",mth,"year =",yr
with open("time.txt","r") as t:
 var1=t.read()
 Time=json.loads(var1)
print Time
if((str)(dte)==Time['date']):
 print "day is same"
else:
 changedte()
if((str)(mth)==Time['month']):
 print "month is same"
else:
 changemth()
if((str)(yr)==Time['year']):
 print "year is same"
else:
 changeyr()

