require_relative "LinearSearch"
require_relative "BinarySearch"

arr = (0..5).to_a
target = 2

puts "#{LinearSearch(arr, target)}"
puts "#{BinarySearch(arr, target)}"