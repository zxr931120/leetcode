class Solution:
    def isRightBracket(self, x):
        print(x)
        if x == ')' or x == '}' or x == ']':
            print('true')
            return True
        else:
            print('false')
            return False

    def isMatch(self, x, y):
        if x == '(':
            if y == ')':
                return True

        if x == '{':
            if y == '}':
                return True

        if x == '[':
            if y == ']':
                return True

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        print('Fuck')

        s = list(s)
        print(s)

        if len(s) % 2 != 0:
            return False

        i = 0
        while len(s) > 0:
            while not self.isRightBracket(self, s[i]):
                i += 1
                if i == len(s):
                    print('No matching right bracket')
                    return False

            if i == 0:
                print('first is right')
                return False

            if not self.isMatch(self, s[i - 1], s[i]):
                print('Brackets not matching')
                return False
            else:
                del s[i]
                del s[i - 1]

            i = i - 1

        return True


ss = '(()[]{()[[]]})'
Sol = Solution
print(Sol.isValid(Sol, ss))

#accepted
