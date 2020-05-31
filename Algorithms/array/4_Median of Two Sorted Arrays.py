"""
注意边界大小
nums1 可能会提前用尽len, 相同nums2 也是这样

归并思路
思路: 因为数组是已经排序好的，那就用双指针方式，有序的将各自的数组内容，插入至tempList中。
     可能会有个数组先用尽自己的len。
     如果超过边界，那就将另外剩余数组内容，直接插入至tempList。
     
     最后根据中间len分配的 复数或单数 找寻中位数。
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sumLen = len(nums1) + len(nums2)
        i, j = 0, 0
        flag = True
        
        tempList = []
        while (flag):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    tempList.append(nums1[i])
                    i += 1
                else:
                    tempList.append(nums2[j])
                    j += 1
            else:
                if (i == len(nums1)):
                    tempList = tempList + nums2[j:]
                else:
                    tempList = tempList + nums1[i:]
                flag = False
        
        half = int(sumLen / 2)
        if (sumLen % 2 != 0):
            return tempList[half]
        else:
            return float(tempList[half - 1] + tempList[half]) / 2


