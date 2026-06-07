class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack= []
        for i in operations:
            if i == '+':
                entry= stack[-1] + stack[-2]
                stack.append(entry)
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                entry= stack[-1] * 2
                stack.append(entry)
            else:
                stack.append(int(i))
        
        return sum(stack)
        