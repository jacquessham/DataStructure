from Link import Link

class LinkedList:
    def __init__(self, elem=None):
        # Top has to be Node object
        self.top = Link(elem)
        self.size = 1

    def add_Elem(self, elem):
        temp = self.top
        # Loop until the last node
        while temp.getNext() is not None:
            temp = temp.getNext()
        temp.setNext(Link(elem))
        self.size += 1

    def add_Elem_pos(self, pos, elem):
        # Stop if pos is greater than the linkedlist size
        if pos > self.size: return None
        new_node = Link(elem)
        # If Add node at top
        if pos == 0:
            new_node.setNext(self.top)
            self.top = new_node
        temp = self.top
        it = 0
        # Loop until the previous node of pos
        while temp.getNext() is not None and it < pos:
            if it+1 == pos: # If the next node is pos
                last_node = temp
                next_node = temp.getNext()
                new_node.setNext(next_node)
                last_node.setNext(new_node)
                self.size += 1
                return
            temp = temp.getNext()
            it += 1
        # Add node at tail
        if it+1 == pos:
            temp.setNext(new_node)
            self.size += 1

    def remove(self, pos):
        # Stop if pos is greater than the linkedlist size
        if pos > self.size: return
        # Remove the top
        if pos == 0:
            if self.top.getNext() is not None:
                self.top = self.top.getNext()
            else:
                self.top = None
            self.size -= 1
            # Once is done, return
            return
        temp = self.top
        it = 0
        # Loop until the previous node of pos
        while temp.getNext() is not None and it < pos:
            if it+1 == pos:
                # If this is the tail
                if temp.getNext() is None:
                    temp.setNext(None)
                else:
                    # If this is not tail; If the next node is node is fine
                    temp.setNext(temp.getNext().getNext())
                # Once the operation is done, -1 on size
                self.size -= 1
                return
            temp = temp.getNext()
            it += 1

    def get(self, pos):
        # If linkedlist is empty
        if self.size == 0: return None
        if pos > self.size: return None
        temp = self.top
        it = 0
        while temp.getNext() is not None and it < pos:
            temp = temp.getNext()
            it += 1
        return temp.elem

    def getSize(self) -> int:
        return self.size

    def printList(self):
        # Helper function to print the whole linkedlist
        temp = self.top
        if temp is None:
        	print('This is Empty')
        	return
        print(temp.getElem())
        while temp.getNext() is not None:
            temp = temp.getNext()
            print(temp.getElem())
