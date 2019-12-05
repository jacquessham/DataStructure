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