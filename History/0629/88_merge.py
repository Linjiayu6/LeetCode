"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""
# def merge(nums1, m, nums2, n):
#   i = 0
#   j = 0
#   L = []
#   nums1 = nums1[:m+1]
#   nums2 = nums2[:n+1]
#   while(i < m and j < n):
#     a = nums1[i]
#     b = nums2[j]
#     if a < b:
#       L.append(a)
#       i += 1
#     elif a > b:
#       L.append(b)
#       j += 1
#     else:
#       L.append(a)
#       L.append(b)
#       i += 1
#       j += 1
#   if (i<m): L += nums1[i:m]
#   if (j<n): L += nums2[j:n]

#   return L

# print(merge([1,2,3], 3, [2,5,6],3))

"""
该题的重点不是新创建一个L, 而是覆盖掉nums1
"""
# def merge(nums1, m, nums2, n):
#   i = m - 1
#   j = n - 1
#   z = m + n - 1
#   while(True):
#     if (i < 0 or j < 0):
#       break

#     if nums1[i] < nums2[j]:
#       nums1[z] = nums2[j]
#       j -= 1
#       z -= 1
#     else:
#       nums1[z] = nums1[i]
#       i -= 1
#       z -= 1

#   while(i >= 0):
#     nums1[z] = nums1[i] 
#     i -= 1 
#     z -= 1
#   while(j >= 0): 
#     nums1[z] = nums2[j] 
#     j -= 1 
#     z -= 1

#   return nums1
# print(merge([1,2,3,0,0,0], 3, [2,5,6],3))

def merge(nums1, m, nums2, n):
  i = m
  j = 0
  while(j < n):
    nums1[i] = nums2[j]
    i += 1
    j += 1
  
  # 前面已经是排序好的, 插入排序
  for x in range(m, len(nums1), 1):
    for y in range(x, 0, -1):
      if (nums1[y] < nums1[y - 1]):
        nums1[y], nums1[y - 1] = nums1[y - 1], nums1[y]

  return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6],3))