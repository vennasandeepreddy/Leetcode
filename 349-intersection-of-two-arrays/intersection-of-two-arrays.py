class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tracking_dict = {}
        output = []
        for num in nums1:
            if not tracking_dict.get(num):
                tracking_dict[num] = 1
        
        for j in nums2:
            if tracking_dict.get(j, -1) == 1:
                output.append(j)
                tracking_dict[j] = 0
        
        return output



"""
tracking_dict = {
    1:0
    2:1
}




"""

        