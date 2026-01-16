# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# brute force
def two_sum(num,target):
    for i in range(len(num)):
                for j in range(i+1,len(num)):
                        if(num[i]+num[j]==target):
                                return[i,j]
    return[]
print(f"Indices are : {two_sum([2,7,11,15],9)}")                    
                   
# optimal approach
def two_sum_optimal(num,target):
        seen={}
        for i in range(len(num)):
                value=target-num[i]
                if value in seen.keys():
                        return[seen[value],i]
                seen[num[i]]=i
        return []
print(f"Indices are : {two_sum_optimal([2,7,11,15],9)}")  