require_relative 'Stack'
require_relative 'Queue'
require_relative 'LinkedList'


# Stack
puts "Array Stack"
stack_arr = ArrayStack.new()
for i in 0..4 do
	stack_arr.push(i)
	puts stack_arr.peak()
end
for i in 0..stack_arr.size() do
	puts stack_arr.pop()
end
puts stack_arr.size()
puts stack_arr.empty()
for i in 0..4 do
	stack_arr.push(i)
	puts stack_arr.peak()
end
puts stack_arr.size()
puts stack_arr.empty()
puts "------------------------------------"

# Queue
puts "Array Queue"
queue_arr = ArrayQueue.new()
for i in 0..4 do
	queue_arr.enqueue(i)
end
puts "#{queue_arr.empty()}"
for i in 0..4 do
	queue_arr.dequeue()
end
puts "#{queue_arr.empty()}"
puts "------------------------------------"

# LinkedList
puts "Linked List"
ll = LinkedList.new(0)
for i in 1..5 do
	ll.add_Elem(i)
end
ll.printList()
puts ll.get(2)
puts ll.get(5)
ll.add_Elem_pos(3,15)
ll.printList()
puts "Size is #{ll.getSize()}"
ll.add_Elem_pos(5,30)
ll.printList()
ll.remove(5)
ll.printList()
ll.remove(ll.getSize()-1)
ll.printList()
ll.remove(1)
ll.printList()
puts '---------'
puts ll.get(0)
puts ll.get(1)
puts ll.get(2)
puts '------------------------------------'
