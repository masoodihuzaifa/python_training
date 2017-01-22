import sys

def main():
  print sys.argv

if __name__ == "__main__":
  main()

# Deleteting file
import os

os.remove("new1.txt")


#creating a new directory
import os

os.mkdir("hello")

#getting the current working directory
import os

os.getcwd()


#Remove directory
import os

os.rmdir( "hello"  )
