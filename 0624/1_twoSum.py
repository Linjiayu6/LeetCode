# 1. 暴力求解法: 该方法为最最最简单, 最笨方法 
"""
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    result = []
    for i in range(n):
      for j in range(i + 1, n):
        if (nums[i] + nums[j] == target):
          result = [i, j]
          break
      if len(result) == 2:
        break
    return result
"""
# 1.1 暴力求解法
"""
对于给定的target，遍历数组 时间复杂度O(n)， 查找target == m+ n的元素，时间复杂度 O(n) 
因为时间复杂度为 O（n^2） 遍历过程，未使用数据结构存储，故空间复杂度为O(1) 耗时 60ms
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
  size = len(nums)
  for i, element in enumerate(nums):
    j = i + 1
    while j < n:
      if (nums[j] + element == target):
        return [i, j]
      
      j += 1

# 1.2 一遍字典模拟Hash: 字典处理效率高
"""
映射关系叫做字典
类似于Object { id: 1, name: lin }
但是在JavaScript中, 似乎对象本身就是一种字典

python中list对象的存储结构采用的是线性表，因此其查询复杂度为O(n),
而dict对象的存储结构采用的是散列表(hash表)，其在最优情况下查询复杂度为O(1)。

建立HashMap，遍历数组nums，key存储nums[i]，value存储i；
遍历过程中，判断HashMap里是否有target - nums[i]的key值，若有直接返回两个数字index。
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
  # 字典
  _dict = {}
  for i, element in enumerate(nums):
    if _dict.get(target - element) is not None:
      return [i, _dict[target - element]]
    _dict[element] = i
