class Solution:
    def isValid(self, s: str) -> bool:
        tracking_dict = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for i in range(len(s)):

            temp = tracking_dict.get(s[i], -1)
            #Found in dict means; opening bracket
            if temp != -1:
                stack.append(temp)
            #closing bracket
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == s[i]:
                    stack.pop()
                else:
                    return False
            
        if len(stack) > 0:
            return False
        else:
            return True