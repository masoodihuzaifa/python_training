#Accessing gmail
import smtplib
import getpass
host = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username = raw_input("gmail")
password=getpass.getpass()
server.login(username,password)
t0 = raw_input("t0")
sub = raw_input("sub")
mes = raw_input("message")
message = "subject:  %s\n%s"%(sub,text)
server.sendmail(username,t0,message)
