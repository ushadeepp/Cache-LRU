class Node:
    def __init__(self,key,data,prev,next):
        self.key=key
        self.data=data
        self.next=next
        self.prev=prev

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def getKey(self):
        return self.key
    
    def getPrev(self):
        return self.prev

    def setNext(self,new_next):
        self.next=new_next
    
    def setPrev(self,new_prev):
        self.prev=new_prev


