class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lenOfList = len(nums)

        j = 0
        for i in range(lenOfList):
            if nums[j] == val:
                del nums[j]
            else:
                j += 1

        return  len(nums)