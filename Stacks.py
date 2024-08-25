MAX = int(input("Enter size of stack"))
top = -1 
stack = [0] * MAX

def push(x):
    global top
    if top == MAX - 1:
        return "Stack Overflow"
    else:
        top += 1 
        stack[top] = x 
        return None  # Return None to indicate success

def pop():
    global top
    if top == -1:
        return "Stack Underflow"
    else:
        x = stack[top]
        top -= 1 
        return x




#-----------------------------------------------------------------------------------------------------------


class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,data):
        self.items.append(data)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack Is Empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack Is Empty")
        
    def size(self):
        return len(self.items)
    
    def print_stack(self):
        print(self.items)
        

S = Stack()

S.push(5)
S.push(15)
S.push(25)
S.print_stack()
print(S.pop())
S.print_stack()
print(S.peek())
            
