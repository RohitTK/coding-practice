from typing import List

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


class Solution:
    # Logic: Run in two iterations
    # In first iteration, store the product of the left side values of the array
    # In second iteration, instead of doing the same, to reduce storage complexity,
    # store the product of the right part values in a variable and multiply it with the values that was created by left
    # Runtime complexity: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        left = 1
        for i in range(1, len(nums)):
            left *= nums[i - 1]
            res[i] = left

        right = 1
        for i in range(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            res[i] *= right

        return res


testcases = [[1, 2, 3, 4],
             [-1, 1, 0, -3, 3]]

sol = Solution()

for testcase in testcases:
    print('List:', testcase,
          '\nResultant List: ', sol.productExceptSelf(testcase), '\n')
