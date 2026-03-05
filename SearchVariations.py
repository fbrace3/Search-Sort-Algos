from SortVariations import bubbleSort as bs
from random import randint as ri

def linearSearch(nums, target):
    for x in nums:
        if x == target:
            return True, target
    
    return False, target

def binarySearch(nums, target):
    mid = len(nums) // 2
    if len(nums) <= 1:
        return False, target
 
    if target == nums[mid]:
        return True, target
    elif target < nums[mid]:
        nums = nums[:mid]
        
    else:
        nums = nums[mid:]
    return binarySearch(nums, target)


target = 34
nums = [ri(0, 100) for _ in range(0, 100)]
sorted_nums = bs(nums)[0]
print(sorted_nums)

print(linearSearch(nums, target))
print(binarySearch(nums, target))
