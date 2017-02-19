import re
import sys
import mysql.connector
file = open("/home/asm/abc.out")
print(file)
list_of_lines = []
my_list=[]
for line in file:
    res = re.match("----- APmgr info: apmgrinfo -a", line , re.M|re.I)
    if res:
        for line in file:
            list_of_lines.append(line)
            res1=re.match("65 APs are connected", line, re.M|re.I)
            if res1:
                break
print("file is extracted")
for n in list_of_lines:
        if n == "\n":
                print "============================"
aps = []
ap = []
                ap.append(line)
        else:
                ap = "".join(ap)
                aps.append(ap)
                ap = []
print len(aps)
for ap in aps:
        print ap
        print "=============================="
        print ap[8:25]
        print ap[28:43]
sql =""""select * from ACCESSPOINTS"""
print("database is selected")
for ap in aps:
        print ap

~                                                                                                                                                                       
