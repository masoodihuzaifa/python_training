import pexpect
import sys

m = pexpect.spawn('python calculator_with_pexpect.py')
m.logfile_read = sys.stdout
m.expect("\n:")
m.sendline("+")
m.expect("Enter a number: ")
m.sendline("10")
m.expect("Enter a another number: ")
m.sendline("20")
#m.expect("Subject :")
#m.sendline("test")
m.expect("Enter the content. Your last line should be as 'quit'")
#m.sendline("hello")
m.sendline("quit")
#m.expect("test has been send to vaishnavi.gopi6@gmail.com")
m.close()
