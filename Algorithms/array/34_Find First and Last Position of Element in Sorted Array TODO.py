class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
        1. target 不在 nums 里 return [-1, -1]
        2. 在nums里, 二分法处理
           left = nums[0: len(nums) / 2]  right = nums[len(nums) / 2:]
           
           - 左边没有, 放弃, 右边有, 继续
           - 左边有, 继续, 右边没有, 放弃
           - 左边右边都有, 那从左边尾部找, 右侧头部找
        """
        
        # [5,7,7,8,8,10]
        half = len(nums) / 2
        
        left, right = 0, len(nums)
        while (left < right):
            # 在右侧
            if nums[half] < target:
                left = half
                while(left < right):
                    if nums[left] != target:
                        left += 1
                    if nums[right] != target:
                        right -= 1
            # 在左侧
            elif nums[half] > target:
                right = half
                
                if nums[left] != target:
                    left += 1
                if nums[right] != target:
                    right -= 1

            # 两边都有
            else:
                left, right = half, half + 1
                if nums[left] == target:
                    if left >= 0 and nums[left] == target:
                        left -= 1
                if nums[right] == target:
                    if right < len(nums) and nums[right] == target:
                        right += 1
                
            return [left, right]