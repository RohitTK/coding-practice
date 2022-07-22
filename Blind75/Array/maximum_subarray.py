from typing import List

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""


class Solution:
    # Logic: Dynamic Programming
    # Just imagine an array A[n]. And imagine we have a solution for A[1 ... i-1].
    # Now we try to check if adding A[i] to the subarray solution is maximum,
    # If adding doesn't improve the solution, it would imply that A[i] is the Maximum Sub Array
    # Runtime Complexity: O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        temp = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            temp = max(temp + nums[i], nums[i])
            max_sum = max(temp, max_sum)
        return max_sum


testcases = [[-2, 1, -3, 4, -1, 2, 1, -5, 4],
             [1],
             [5, 4, -1, 7, 8]
             ]

sol = Solution()

for testcase in testcases:
    print('List:', testcase,
          '\nMax Sum: ', sol.maxSubArray(testcase), '\n')
