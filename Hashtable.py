from Node import *
from LinkedList import *
from CachedDataQueue import * 

#  HashTable 
class HashTable:
    
    # cunstrcutor initialize tableSize & cacheMaxSize
    def __init__(self,tableSize,cacheMaxSize):
        self.tableSize=tableSize
        self.cacheMaxSize=cacheMaxSize
        self.table=[]
        for i in range(tableSize):
            self.table.append(LinkedList())
        self.cacheData=CachedDataQueue()
    
    #  considering the keys are only int caliculating the hash of key
    def hashFunc(self,key):
        return key%self.tableSize

    #  Insert data in hashtable
    def insertData(self,key,data):
        if self.cacheData.getSize()==self.cacheMaxSize:
            self.evictLastElement()
        keyHash=self.hashFunc(key)
        node=Node(key,data,None,None)
        self.cacheData.addData(node)
        self.table[keyHash].addData(node)


    #  get data from cache
    def getData(self,key):
        keyHash=self.hashFunc(key)
        li=self.table[keyHash]
        result=li.search(key)
        if(result==None):
            return None
        self.cacheData.fetchData(result)
        return result.getData()
    
    # Delete the last Node
    def evictLastElement(self):
        deletedNode=self.cacheData.getTail()
        keyHash=self.hashFunc(deletedNode.getKey())
        self.table[keyHash].deleteNode(deletedNode)
        self.cacheData.deleteTail()
        


    def printTableAndCacheQueue(self):
        for key in range(self.tableSize):
            print('Key'+str(key)+':   --------------------')
            self.table[key].printData()        
        self.cacheData.printWholeList()

        