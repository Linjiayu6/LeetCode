"""
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

https://leetcode-cn.com/problems/unique-paths-ii
"""
"""
if obstacleGrids[i][j] == 0:
  obstacleGrids[i][j] = obstacleGrids[i-1][j] + obstacleGrids[i][j]

28 ms, 在所有 Python 提交中击败了99.76%的用户
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1: return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                else:
                    if obstacleGrid[i][j] != 1:
                        if i == 0 and j > 0:
                          grid[i][j] += grid[i][j - 1]
                        elif i > 0 and j == 0:
                            grid[i][j] += grid[i - 1][j]
                        else:
                            grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
        print grid
        return grid[-1][-1]
print Solution().uniquePathsWithObstacles(
  [
    [0,0,0],
    [0,1,0],
    [0,0,0]
  ]
)
