class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        _temp = sum(list(set(nums)))
        _dis = (sum(nums) - _temp) / 2
        return int(_temp - _dis)

# 没有用到位运算, 就是一个数学归纳的方法

# TODO: 位运算方法待求解