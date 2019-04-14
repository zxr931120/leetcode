class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        buff = nums[0]
        j = 1

        for i in range(1, len(nums)):
            if nums[j] == buff:
                del nums[j]
            else:
                buff = nums[j]
                j += 1

        return len(nums)


sol = Solution()
inList = []
print(sol.removeDuplicates(inList))
print(inList)
