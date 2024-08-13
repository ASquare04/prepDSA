#Singly Linked List

class Node:
    def __init__(self, item=None,next=None):
        self.item = item
        self.next = next
        
        
class SLL:
    def __init__(self,start=None):
        self.start = start
        
    def is_empty(self):
        return self.start==None
    
    
    
    def at_start(self, data):
        n=Node(data,self.start)
        self.start=n
        
    def at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
            
            
            
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n=Node(data, temp.next)
            temp.next = n
            
            
            
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp = temp.next
            
            
            
        
mylist = SLL()
mylist.at_start(23)
mylist.at_start(32)
mylist.at_last(42)
nodeA = mylist.search(42)
mylist.insert_after(nodeA, 81)
mylist.at_start(312)
mylist.at_last(142)
mylist.print_list()