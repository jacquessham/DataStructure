require_relative "LinearSearch"
require_relative "BinarySearch"


n = 100000 # The size of the array
arr = (0..n).to_a
target = arr.sample
puts "Now we are search #{target} between 0 and #{n-1}"

# Linear Search
ls_start = Time.now()
LinearSearch(arr, target)
ls_end = Time.now()
ls_diff = '%.6f' % ((ls_end-ls_start).to_f*1000)
puts "LinearSearch() took #{ls_diff} ms"
# Binary Search
bs_start = Time.now()
BinarySearch(arr, target)
bs_end = Time.now()
bs_diff = '%.6f' % ((bs_end-bs_start).to_f*1000)
puts "BinarySearch() took #{bs_diff} ms"
