import re
print "###################    MAC ADRESS   #################"
file = open('/home/asm/abc.out','rb').read()
a = re.compile(r'(\s[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2})')
mac1 = re.findall(a,file)
for i in mac1:
    
    print i
print "###################   IPv4    ################ "
file = open('/home/asm/abc.out','rb').read()
b = re.compile(r'/\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]/')
ipv4_val = re.findall(b,file)
for i in ipv4_val:
    print i
