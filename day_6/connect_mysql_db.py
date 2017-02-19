import MySQLdb

db = MySQLdb.connect("localhost","root","asm123","TESTDB" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)
db.close()
