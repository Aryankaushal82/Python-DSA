# Time is prioritize in Time and space complexity if time is less and space is more then time priority is more
# We should always try to reduce time complexity if we can increase space complexity and decrease time complexity we should prefer that

# linear search
#  li=[1,2,3,4,5]
# n=5
# if our target value is 5 we have to iterate through all the value of the list and complexity will be O(n) it is worst case and we have target value is 1 then time complexity will be omega (1) which best case sceanrio
# 0(1),O(logn),O(n),O(nlogn),O(n^2),O(2^n),O(n!) 

def linear_search(num,arr):
    for i in range(len(arr)):
        if(arr[i]==num):
            return True,f"Element found at index {i}"
    return False,"Element not found"
a=[2,4,6,7,9]
n=10
print(linear_search(n,a))


def binary_search(num,arr):
    l=0
    r=len(arr)-1
    while l<=r:
        m=(l+r)//2
        if num<arr[m]:
            r=m-1
        elif num>arr[m]:
            l=m+1
        else:
            return True,f"Element found at index {m}"
    return False,"Element not found"
a=[1,5,6,7,18,55,66,87]
n=55
print(binary_search(n,a))