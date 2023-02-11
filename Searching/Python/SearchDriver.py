from datetime import datetime, timedelta
from random import randint
import LinearSearch as ls
import BinarySearch as bs


n = 100000 # The size of the list
arr = range(n)
target = randint(0,n-1)
print(f'Now we are searching {target} between 0 and {n-1}')

# Linear Search
ls_start = datetime.now()
ls.LinearSearch(arr,target)
ls_end = datetime.now()
ls_diff = (ls_end-ls_start).total_seconds()*1000
print(f'LinearSearch() took {ls_diff:.6f} ms')
# Binary Search
bs_start = datetime.now()
bs.BinarySearch(arr,target)
bs_end = datetime.now()
bs_diff = (bs_end-bs_start).total_seconds()*1000
print(f'BinarySearch() took {bs_diff:.6f} ms')
