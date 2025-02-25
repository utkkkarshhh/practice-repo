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
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        print(f"Pushed item {item} onto the stack!")

    def pop(self):
        if self.is_empty():
            print(f"Stack is already empty! Nothing to pop!")
        else:
            popped_item = self.top
            self.top = self.top.next
            print(f"Popped item {popped_item.data} from the stack")

    def peek(self):
        return self.top.data if self.top else "Stack is empty!"


my_stack = Stack()

print("Is the stack empty?", my_stack.is_empty())
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print("Is the stack empty?", my_stack.is_empty())
print(my_stack.peek())
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
