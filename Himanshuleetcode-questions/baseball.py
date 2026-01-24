class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        a=0
        for i in range(len(operations)):
            if(operations[i]=='+'):
                stack.append(stack[len(stack)-1]+stack[len(stack)-2])
            elif(operations[i]=='D'):
                stack.append(2*stack[len(stack)-1])
            elif(operations[i]=='C'):
                stack.pop()
            else:
                stack.append(int (operations[i]))

        for j in range(len(stack)):
           a=a+stack[j]
        return a