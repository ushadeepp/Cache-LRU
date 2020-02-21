from Node import *

# Class that stores the cached data in a form of doubly linked list
class CachedDataQueue:
    # Counstructor taking the Initializng the head & tail to Null
    def __init__(self):
        self.head=None
        self.tail=None
    
    # Adding the nodes at head as Recently used should come to first takes O(1) complexity
    def addData(self,nodeRef):
        if(self.head==None):
            nodeRef.setPrev(None)
            nodeRef.setNext(None)
            self.tail=nodeRef
        else:
            nodeRef.setPrev(None)
            nodeRef.setNext(self.head)
            self.head.setPrev(nodeRef)
        self.head=nodeRef
    
    #  To Print Whole list takes iteration through wole list takes O(N)
    def printWholeList(self):
        current=self.head
        while(current!=None):
            print('-------')
            print('current:'+str(current))
            print('Prev:'+str(current.getPrev()))
            print('Key:'+str(current.getKey()))            
            print('Data:'+str(current.getData()))
            print('next:'+str(current.getNext()))
            current=current.getNext()

    # To get the size of linked list iteration through whole list takes O(N) 
    def getSize(self):
        size=0
        current=self.head
        while(current!=None):
            size+=1
            current=current.getNext()        
        return size

    # Geting Data fetched and moving the Node to front of the list as it is Recently Used 
    def fetchData(self,nodeRef):
        if nodeRef!=self.head and nodeRef!=self.tail:
            
            nodeRef.getPrev().setNext(nodeRef.getNext())
            nodeRef.getNext().setPrev(nodeRef.getPrev())
        elif nodeRef==self.head:
            self.head=nodeRef.getNext()
            nodeRef.getNext().setPrev(nodeRef.getPrev())
            # nodeRef.setPrev(None)
        elif nodeRef==self.tail:
            
            self.tail=nodeRef.getPrev()
            nodeRef.getPrev().setNext(nodeRef.getNext())
            print(self.tail)
            # nodeRef.setNext(None)
            
        self.addData(nodeRef)    

          

    def deleteHead(self):
        temp=self.head
        self.head=self.head.getNext()
        self.head.setPrev(None)
        del temp
    
    #  Tail deletion takes O(1) complexity as the prev ref is available and dont need to loop in order to update prev next
    def deleteTail(self):
        cur=self.tail.getPrev()        
        temp=self.tail
        cur.setNext(None)
        self.tail=cur
        del temp
        

    def getTail(self):
        return self.tail
    
