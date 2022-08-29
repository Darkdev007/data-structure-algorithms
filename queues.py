class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        
    
    def print_list(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
            
    def enqueue(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length -= 1
            return temp
        
queue_list = Queue(3)
queue_list.enqueue(2)
print(queue_list.dequeue())
queue_list.print_list()
print(queue_list.dequeue())
queue_list.print_list()
        