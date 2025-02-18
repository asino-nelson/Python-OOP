# Logarithmic Time O(log n)

# Suppose we have a sorted array and we must find the
# index of a particular value in the array, if it exists. 
# What is the time complexity of the following algorithm ?

nums = [1,3,4,5,7,9,11,23]
indx = 4

low = 0
high = len(nums) - 1

if low <= nums[0] :
    mid = (high - low)/2
    if nums[mid] == indx:
        print(mid)
    elif nums[mid] < indx:
        low = mid + 1
    elif nums[mid] > indx:
        high = mid - 1

print("Index not found")