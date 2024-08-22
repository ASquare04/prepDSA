class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
        
class CLL:
    def __init__(self,last=None):
        self.last = last
    def is_empty(self):
        return self.last==None
