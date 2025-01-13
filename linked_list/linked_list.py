class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    def append(self, data): #Add in the end
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def prepend(self, data): #Add at the beginning
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def delete(self, data): #Delete with the data 
        if self.is_empty():
            print("Linked List is empty!")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data!= data:
            current = current.next
        
        
    def delete_starting(self): #Delete the starting element
        pass
    
    def delete_ending(self): #Delete the ending element
        pass
    
    def search(self, data): #Search the given element in the linked list
        pass
    
    def display(self): #Display the entire linked list
        pass