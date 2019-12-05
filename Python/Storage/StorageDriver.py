import Stack
import Queue


# Stack
stack = Stack.ArrayStack()
for i in range(5):
    stack.push(i)
    print(stack.peak())
for i in range(stack.size()):
    print(stack.pop())
print(stack.size())
print(stack.empty())
for i in range(5):
    stack.push(i)
    print(stack.peak())
print(stack.empty())
print(stack.size())
print('------------------------------------')

# Queue
queue = Queue.ArrayQueue()
for i in range(5):
	queue.enqueue(i)
print(queue.empty())
for i in range(5):
	print(queue.dequeue())
print(queue.empty())