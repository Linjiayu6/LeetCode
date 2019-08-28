# -- coding:UTF-8 --

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # i = 1 to len(A) - 2
        i = 1
        A_len = len(A) - 1
        while(True):
            if i > A_len - 1:
                break
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                return i
            else:
                i += 1

print Solution().peakIndexInMountainArray([0,2,1,0])