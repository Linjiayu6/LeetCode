"""
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:
输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
"""
def containsDuplicate(nums):
  _dict = {}
  for i, element in enumerate(nums):
    if _dict.get(element) is not None:
      return true
    _dict[element] = i
        