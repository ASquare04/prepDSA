# Print 1 to N using Recursion

def print_numbers(n):
    if n >= 1:
        print_numbers(n - 1)  # Recursive call
        print(n)

n = 5  
print_numbers(n)