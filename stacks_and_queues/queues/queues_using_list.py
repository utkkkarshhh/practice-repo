class Queue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} has been enqueued!")
    
    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued {item} from the queue!")
            return
        print(f"Queue is empty, nothing to dequeue!")
        
    def front(self):
        if not self.is_empty():
            item = self.queue[0]
            print(f"{item} is in the front!")
            return
        print(f"Queue is empty, nothing in front!")
        
        
queue = Queue()

print("Is the queue empty?", queue.is_empty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.front()
print("Queue size:", queue.size())

queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.front()
print("Queue size:", queue.size())
