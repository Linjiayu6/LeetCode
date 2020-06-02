class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 1. 先排序
        intervals.sort()
        
        # 2. 再合并
        i, m, = 0, len(intervals)
        if (m == 1 or m == 0):
          return intervals
        n = len(intervals[0])
        while (i < m - 1):
          # [1, 4] [0, 5]
          if intervals[i][n - 1] >= intervals[i + 1][0]:
              intervals[i] = [min(intervals[i][0], intervals[i + 1][0]), max(intervals[i][n - 1], intervals[i + 1][n - 1])]
              del intervals[i + 1]
              m -= 1
          else:
              i += 1
              
        return intervals