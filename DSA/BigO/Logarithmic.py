# Logarithmic Time O(log n)

# Suppose we have a sorted array and we must find the
# index of a particular value in the array, if it exists. 
# What is the time complexity of the following algorithm ?

import math

nums = [1,3,4,5,7,9,11,23]
target = 33

low = 0
high = len(nums) - 1

while low <= high :
    mid = math.floor(low + (high - low)// 2)
    if nums[mid] == target:
        print(f"Index found : {mid}")
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Index not found")