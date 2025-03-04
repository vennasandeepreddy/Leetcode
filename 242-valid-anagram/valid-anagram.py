class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s)!= len(t):
            return False

        for i in range(len(s)):
            s_check = s_dict.get(s[i], -1)
            if s_check == -1:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] = s_check + 1

        for j in range(len(t)):
            t_check = t_dict.get(t[j], -1)
            if t_check == -1:
                t_dict[t[j]] = 1
            else:
                t_dict[t[j]] = t_check + 1

        for k in s_dict:
            if k not in t_dict or s_dict[k] != t_dict[k]:
                return False
        return True
                
                
