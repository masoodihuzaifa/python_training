import sys

def main():
  print "Hello World"

if __name__ == "__main__":
  main()



#opening a file in read mode
f = open("new.txt", "r")
print "Name of the file: ", f.name
print "Opening mode : ", f.mode

#opening a file in write mode
f = open("new.txt", "w")
print "Name of the file: ", f.name
print "Opening mode : ", f.mode


#closing a file
f.close()

# Opening file and writing into file
f = open("new.txt", "wb")
f.write( "hi.\nHello World!!\n");
f.close()
