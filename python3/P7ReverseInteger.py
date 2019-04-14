class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= pow(2,31)-1 or x <= -1 * pow(2,31):
            return 0

        result = 0
        neg = False
        if x < 0:
            neg = True

        xstr = list(str(x))

        print(xstr)

        bitOfx = len(xstr)
        if neg:
            bitOfx -= 1

        print(bitOfx)

        for i in range(bitOfx):
            result += int(xstr[len(xstr) - 1 - i]) * pow(10, bitOfx - i - 1)
            if result >= pow(2, 31) - 1 or result <= -1 * pow(2, 31):
                return 0

        if neg:
            result = result * -1
        return result


x = 12340000
Sol = Solution()
print(Sol.reverse(x))

#accepted