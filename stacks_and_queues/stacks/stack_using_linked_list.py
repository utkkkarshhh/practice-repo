class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None 
        
    def is_empty(self):
        return self.top is None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {item} onto the stack!")
        
    def pop(self):
        if self.is_empty():
            print(f"Stack is empty nothing to pop!")
        else:
            popped_item = self.top.data
            self.top = self.top.next
            print(f"Popped {popped_item} from the stack!")
            
    def peek(self):
        return self.top.data if self.top else "Stack is empty!"
            
            
my_stack = Stack()

print("Is the stack empty?", my_stack.is_empty())
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print("Is the stack empty?", my_stack.is_empty())
my_stack.peek()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.peek()
my_stack.pop()