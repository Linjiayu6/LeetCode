
# # -- coding:UTF-8 --
# """
# 在大小为 2N 的数组 A 中有 N+1 个不同的元素，
# 其中有一个元素重复了 N 次。
# 返回重复了 N 次的那个元素。

# 其余的每种是不重复的, 只有一个是占N种的, 相当于找重复元素
# """
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = set()
        for i in A:
            if i in a:
                return i
            else:
                a.add(i)

print Solution().repeatedNTimes([9,5,3,3])


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        set_A = sorted(set(A))
        N = len(set_A) - 1
        # 找到重复N次的那个元素
        for i in set_A:
            if A.count(i) == N:
                return i


class Solution(object):
    def repeatedNTimes(self, A):
        dictionary = {}
        for i in A:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

        N = len(A) // 2
        for key, value in dictionary.items():
            if value == N:
                return key

print Solution().repeatedNTimes([2,1,2,5,3,2])
