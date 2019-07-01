# -*- coding: utf-8 -*
"""
在杨辉三角中，每个数是它左上方和右上方的数的和。

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

def generate(numRows):
  L = []
  if numRows == 1:
    L += [1]
  else:
    for i in range(numRows):
      

  return L