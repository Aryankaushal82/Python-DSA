def linear_search(num,arr):
    for i in range(len(arr)):
        if(arr[i]==num):
            return True,f"Element found at index {i}"
    return False,"Element not found"
a=[2,4,6,7,9]
n=10
print(linear_search(n,a))