import json
my_li=[1,2,3,4,5]
my_dict={'name':'masood'}
my_str='asm technology'
f=open('b.txt','w')
json.dump(my_li,f)
json.dump(my_dict,f)
print my_li
print my_dict
print my_str
f.close()
