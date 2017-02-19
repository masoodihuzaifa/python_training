import pickle
f = open('pp.txt','r')
mylist = pickle.load(f)
mystr = pickle.load(f)
mydict = pickle.load(f)
print mylist
print mystr
print mydict
