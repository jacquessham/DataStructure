from LinkedList import LinkedList

class ArrayStack:
    def __init__(self):
        self.arr = []

    def push(self, new_elem):
        self.arr.append(new_elem)

    def pop(self):
        if len(self.arr) == 0:
            return None
        return self.arr.pop()

    def peak(self):
        if len(self.arr) == 0:
            return None
        return self.arr[len(self.arr)-1]

    def empty(self):
        if len(self.arr) == 0:
            return True
        return False

    def size(self):
        return len(self.arr)

class LinkStack:
    def __init__(self):
        self.ll = None

    def push(self, new_elem):
        if self.ll is None:
            self.ll = LinkedList(new_elem)
        else:
            self.ll.add_Elem(new_elem)

    def pop(self):
        # If stack is empty
        if self.ll is None: return None
        # If stack has linkedlist but no elem
        if self.ll.getSize() == 0: return None
        # If stack is not empty, get the pos of tail
        tail_int = self.ll.getSize()-1
        last_elem = self.ll.get(tail_int)
        self.ll.remove(tail_int)
        return last_elem

    def peak(self):
        # If stack is empty
        if self.ll is None: return None
        # If stack is not empty, get the pos of tail
        tail_int = self.ll.getSize()-1
        return self.ll.get(tail_int)

    def empty(self):
        # Empty means self.ll is None or self.ll.size() == 0
        if self.ll is None or self.ll.size()==0:
            return True
        return False

