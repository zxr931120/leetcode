# O(n) solution, accepted
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxSum = nums[0]
        currentSum = 0

        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum > maxSum:
                maxSum = currentSum

            if currentSum < 0:
                currentSum = 0

        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution
print(sol.maxSubArray(sol, nums))











# O(n^2) solution, not acceptable because of time limit exceed
# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         maxSum = nums[0]
#         maxSA = nums[0]
#
#         for i in range(len(nums)):
#
#             sumOfSubStartFromI = nums[i]
#             if sumOfSubStartFromI > maxSum:
#                 maxSum = sumOfSubStartFromI
#                 maxSA = nums[i]
#
#             if i == len(nums) - 1:
#                 break
#
#             for j in range(i + 1, len(nums)):
#                 sumOfSubStartFromI += nums[j]
#                 if sumOfSubStartFromI > maxSum:
#                     maxSum = sumOfSubStartFromI
#                     maxSA = nums[i:j + 1]
#
#         print('MaxArray: ', maxSA)
#         print('Its sum: ', maxSum)
#
#         return maxSum
#
#

