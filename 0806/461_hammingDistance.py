# -- coding:UTF-8 --

class Solution(object):
    def onList(self, num):
        # list or number or string
        return list(bin(num)[2:])

    def addLen(self, L, add_len):
        add_L = []
        for i in range(0, add_len):
            add_L.append('0')
        L = add_L + L
        return L

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        l_x, l_y = self.onList(x), self.onList(y)
        xy_abs = abs(len(l_x) - len(l_y))

        if len(l_x) > len(l_y):
            l_y = self.addLen(l_y, xy_abs)
        else:
            l_x = self.addLen(l_x, xy_abs)

        print l_x, l_y

        i = 0
        data = 0
        while(i < len(l_x)):
            if l_x[i] != l_y[i]:
              data = data + 1
            i = i + 1
        return data

print Solution().hammingDistance(60, 13)

# ^ 按位异或运算符：当两对应的二进位相异时，结果为1
# 	(60 ^ 13) 输出结果 49 ，二进制解释： 0011 0001
# 0b110001
print bin(60 ^ 13)
print bin(60 ^ 13).count('1')


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 异或运算 1都是不同的, 再数1
        # return bin(x ^ y).count('1')
        b = bin(x ^ y)
        
        data = 0
        for i in b:
            if i == '1':
                data += 1
                
        return data