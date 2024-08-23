class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
        
class CLL:
    def __init__(self,last=None):
        self.last = last
    def is_empty(self):
        return self.last==None
    
    def at_start(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
    
    def at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n
              
            
        
