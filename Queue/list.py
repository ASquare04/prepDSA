class Queue:
    def __init__(self):
        self.items = []

        
    def is_empty(self):
        return len(self.items)==0
    
    def enqueue(self,data):
        self.items.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Q Underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Q Underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Q Underflow")
        
    def size(self):
        return len(self.items)
        
            
    
    
        
