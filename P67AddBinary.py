class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        compLen = 0
        longer = ''
        result = ''

        if len(a) <= len(b):
            shorter = a
            longer = b
        else:
            shorter = b
            longer = a

        carry = 0
        for i in range(len(shorter)):
            re = int(a[len(a) - i - 1]) + int(b[len(b) - i - 1]) + carry
            if re > 1:
                result = str(re - 2) + result
                carry = 1
            else:
                result = str(re) + result
                carry = 0

        for i in range(len(shorter),len(longer)):
            re = int(longer[len(longer) - i - 1]) + carry
            if re > 1:
                result = str(re - 2) + result
                carry = 1
            else:
                result = str(re) + result
                carry = 0

        if carry == 1:
            result = '1' + result

        return result

#accepted
a = "10010"
b = "111"

sol = Solution
print(sol.addBinary(sol, a, b))
