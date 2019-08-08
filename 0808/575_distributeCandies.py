class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # 第一种
        # return min(len(set(candies)), len(candies) / 2)

        # 第二种
        dic = {}
        for i in candies:
            if i in dic:
                dic[i] =+ 1
            else:
                dic[i] = 1
        return min(len(dic.keys()), len(candies) / 2)

print Solution().distributeCandies([1,1,2,3])
