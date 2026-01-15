# in python the list are denoted by []
#  difference bettween array and list is that list can store all the type of data wheereas arrya can can integer type of data 
a=[1,'a',True]
print(type(a))
print(len(a))  #it will print number of element in the list
# how to iterate through the list
for i in range(0,len(a)):
    print(a[i])
# how to find if element is present in the list or not
fruits = ['apple','banana','mango','grapes']
if "banana" in fruits: # we can use in keyword to find if element is present in the list or not
    print("banana is present in the list")

def linear_search(num,target):
    for i in range(len(num)):
      if num[i]==target:
          return True
      return False
n=[1,2,3,45,66]
t=66
print(linear_search(n,t))        