class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return False
        
        else:
            _len = len(nums)
            array = [1] * _len
            for i in range(1, _len):
                for j in range(i - 1, -1, -1):
                    if nums[j] < nums[i]:
                        array[i] = max(array[i], array[j] + 1)
                        if (array[i] == 3):
                            return True
                        
                        
        return False