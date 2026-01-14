a = {1:'aryan',2:'john',3:'doe',4:'smith'}
print(type(a))
print(a)
print(len(a))
print(a[1])
a[5]='hello'
print(a)
print(a.keys())
print(a.values())
print(a.items())

for i in a.keys():
    print(f"Key is : {i} and Value is : {a[i]}")

for i,j in a.items():
    print(f"Key is : {i} and Value is : {j}")