class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
        
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    