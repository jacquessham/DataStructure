from LinkedList import LinkedList

class ArrayQueue:
    def __init__(self):
        self.arr = []
        self.head = 0
        self.tail = 0

    def enqueue(self, new_elem):
        self.arr.append(new_elem)
        self.tail += 1

    def dequeue(self):
        # Edge case: When arr has nothing
        if len(self.arr) == 0:
            return None
        item = self.arr[self.head]
        self.head += 1
        return item

    def empty(self):
        if (self.head==self.tail):
            return True
        return False

class LinkQueue:
    def __init__(self):
        self.ll = None

    def enqueue(self, new_elem):
        if self.ll is None:
            self.ll = LinkedList(new_elem)
        else:
            self.ll.add_Elem(new_elem)

    def dequeue(self):
        # If queue is empty
        if self.ll is None: return None
        # If queue has linkedlist but no elem
        if self.ll.getSize() == 0: return None  
        first_elem = self.ll.get(0)
        self.ll.remove(0)
        return first_elem

    def empty(self):
        if self.ll is None or self.ll.size()==0:
            return True
        return False        
