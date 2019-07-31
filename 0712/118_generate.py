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
  List = []
  for i in range(0, numRows):
    itemList = []

    for j in range(0, i + 1):
      if j == 0 or j == i:
        itemList.append(1)
      else:
        previousList = List[i - 1]
        itemList.append(previousList[j-1] + previousList[j])

    List.append(itemList)
  print(List)


def generate2(numRows):
  # 返回内容
  List = []
  # 临时数组
  temp = []
  
  for _ in range(numRows):
    # 每次循环都会在0位置上填上1
    # temp = [1,2,1]
    temp.insert(0, 1)
    # 插入后, 变为 temp = [1,1,2,1]

    # 针对temp的值 在temp基础上, 进行操作, 如果是1或2的情况, 该循环是不进来的
    for i in range(1, len(temp) - 1):
      temp[i] = temp[i] + temp[i + 1]

    # L1 = L # L和L1是一回事，穿同一条裤子，改L的值，L1也改变
    # L1=L[:] #L1和L是两回事，L1和L恩断义绝，改L1的值，L的内心毫无波动
    # temp[:] 是当前的值赋值给List, temp之后变更的内容不会 对List之前值有任何影响
    List.append(temp[:])
  return List

print(generate2(5))

