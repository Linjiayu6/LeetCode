# -*- coding: utf-8 -*

"""
学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。
请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：能让所有学生以 非递减 高度排列的必要移动人数。

1,2,3,4,5,.:递增排列 
9,8,7,6,5.:递减排列 
1,2,3,3,4,5,8,8,.:非递减排列 
9,8,7,7,6,5,5,2,1,.:非递增排列

Students are asked to stand in non-decreasing order of heights for an annual photo.
至少
Return the minimum number of students not standing in the right positions.  
(This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.
"""

def heightChecker(heights):
  checker = []
  # 先排序, 再对两个数据进行数值比较
  sortHeights = sorted(heights)
  for i, d in enumerate(sortHeights):
    if d != heights[i]:
      checker.append(d)
  return len(checker)


print(heightChecker([1,1,4,2,1,3]))
