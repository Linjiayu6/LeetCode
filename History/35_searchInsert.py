
# -*- coding: utf-8 -*
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
示例 1:

输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1
"""
# def searchInsert(nums, target):
#   i = len(nums)
#   while(True):
#     i = i // 2
#     if (nums[i] == target):
#       return i
#     elif (nums[i] > target):
#       searchInsert(nums[0:i], target)
#     else:
#       searchInsert(nums[i:len(nums)], target)
#     if (i == 0):
#       return -1


# print(searchInsert([1,3,5,6], 2))

# 二分法 + 双指针方法
# def searchInsert(nums, start, end, target):
#   print(nums[start:end])
#   i = len(nums[start:end]) // 2

#   # 直接命中target
#   if nums[i] == target:
#     return i

#   # 当前值大于则, 目标锁定到0到i-1位置
#   if nums[i] > target:
#     if (len(nums) == 1):
#       return i - 1
#     # nums[0, i]
#     searchInsert(nums, 0, i + 1, target)

#   if nums[i] < target:
#     if (len(nums) == 1):
#       return i + 1
#     # nums[i + 1, len(nums) - 1]
#     searchInsert(nums, i + 1, len(nums[start:end]), target)

# print(searchInsert([1,3,5,6], 0, 3, 6))