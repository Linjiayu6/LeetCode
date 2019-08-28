# -*- coding: utf-8 -*

"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""

class Solution(object):
    def defangIPaddr(self, address = ''):
        """
        :type address: str
        :rtype: str
        """
        # 规则.join(list)
        # print '[.]'.join(address.split('.'))
        print address.replace('.', '[.]')

Solution().defangIPaddr('255.100.50.0')
