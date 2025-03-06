class Solution:
    def isHappy(self, n: int) -> bool:
        tracking_list = []

        while n != 1:
            if n in tracking_list:
                return False
            else:
                tracking_list.append(n)
                temp_sum = 0
                for i in str(n):
                    temp_sum = temp_sum+int(i)**2
                n = temp_sum

        return True