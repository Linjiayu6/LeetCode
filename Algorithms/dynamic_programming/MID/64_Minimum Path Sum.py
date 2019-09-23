
# https://leetcode-cn.com/problems/minimum-path-sum/

# grid[i,j] = grid[i,j] + min(grid[i-1,j], grid[i,j-1])
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # eg: m * n = 2 * 3 matrix
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                print i, j
                if i == 0 and j == 0:
                    continue
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                elif i != 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
        # grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])

print Solution().minPathSum(
  [
    [1,3,1],
    [1,5,1],
    [4,2,1]
  ]
)