from SingleLinkNode import *

class LinkedList:
    # Counstructor taking the data and Initializng the headNode
    def __init__(self):        
        self.head=None
        self.tail=None

    # Adding data to end of the list as we are maintaing the Tail it take O(1) else it takes O(N) for iteration to end
    def addData(self,newNode):
        newDataNode=SingleLinkNode(newNode,None)
        if(self.head==None):            
            self.head=newDataNode
            self.tail=newDataNode
        else:
            self.tail.setNext(newDataNode)
            self.tail=newDataNode

    #  To Print Whole list takes iteration through wole list takes O(N)
    def printData(self):
        current=self.head
        while(current!=None):
            print(current.getData())
            current=current.getNext()

    # To get the size of linked list iteration through whole list takes O(N) 
    def getSize(self):
        size=0
        current=self.head
        while(current!=None):
            size+=1
            current=current.getNext()        
        return size

    # Function to search in the list take O(N)
    def search(self,key):
        current=self.head
        while(current!=None):
            if key==current.getData().getKey():
                return current.getData()
            current=current.getNext()
        return None

    #  delete the Node teake O(N) to search 
    def deleteNode(self,data):
        if data==self.head.getData():
            self.deleteHead()        
        else:
            if self.search(data)!=None:
                prev=self.head
                cur=self.head.getNext()
                while cur.getData()!=data:
                    prev=cur
                    cur=cur.getNext()
                prev.setNext(cur.getNext())
                del cur
            

    def deleteHead(self):
        temp=self.head
        self.head=self.head.getNext()
        del temp
    
    def deleteTail(self):
        cur=self.head
        while(cur.getNext()!=self.tail):
            cur=cur.getNext()
        
        temp=self.tail
        cur.setNext(None)
        self.tail=cur
        del temp
