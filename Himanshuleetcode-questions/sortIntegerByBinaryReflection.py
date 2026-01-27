
# Code


# Testcase
# Testcase
# Test Result
# 3769. Sort Integers by Binary Reflection
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums.

# The binary reflection of a positive integer is defined as the number obtained by reversing the order of its binary digits (ignoring any leading zeros) and interpreting the resulting binary number as a decimal.

# Sort the array in ascending order based on the binary reflection of each element. If two different numbers have the same binary reflection, the smaller original number should appear first.

# Return the resulting sorted array.

 

# Example 1:

# Input: nums = [4,5,4]

# Output: [4,4,5]

# Explanation:

# Binary reflections are:

# 4 -> (binary) 100 -> (reversed) 001 -> 1
# 5 -> (binary) 101 -> (reversed) 101 -> 5
# 4 -> (binary) 100 -> (reversed) 001 -> 1
# Sorting by the reflected values gives [4, 4, 5].
# Example 2:

# Input: nums = [3,6,5,8]

# Output: [8,3,6,5]

# Explanation:

# Binary reflections are:

# 3 -> (binary) 11 -> (reversed) 11 -> 3
# 6 -> (binary) 110 -> (reversed) 011 -> 3
# 5 -> (binary) 101 -> (reversed) 101 -> 5
# 8 -> (binary) 1000 -> (reversed) 0001 -> 1
# Sorting by the reflected values gives [8, 3, 6, 5].
# Note that 3 and 6 have the same reflection, so we arrange them in increasing order of original value.
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 109

def binary_reflection(nums):
    a=[]
    for num in nums:
        binary=bin(num)[2:]
        reversed_binary=binary[::-1]
        reflected=int(reversed_binary,2)
        a.append((reflected,num))
    a.sort()
    result=[]
    for i in a:
        result.append(i[1])
    return result
print(binary_reflection([4,5,4]))  # Output: [4,4,5]


    