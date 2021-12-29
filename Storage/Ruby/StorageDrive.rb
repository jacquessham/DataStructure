require_relative 'Stack'


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