import math


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        xstr = list(str(x))

        CheckLen = math.floor(float(len(xstr)) / 2)

        for i in range(CheckLen):
            if xstr[i] != xstr[len(xstr) - 1 - i]:
                return False

        return True

# accepted
