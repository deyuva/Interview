# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# notes:

# - is it sorted?
# - duplication of elements?
# - multiple solutions?

# SOLUTION 1 algorithem:

# 1 - sort the array.

# 2 - assign 2 pointers: low at index 0, high at index len(array) - 1

# 3 - while high > low:
        sum = array[low] + array[high]
        if sum > target:
          high = high -1 
        elif sum < target:
          low = low + 1
        if sum == target:
          return (low, high)
          
# SOLUTION 1 python:

def twoSum(nums, target):
        
    nums_sorted = sorted(nums)
    low = 0
    high = len(nums) - 1
        
    while high > low:
        sum = nums_sorted[low] + nums_sorted[high]
            
        if sum > target:
            high = high -1
                
        elif sum < target:
            low = low + 1
            
        else:
            return (low, high)
            
    return -1



# SOLUTION 2 algorithem:

# 1 - create a hash table

# 2 - create an index variable, i = 0

# 3 - while i < len(array) - 1

        if array[i] is in hash:
          return (i, hash[i])
          
        complement = target - array[i]
        
        hash[i] = comlement
        
       return -1
       
# SOLUTION 2 python:


def twoSum(nums, target):

    hash1 = {}
    i = 0
    
    while i < len(nums) - 1:
        if nums[i] in hash1:
            return (hash1[nums[i]], i)
        else:
            hash1[target - nums[i]] = i
        i += 1
    
    return -1
    
    
list1 = [3,5,6,7,9,11]
target = 14

        
        




        
