mydict = {'name':'huzaif','company':'ASM Technologies','role':'SE','age':25}

#To get contents of Dictonary
print mydict.items()
print mydict
print len(mydict)#length of Dictonary
print "\n"
#to add new item to Dictonary
mydict ['Loc']='Banglore'
print mydict.items()
print len(mydict)
print "\n"
#Updating an Item in Dictonary
mydict ['age']=23
print mydict.items()
print len(mydict)
print "\n"
#Deleting the Item from Dictonary
del mydict['age']
print mydict.items()
print len(mydict)
print "\n"
#To clear the entire Dictonary
mydict.clear()
print mydict.items()
print len(mydict)