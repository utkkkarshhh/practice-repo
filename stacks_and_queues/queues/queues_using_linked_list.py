class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{item} has been enqueued!")
            
    def dequeue(self):
        pass