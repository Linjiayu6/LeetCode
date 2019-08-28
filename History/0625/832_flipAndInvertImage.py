# -*- coding: utf-8 -*

"""
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

[[1,1,0],[1,0,1],[0,0,0]]
"""
def flipAndInvertImage(A):
  result = []
  for item in A:
    newItem = []
    n = len(item)
    while True:
      print(n)
      if n > 0:
        # 水平翻转 [1, 1, 0] 的结果是 [0, 1, 1], 反转 [0, 1, 1] 的结果是 [1, 0, 0] 
        newItem.append(0 if item[n - 1] == 1 else 1)
        n = n - 1
      else:
        break

    print(newItem)
    result.append(newItem)    

  return result

print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))


"""
别人的例子
"""
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
  # i: 0, data1: [1,1,0]
  for i, data1 in enumerate(A):
    # list[<start>:<stop>:<step>]
    for j, data2 in enumerate(data1[::-1]):
      # 绝对值
      A[i][j] = abs(data2 - 1)
  return A

"""
list[<start>:<stop>:<step>]
[::-1] take everything in this dimension but backwards
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a[:-1]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> a[-2::-1]
[8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

