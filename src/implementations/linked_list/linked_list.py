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
    
    def delete(self, data):
        if not self.head:
            print("Linked List is empty!")
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if not current.next:
            print(f"Data {data} not found in the linked list.")
            return

        current.next = current.next.next
        
        
    def delete_starting(self):
        if not self.head:
            print("The list is empty, nothing to delete!")
            return

        self.head = self.head.next
    
    def delete_ending(self): #Delete the ending element
        if not self.head:
            print("The list is empty, nothing to delete")
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next and current.next.next:
            current = current.next

        current.next = None

    
    def search(self, data): #Search the given element in the linked list
        if not self.head:
            print("Linked list is empty, nothing to find!")

        current = self.head
        position = 0
        while current:
            if current.data == data:
                print(f"{data} found at position {position}")
                return
            current = current.next
            position += 1
        print(f"{data} not found in the linked list!")

    
    def display(self): #Display the entire linked list
        current = self.head
        if not current:
            print("The linked list is empty.")
            return
        while current:
            print(current.data, end=" -> " if current.next else " -> NULL \n")
            current = current.next

ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)

ll.display()
ll.delete_starting()
ll.delete_ending()
ll.search(10)
ll.search(30)
ll.search(60)
ll.search(40)
ll.display()
