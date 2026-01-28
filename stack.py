stack=[]
# it is LIFO data structure
def push(val,stack):
    stack.append(val)
def pop_1(stack):
    return stack.pop()
def size(stack):
    return len(stack)
def top(stack):
    return stack[-1]


## monotonic stack
def next_greater_element(arr):
    result=[-1]*len(arr)
    mono_stack=[]
    for i in range(len(arr)-1,-1,-1):
        while size(mono_stack)>0 and top(mono_stack)<=arr[i]:
            pop_1(mono_stack)
        if size(mono_stack)>0:
            result[i]=top(mono_stack)
        push(arr[i],mono_stack)
    return result


