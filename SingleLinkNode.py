class SingleLinkNode:
    def __init__(self,data,nextLink):
        self.data=data
        self.next=nextLink

    def setData(self,data):
        self.data=data
    
    def setNext(self,next):
        self.next=next

    def getNext(self):
        return self.next
    
    def getData(self):
        return self.data
    

