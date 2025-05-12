class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ip_dict = {}
        for i, ele in enumerate(nums):
            lookup = target - ele
            idx = ip_dict.get(lookup, -1)
            if idx is not -1:
                return [i, idx]
            else:
                ip_dict[ele] = i


        