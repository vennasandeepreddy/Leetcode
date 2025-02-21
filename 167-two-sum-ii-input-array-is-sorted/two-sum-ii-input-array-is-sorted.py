class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        [2,7,11,15], target = 9
        """
        i = 0
        j = len(numbers)-1

        while i < j:
            if numbers[i]+numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i]+numbers[j] > target:
                j= j-1
            else:
                i = i+1







