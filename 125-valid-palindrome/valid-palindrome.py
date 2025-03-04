import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        s = raceacar
        '''
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        i = 0
        j = len(s)-1

        while i<=j:
            if s[i] == s[j]:
                i = i+1
                j = j-1
            else:
                return False
        
        return True
