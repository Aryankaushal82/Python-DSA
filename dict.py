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


# 3 important looping present .keys,.values,.items     

d={1:"a",2:"b",3:"c"}
# print(d.keys()) #it will print all the keys present in the dictionary
# print(d.values())#it will print all the values present in the dictionary
# print(d.items())#it will print all the key value pair present in the dictionary
# for i in d.keys():
#     print(d[i])
for i in d.items():
    print(i[0]) 
# for i in d.values():
#     print(i)   