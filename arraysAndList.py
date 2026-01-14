print("hello python")

a = [1,2,3,4]
b=[]

print(type(a))
print(len(a))
print(a[0])
print(a.index(2))
a.append(5)
print(a)


def linear_search(arr,target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i
    return -1


print(f"Index of 3 is : {linear_search(a,3)}")



def binary_search(arr,target):
    l = 0
    r = len(arr)-1
    while(l<=r):
        m = l+(r-l)//2
        if(arr[m]==target):
            return m
        elif(arr[m]<target):
            l=m+1
        else:
            r=m-1
    return -1

print(f"Index of 3 is : {binary_search(a,3)}")