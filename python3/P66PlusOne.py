class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits) - 1] += 1

        carry = False
        for i in range(len(digits)):
            if carry:
                digits[len(digits) - i - 1] += 1
                carry = False
            if digits[len(digits) - i - 1] >= 10:
                digits[len(digits) - i - 1] -= 10
                carry = True

        if carry:
            digits.insert(0, 1)
        return digits

#accepted
dig = [9, 9, 9]
sol = Solution()
print(sol.plusOne(dig))
