def sortArrayByParity(nums):
        i=0
        j=len(nums)-1
        while(i<j):
            if(nums[i]%2==0):
                i+=1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j-=1
        
        return nums
    
print(sortArrayByParity([3,1,2,4]))