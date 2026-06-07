class Solution:
    def isValid(self, s: str) -> bool:
        parenth_dict= {'(':')','[':']','{':'}'}
        stack= []
        if len(s) % 2 !=0:
            return False

        for i in s:
            if i in parenth_dict:
                stack.append(i)
            elif stack:
                if i == parenth_dict[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return True if not stack else False

        