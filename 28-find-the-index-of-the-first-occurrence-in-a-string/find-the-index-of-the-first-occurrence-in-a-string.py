class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p = 0
        ret = -1
        while p <= len(haystack)-len(needle):
            if haystack[p:p+len(needle)] == needle:
                ret = p
                break
            p = p+1
        return ret