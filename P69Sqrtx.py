import math


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x ** 2 == x:
            return x

        return self.sqrtHalfSearch(0, x, x)

    def sqrtHalfSearch(self, start, end, num):
        if start + 1 == end:
            return start
        half = math.floor((start + end) / 2)
        if half ** 2 == num:
            return half
        elif half ** 2 > num:
            return self.sqrtHalfSearch(start, half, num)
        else:
            return self.sqrtHalfSearch(half, end, num)

#Accpeted