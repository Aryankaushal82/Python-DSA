# Two Sum

# brute force approach
def two_sum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if(num[i]+num[j]==target):
                return [i,j]
    return []



print(f"Indices are : {two_sum([2,7,11,15],9)}")

# optimal approach
def two_sum_optimal(num,target):
    seen = {}
    for i in range(len(num)):
        complement = target - num[i]
        if complement in seen:
            return [seen[complement], i]
        seen[num[i]] = i
    return []

print(f"Indices are : {two_sum_optimal([2,7,11,15],9)}")