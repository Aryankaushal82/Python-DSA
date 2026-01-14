class Solution:
    def rotate(nums, k):
        n = len(nums)
        k %= n 
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
