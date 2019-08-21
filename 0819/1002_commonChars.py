class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        i = 0
        L = []
        while (i < len(A[0])):
            i_data = A[0][i]
            i += 1

            flag = True
            for j in range(1, len(A)):
                if i_data in A[j]:
                    sublist = list(A[j])
                    ind = sublist.index(i_data)
                    sublist.pop(ind)
                    A[j] = ''.join(sublist)
                else:
                    flag = False
            if flag == True:
               L.append(i_data)
        return L
        
print Solution().commonChars(["cool","lock","cook"])
