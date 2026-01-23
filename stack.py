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

