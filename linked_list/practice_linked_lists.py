class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def get_size(self):
        print(f"Current Size of Linked List is: {self.size}")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def insert_at_a_position(self, data, position):
        if position < 0 or position > self.size:
            raise ValueError("Invalid Position")
        if position == 0:
            self.insert_at_beginning(data)
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def delete_at_beginning(self):
        if self.is_empty():
            raise ValueError("List is Empty!")
        self.head = self.head.next
        self.size -= 1

    def delete_at_end(self):
        if self.is_empty():
            raise ValueError("List is Empty!")
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        self.size -= 1

    def delete_at_position(self, position):
        if self.is_empty():
            raise ValueError("List is Empty")
        if position < 0 and postion > self.size:
            raise ValueError("List is Empty")
        if position == 0:
            self.delete_at_beginning()
            return
        current = self.head
        for _ in range(position - 1):
            current = current.next
        current.next = current.next.next
        self.size -= 1

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        print(f"No {data} found in this list!")
        return -1

    def display(self):
        current = self.head
        if not current:
            print("List is empty!")
            return
        while current:
            print(current.data, end=" -> " if current.next else " -> NULL \n")
            current = current.next

    def display_with_index(self):
        current = self.head
        index = 0
        while current:
            print(f"[{current.data}|{index}]", end=" -> " if current.next else " -> NULL \n")
            current = current.next
            index += 1


    def reverse(self):
        prev = None
        current  = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def reverse_recursive(self, head=None):
        if head is None:
            head = self.head

        if not head or not head.next:
            self.head = head
            return head

        new_head = self.reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def detect_cycle(self):
        if not self.head or not self.head.next:
            return False

        slow = fast = self.new_head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def get_middle_node(self):
        if not self.head:
            return None
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.Data

    def merge_sorted_lists(self, other_list):
        pass

def test_linked_list():
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.display_with_index()
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    ll.insert_at_end(60)
    ll.display_with_index()
    ll.get_size()
    ll.insert_at_a_position(10, 4)
    ll.display_with_index()

    ll.delete_at_beginning()
    ll.delete_at_end()
    ll.display_with_index()
    ll.get_size()

    ll.delete_at_position(3)
    ll.display()
    ll.get_size()

    ll.reverse_recursive()
    ll.display()
    ll.reverse()
    ll.display()


if __name__ == "__main__":
    test_linked_list()
