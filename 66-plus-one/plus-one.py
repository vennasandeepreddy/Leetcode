class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        [1,2,3] - [3*10^0 + 2*10^1 + 1*10^2]
        """
        i = len(digits)-1
        digit = 0
        power = 0
        while i >= 0:
            digit = digit+(digits[i]*10**power)
            i = i-1
            power += 1
        digit = digit+1

        result = []
        for char in str(digit):
            result.append(int(char))
        return result




        