def two_sum_optimal(num,target):
        seen={}
        for i in range(len(num)):
                value=target-num[i]
                if value in seen.keys():
                        return[seen[value],i]
                seen[num[i]]=i
        return []
print(f"Indices are : {two_sum_optimal([2,7,11,15],9)}")  