class Solution:
    def isValid(self, s: str) -> bool:
        dict_ocl = { ')' : '(', ']' : '[', '}' : '{', }
        stack = []
        for i in s:
            #if it is a closing bracket
            if i in dict_ocl:
                #corresponding opening bracket found
                if stack and dict_ocl.get(i) == stack[-1]:
                    stack.pop(-1)
                #opening paranthesis not found
                else:
                    return False
            #if it is a opening bracket
            else:
                stack.append(i)
        
        if stack:
            return False
        else:
            return True