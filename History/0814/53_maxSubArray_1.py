# -*- coding: utf-8 -*

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入: [-2,1,-3,4,-1,2,1,-5,4]
"""

"""
!连续状态
字段
1. tmp: 暂存 连续或上一个状态的内容 
2. max: 目前最大值

如果 tmp + nums[i] > nums[i]，则说明对结果有增益效果，则保留并加上当前遍历数字
否则，则说明对结果无增益效果，需要舍弃，则直接更新为当前遍历数字
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 前一个值 或 前一组连续的值
        tmp = nums[0]
        max_ = tmp
        for i in range(1, len(nums)):
            # 前一组连续的值 强强联手 > 目前值 说明可以继续走下去了
            if tmp + nums[i] > nums[i]:
                max_ = max(tmp + nums[i], max_)
                tmp += nums[i]
            # 当前值 因为局部已经是小的情况了
            else:
                max_ = max(tmp, nums[i], max_)
                tmp = nums[i]
        return max_

print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])


"""
网友的解释很到位

假设你是一个选择性遗忘的赌徒，数组表示你这几天来赢钱或者输钱，
你用sum来表示这几天来的输赢，
用ans来存储你手里赢到的最多的钱，

如果昨天你手上还是输钱（sum < 0），你忘记它，明天继续赌钱；
如果你手上是赢钱(sum > 0), 你记得，你继续赌钱；
你记得你手气最好的时候
"""