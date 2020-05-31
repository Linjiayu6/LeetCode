class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # [4,3,2,7,8,2,3,1]
        obj = {}
        List = []
        for data in nums:
            # 判断对象里是否有该值
            if obj.get(str(data)):
                List.append(data)
            else:
                obj[str(data)] = data
                
        return List