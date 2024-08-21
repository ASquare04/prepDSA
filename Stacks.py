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
