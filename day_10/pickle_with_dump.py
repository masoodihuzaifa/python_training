import pickle
my_li=[1,2,3,4,5]
my_dict={'name':'masood'}
my_str='asm technology'
f=open('a.txt','w')
pickle.dump(my_li,f)
pickle.dump(my_dict,f)
print my_li
print my_dict
print my_str
f.close()
