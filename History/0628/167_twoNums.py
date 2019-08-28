
# -*- coding: utf-8 -*

"""
167. 两数之和 II - 输入有序数组

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

!!! 你需要考虑到负数的情况
[-3, 0, 2, 4, 5] target = 1
暴力求解方法
HashTable
双指针 我们要利用排序特性
"""
# def twoNum(numbers, target):
#   # dictionary
#   _Dict = {}
#   for i, element in enumerate(numbers):
#     if _Dict.get(target - element) is not None:
#       return [_Dict.get(target - element) + 1, i + 1]
    
#     _Dict[element] = i

# print(twoNum([-3, 0, 2, 4, 5], 1))

def twoNum(numbers, target):
  i = 0
  j = len(numbers) - 1
  while(i < j):
    Sum = numbers[i] + numbers[j]
    if Sum == target:
      return [i, j]
    elif Sum < target:
      i += 1
    else:
      j -= 1

print(twoNum([-3, 0, 2, 4, 5], 1))