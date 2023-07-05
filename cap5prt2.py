
from cap5 import *
clist = Circular()

print(clist.is_empty())  

clist.insert_last(10)
clist.insert_last(20)
clist.insert_first(5)
clist.insert_first(21)
clist.insert_first(22)

print(clist.get_first())  
print(clist)  

clist.delete_first()

print(clist) 

print(clist.search(20))  

clist.step()
print(clist.get_first())  

clist.seek(20)
print(clist.get_first())  