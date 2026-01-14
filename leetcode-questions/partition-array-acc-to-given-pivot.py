def pivotArray( nums, pivot):
        res = [0] * len(nums)
        pivotCount = 0
        idx=0
        for i in range(len(nums)):
            if(nums[i]==pivot):
                pivotCount+=1
            elif(nums[i]<pivot):
                res[idx] = nums[i]
                idx+=1
        
        while(pivotCount!=0):
            res[idx] = pivot
            idx+=1
            pivotCount-=1
        for i in range(len(nums)):
            if(nums[i]>pivot):
                res[idx] = nums[i]
                idx+=1
        return res