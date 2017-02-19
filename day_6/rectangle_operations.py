class Rectangle:
 cnt = 0
 def __init__(self,x,y) :
   self.len=x
   self.wid=y
   Rectangle.cnt=Rectangle.cnt+1
 def __str__(self):
    return 'Rectangle({0},{1})'.format(self.len,self.wid)
 def __add__(self,other):
    return Rectangle(self.len+other.len,self.wid+other.wid)
 def __eq__(self,other):
    return Rectangle(self.len==other.len,self.wid==other.wid)
 def area(self):
    return self.len * self.wid
 def perimeter(self):
    return 2 * self.len
 def issquare(self):
    if self.len == self.wid:
     return True
 @staticmethod
 def getcount():
   return Rectangle.cnt
R=Rectangle(3,4)
print R
a=R.area()
print "Area:",a
b=R.perimeter()
print "Perimeter:",b
if R.issquare():
   print "Square"
else:
   print "Not Square"
R1=Rectangle(4,5)
R2=Rectangle(1,1)
R3=R1+R2
print "R3:",R3
a=R3.area()
print "Area:",a
"gmaill.com" 44 lines, 916 characters
