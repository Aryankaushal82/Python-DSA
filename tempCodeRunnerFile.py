
def linear_search(num,target):
    for i in range(len(num)):
      if num[i]==target:
          return True
      return False
n=[1,2,3,45,66]
t=66
print(linear_search(n,t))   