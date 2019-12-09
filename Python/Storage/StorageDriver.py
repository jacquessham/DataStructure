import Stack
import Queue
import LinkedList


# Stack
print('Array Stack')
stack_arr = Stack.ArrayStack()
for i in range(5):
    stack_arr.push(i)
    print(stack_arr.peak())
for i in range(stack_arr.size()):
    print(stack_arr.pop())
print(stack_arr.size())
print(stack_arr.empty())
for i in range(5):
    stack_arr.push(i)
    print(stack_arr.peak())
print(stack_arr.empty())
print(stack_arr.size())
print('------------------------------------')

# Queue
print('Array Queue')
queue_arr = Queue.ArrayQueue()
for i in range(5):
	queue_arr.enqueue(i)
print(queue_arr.empty())
for i in range(5):
	print(queue_arr.dequeue())
print(queue_arr.empty())
print('------------------------------------')


# Linked List
print('Linked List')
ll = LinkedList.LinkedList(0)
for i in range(1,5):
	ll.add_Elem(i)
ll.printList()
print(ll.get(2))
print(ll.get(5))
ll.add_Elem_pos(3,15)
ll.printList()
print('Size is',ll.size)
ll.add_Elem_pos(5,30)
ll.printList()
ll.remove(5)
ll.printList()
ll.remove(ll.size-1)
ll.printList()
ll.remove(1)
ll.printList()
print('---------')
print(ll.get(0))
print(ll.get(1))
print(ll.get(2))
print('------------------------------------')

# Link Stack
print('Linked list Stack')
stack_ll = Stack.LinkStack()
for i in range(5):
	stack_ll.push(i)
stack_ll.ll.printList()

for i in range(5):
	print(stack_ll.peak())
	print(stack_ll.pop())
print('------------------------------------')

# Link Queue
print('Linked list Queue')
queue_ll = Queue.LinkQueue()
for i in range(5):
	queue_ll.enqueue(i)

for i in range(5):
	print('DQ',queue_ll.dequeue())
