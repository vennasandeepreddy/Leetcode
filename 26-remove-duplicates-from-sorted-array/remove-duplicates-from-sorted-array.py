class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        [1, 1, 2, 4]
        """
        p = 0
        q = 1
        unique = 1

        while q < len(nums):
            if nums[p] == nums[q]:
                q = q+1
            else:
                nums[p+1] = nums[q]
                p = p+1
                q = q+1
                unique = unique+1
        return unique


