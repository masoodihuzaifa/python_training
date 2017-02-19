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
