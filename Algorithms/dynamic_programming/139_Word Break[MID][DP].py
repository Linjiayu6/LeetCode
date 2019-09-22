# -*- coding: utf-8 -*
"""
cases:
s = "applepenapple", wordDict = ["apple", "pen"] ([ pen , apple apple])
s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"] ([andog, catsan, cat og, cats og, sandog])
s = 'cars', wordDict = ["car","ca","rs"]  ([s, rs, ca])
原定规则有个问题
"ccaccc", ["cc", 'ac']
例如 replace掉cc后剩余"a c"
[a c, cc cc]
"""
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         # wordDict为空或者s为空, 则返回false
#         if not wordDict or not s: return False
#         # 第一个数字匹配, 重叠或者相等命中
#         if not s.replace(wordDict[0], ''): return True
#         # 存放剩下的元素
#         L = [''] * len(wordDict)
#         for i, item in enumerate(wordDict):
#             L[i] = s.replace(item, ' ')
#             print L
#             for j_data in wordDict:
#                 temp = L[i].replace(j_data, ' ')
#                 if not temp.replace(" ", ''): 
#                     return True
#         return False

# print Solution().wordBreak("abcd", ["a","abc","b","cd"])

"""
j = len(s)
s = s(0 - i) + s(i - j)
"""

class Solution(object):
    # 本题回溯法超出时间限制，采用动态回归法
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 初始化标记列表
        flag = [True]+[False]*len(s)

        for start in range(len(s)):
            if flag[start]:
                for end in range(start+1, len(s)+1):
                    print s[start:end]
                    if s[start:end] in wordDict:
                        flag[end] = True
                print flag
        print flag
        return flag[-1]

print Solution().wordBreak("cars", ["car","ca","rs"])