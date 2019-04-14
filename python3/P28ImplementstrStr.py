class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) == 0:
            return 0

        endIndex = len(haystack) - len(needle)

        count = 0
        for i in range(endIndex + 1):
            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    count += 1
                else:
                    count = 0
                    break
            if count > 0:
                return i

        return -1