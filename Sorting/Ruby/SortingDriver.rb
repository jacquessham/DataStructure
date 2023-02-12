require_relative "SelectionSort"
require_relative "BubbleSort"
require_relative "InsertionSort"
require_relative "MergeSort"
require_relative "QuickSort"


# Set the size of array
arr_len = 10000

# Build an array with numbers randomly assigned
min_num = 0
max_num = 50000
arr = Array.new(arr_len){rand(min_num...max_num)}


# Time for selection sort
ss_start = Time.now()
arr_selectSorted = selectionSort(arr.clone)
ss_end = Time.now()
ss_time_diff = '%.6f' % ((ss_end-ss_start).to_f*1000)
puts "It took #{ss_time_diff} seconds to sort with Selection Sort"

# Time for Bubble Sort
bs_start = Time.now()
arr_bubbleSorted = bubbleSort(arr.clone)
bs_end = Time.now()
bs_time_diff = '%.6f' % ((bs_end-bs_start).to_f)
puts "It took #{bs_time_diff} seconds to sort with Bubble Sort"

# Time for Insertion Sort
is_start = Time.now()
arr_insertionSorted = insertionSort(arr.clone)
is_end = Time.now()
is_time_diff = '%.6f' % ((is_end-is_start).to_f)
puts "It took #{is_time_diff} seconds to sort with Insertion Sort"


# Time for Merge Sort
ms_start = Time.now()
arr_mergeSorted = mergeSort(arr.clone)
ms_end = Time.now()
ms_time_diff = '%.6f' % ((ms_end-ms_start).to_f)
puts "It took #{ms_time_diff} seconds to sort with Merge Sort"

# Time for Quick Sort
qs_start = Time.now()
arr_quickSorted = quickSort(arr.clone)
qs_end = Time.now()
qs_time_diff = '%.6f' % ((qs_end-qs_start).to_f)
puts "It took #{qs_time_diff} seconds to sort with Quick Sort"
