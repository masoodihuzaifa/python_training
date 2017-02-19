import re
print "###################    MAC ADRESS   #################"
file = open('/home/asm/abc.out','rb').read()
a = re.compile(r'(\s[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2})')
mac1 = re.findall(a,file)
print a
for i in mac1:    
    print i
    
print "###################   IPv4    ################ "
file = open('/home/asm/abc.out','rb').read()
b = re.compile(r'/\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]/')
ipv4_val = re.findall(b,file)
print b
for i in ipv4_val:
    print i

print "#############     IPv6    ###################"
file = open('/home/asm/abc.out','rb').read()
c = re.compile(r'[A-Za-z0-9]{1,4}::[0-9]{1}')
ipv6_val = re.findall(c,file)
print c
for i in ipv6_val:
    print i
    
print "################   Name   ################"
file = open('/home/asm/abc.out','rb').read()
name = re.compile(r'\s*Name\s*:\s*(.*)')
name1 = re.findall(name,file)
print name
for a in name1:
	ss = a.split(":")
	print ss[0]

    
print "############    Tunnel    ##################"
file = open('/home/asm/abc.out','rb').read()
tunn = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)')
tunnal = re.findall(tun,file)
for a in tunnal:
	ss = a.split("/")
	print ss[0]
    
print "#############    State   ##################"
file = open('/home/asm/abc.out','rb').read()
state = re.compile(r'\s*State\s*:\s*(.*)')
state1 = re.findall(state,file)
print state1
for a in state1:
	ss = a.split("/")
	print ss[0]
    
print "###########  Sec Mode  ##################"
file = open('/home/asm/abc.out','rb').read()
mode = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)')
sec = re.findall(mode,file)
for a in sec:
	ss = a.split("/")
	print ss[1]

print "################ Mesh Role #############"
le = open('/home/asm/abc.out','rb').read()
mesh = re.compile(r'\s*Mesh Role\s*:\s*(.*)')
print mesh
mesh1 = re.findall(mesh,file)
for a in mesh1:
	ss = a.split(":")
	print ss[0]

print "# PSK #"
file = open('/home/asm/abc.out','rb').read()
psk = re.compile(r'\s*PSK\s*:\s*(.*)')
print psk
psk1 = re.findall(psk,file)
for a in psk1:
	ss = a.split(":")
	print ss[0]

print "# Timer #"
file = open('/home/asm/abc.out','rb').read()
time = re.compile(r'\s*Timer\s*:\s*(.*)')
print time
timer = re.findall(time,file)
for a in timer:
	ss = a.split(":")
	print ss[0]

print "# HW Version #"
file = open('/home/asm/abc.out','rb').read()
hwv = re.compile(r'\s*HW/SW Version\s*:\s*(.*)')
print hwv
hwver = re.findall(hwv,file)
for a in hwver:
	ss = a.split("/")
	print ss[0] 

print "# SW Version $"
file = open('/home/asm/abc.out','rb').read()
swv = re.compile(r'\s*HW/SW Version\s*:\s*(.*)')
print swv
swver = re.findall(swv,file)
for a in swver:
	ss = a.split("/")
	print sse[1] 

print "# Model #"
file = open('/home/asm/abc.out','rb').read()
mod = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)')
print mod
modelmod = re.findall(mod,file)
for a in modelmod:
	ss = a.split("/")
	print ss[0]

print "# Serial Num #"
file = open('/home/asm/abc.out','rb').read()
ser = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)')
print ser
sernum = re.findall(ser,file)
for a in sernum:
	x = a.split("/")
	print x[1]

if len(mac1)==len(ipv4_val)==len(swver)==len(hwver)==len(name1)==len(state1)==len(tunnal)==len(sec)==len(mesh1)==len(psk1)==len(timer)==len(modelmod)==len(sernum)==len(ipv6_val):
            for i in range(len(mac1)):
                        cursor.execute("""INSERT INTO ACCESSPOINTS(Name,MACAddress,IPV4Address,SW_Version,HW_Version,State,Tunnel,Sec_Mode,Mesh_Role,PSK,Timer,Model,Serial_number,IPv6Address)
                         VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');""" % (name1[i],mac1[i],ipv4_val[i][1:-1],swver[i][11:23],hwver[i],state1[i],tunnal[i],sec[i][15:18],mesh1[i],psk1[i],timer[i],modelmod[i],sernum[i][9:21],ipv6_val[i]))

try:
    db.commit()
except:
    db.rollback()
    db.close()
