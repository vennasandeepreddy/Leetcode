class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [3, 2, 4]; target = 6
        """
        my_dict = {}
        #iterating over the nums
        for i in range(len(nums)):
            #how much we are falling short compared to target
            missing_num = target - nums[i]
            #checking if it is already available in dict
            if my_dict.get(missing_num, -1) == -1:   
                #not found, add it to the dict
                my_dict[nums[i]] = i
            else:
                return [i, my_dict.get(missing_num)]