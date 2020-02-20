from LRUCache import *


h1=LRUCache(4,4)

h1.insertData(11,'hey11')
h1.insertData(10,'hey10')
h1.insertData(12,'hey12')
h1.insertData(16,'hey16')
h1.insertData(5,'hey10')



re=h1.getData(12)
# re=h1.getData(10)

print('result')
print(re)


h1.printTableAndCacheQueue()
