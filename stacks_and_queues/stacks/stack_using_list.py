class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
        print(f"{data} has been added onto the stack!")
    
    def pop(self):
        if self.is_empty():
            print(f"Stack is empty, nothing to pop!")
            return None
        item = self.stack.pop()
        print(f"{item} has been popped from the stack!")
        return None
        
    
    def is_empty(self):
        return len(self.stack) == 0
    
my_stack = Stack()
print(f"Is the stack empty?", my_stack.is_empty())
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(f"Is the stack empty?", my_stack.is_empty())
my_stack.pop()
my_stack.pop()
my_stack.pop()

my_stack.pop()