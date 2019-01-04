import math


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lenOfList = len(nums)

        if lenOfList == 0:
            return 0

        if target <= nums[0]:
            return 0

        if target == nums[lenOfList - 1]:
            return lenOfList - 1

        if target > nums[lenOfList - 1]:
            return lenOfList

        inIndex = self.BinarySearch(self, 0, lenOfList - 1, nums, target)
        print(inIndex)
        return inIndex

    def BinarySearch(self, startIndex, endIndex, nums, target):
        print('start index: ', startIndex)
        print('end index: ', endIndex)
        if startIndex + 1 == endIndex:
            return endIndex

        halfIndex = math.floor(float(startIndex + endIndex) / 2)
        if target == nums[halfIndex]:
            return halfIndex
        elif target > nums[halfIndex]:
            return self.BinarySearch(self, halfIndex, endIndex, nums, target)
        elif target < nums[halfIndex]:
            return self.BinarySearch(self, startIndex, halfIndex, nums, target)

#Accepted, O(logn)

nums = [1, 3, 5, 6]
target = 4

sol = Solution
print(sol.searchInsert(sol, nums, target))

