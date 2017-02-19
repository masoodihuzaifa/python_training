import MySQLdb
db = MySQLdb.connect("localhost","root","asm123","TESTDB" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)
db.close()


import MySQLdb
db = MySQLdb.connect("localhost","root","asm123","TESTDB" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS ACCESSPOINTS")
sql = """CREATE TABLE ACCESSPOINTS(
         MACAddress VARCHAR(255),
         IPv4Address VARCHAR(255),
         IPv6Address VARCHAR(255),
         Name VARCHAR(255),
         State VARCHAR(255),
         Tunnel VARCHAR(255),
         Sec_Mode VARCHAR(255),
         Mesh_Role VARCHAR(255),
         PSK VARCHAR(255),
         Timer VARCHAR(255),
         HW_Version VARCHAR(255),
         SW_Version VARCHAR(255),
         Model VARCHAR(255),
         Serial_number VARCHAR(255)
         );"""
cursor.execute(sql)
db.close()

import re
import sys
import mysql.connector
con=None
x=None
results=None
y=None
query=None
class MyClass:
	def __init__(self):
		self.con=mysql.connector.connect(user='root',password='asm123',host='localhost',database='TESTDB')
		print("connection successfull")

		self.x=self.con.cursor(buffered=True)
		self.query="select *from ACCESSPOINTS;"
		self.x.execute(query)
		print results
	def parsing(self):
		fl1=open("/home/asm/abc.out")
		print fl1
		list_of_lines= []
		mylist=[]
		for line in fl1:
		    res = re.match("----- APmgr info: apmgrinfo -a", line , re.M|re.I)
		    if res:
			for line in fl1:
			    list_of_lines.append(line)
			    res1=re.match("65 APs are connected", line, re.M|re.I)
		 	    if res1:
				break
		print("fl1 extracted")
		for n in list_of_lines:
		    	if n == "\n":
				pass
		aps = []
		ap = []
		for line in list_of_lines:
			if line != "\n":
				ap.append(line)
			else:
				ap = "".join(ap)
				aps.append(ap)
				ap = [] 
		print("database selected")
		for ap in aps:
			mac=re.search(r'([0-9a-f]{2}[:]){5}([0-9a-f]{2})',ap,re.I)
			if mac:
				mac=str(mac.group())
				print mac
			ipv4=re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ap,re.I)
			if ipv4:
				ipv4=ipv4.group()
				print ipv4
			ipv6=re.search(r'([0-9a-f]{1,4}:){1,6}:[0-9]{1,2}',ap,re.I)
			if ipv6:
				ipv6=ipv6.group()
				print ipv6
			name=re.search(r'(Name\s.*)',ap,re.I)
			nameval=''	
			if name:
				nmk=str(name.group())	
				if nmk:
					nmk1=nmk.split(':')
					namekey=nmk1[0]
					print namekey		
					nameval=nmk1[1]
					print nameval	
			tse=re.search(r'(Tunnel/Sec Mode.*)',ap,re.I)
			tunval=''
			secval=''
			if tse:	
				tse1=str(tse.group())
				ts1=tse1.split(':')
				tsk=ts1[0]
				tsv=ts1[1]
				tk1=tsk.split('/')
				tunkey=tk1[0]
				seckey=tk1[1]
				ts1=tsv.split('/')		
				tunval=ts1[0]		
				secval=ts1[1]
				print tunkey
				print tunval
				print seckey
				print secval
			sk=re.search(r'(State.*)',ap,re.I)
			stateval=''
			if sk:	
				skstr=str(sk.group())
				if skstr:
					skstr1=skstr.split(' :')
					statekey=skstr1[0]
					print statekey
					stateval=skstr1[1]			
					print stateval
			mk=re.search(r'(Mesh Role.*)',ap,re.I)
			meshval=''
			if mk:
				meshstr=str(mk.group())
				if meshstr:
					meshstr1=meshstr.split(' :')
					meshkey=meshstr1[0]
					print meshkey
			 		meshval=meshstr1[1]
					print meshval
			pk=re.search(R'(PSK)',ap,re.I)
			pskval=''
			if pk:
				pskkey=str(pk.group())
				print pskkey	
			pv=re.search(r'(PSK(.*):(.*))',ap,re.I)
			if pv:	
				s=str(pv.group())
				if s:
					s1=s.split(': ')	
					pskval=s1[1]
				print pskval
			tmk=re.search(r'(Timer)',ap,re.I)
			timerval=''
			if tmk:
				timerkey=str(tmk.group())
				print timerkey
			tv1=re.search(r'(Timer.*)',ap,re.I)
			if tv1:
				t=str(tv1.group())
				if t:
					t1=t.split(': ')
					timerval=t1[1]
				print timerval
			hk=re.search(r'(HW)',ap,re.I)	
			hardval=''
			if hk:
				hardkey=str(hk.group())
				print hardkey
			hv=re.search(r'(\s[0-9]{1,2}.[0-9]{1}.[0-9]{1}.[0-9]{1}\s)',ap,re.I)
			if hv:
				hardval=str(hv.group())
				print hardval
			sk=re.search(r'(SW)',ap,re.I)
			softval=''
			if sk:
				softkey=str(sk.group())
				print softkey
			sv=re.search(r'(HW.*)',ap,re.I)
			if sv:
				s=str(sv.group())
				s1=s.split('/ ')
				softval=s1[1]
				print softval
			mdv=re.search(r'(Model.*)',ap,re.I)
			modelval=''
			serialval=''
			if mdv:	
				s=str(mdv.group())
				ms1=s.split(': ')
				mskey=ms1[0]
				mskey1=mskey.split('/')
				modelkey=mskey1[0]	
				serialkey=mskey1[1]
				mvkey=ms1[1]		
				mv1=mvkey.split('/')
				modelval=mv1[0]	
				serialval=mv1[1]
				print modelkey
				print modelval
				print serialkey
				print serialval
			print mac,ipv4,ipv6,nameval,stateval,tunval,secval,meshval,pskval,timerval,hardval,softval,modelval,serialval	
			self.x.execute("insert into ACCESSPOINTS(MACAddress,IPv4Address,IPv6Address,Name,State,Tunnel,Sec_Mode,Mesh_Role,PSK,Timer,HW_Version,SW_Version,Model,Serial_number) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (mac,ipv4,ipv6,nameval,stateval,tunval,secval,meshval,pskval,timerval,hardval,softval,modelval,serialval) )			
			self.con.commit()
a=MyClass()
a.parsing()
