class Solution:
    a = []

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        self.a = [0 for i in range(n)]
        self.a[0] = 1
        self.a[1] = 2
        return self.climbTopDown(n)

    def climbTopDown(self, n):
        if self.a[n-1] != 0:
            return self.a[n-1]

        else:
            self.a[n - 1] = self.climbTopDown(n - 2) + self.climbTopDown(n - 1)
            return self.a[n - 1]


sol = Solution()
print(sol.climbStairs(3))
