# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:24:27 2019

@author: heich
"""

class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        if x > 0:
            x = list(str(x))
        else:
            a+=1
            x = list(str(-x))
        x = x[::-1]
        x = ''.join(x)
        if a==0:
            if int(x)<2**31-1:
                return (int(x))
            else:
                return 0
        else:
            if -int(x) > -2**31:
                return (-int(x))
            else:
                return 0