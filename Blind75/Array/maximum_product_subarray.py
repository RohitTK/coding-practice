from typing import List

"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution:
    # Logic: Dynamic Programming.
    # Similar to maximum subarray. Instead, we now maintain two values, 1 for min and 1 for max and keep updating them.
    # At every iteration, either multiply the element to the existing product or consider the new element directly.
    # If in the number is negative in the current iteration, we swap out the max and min values
    # because max becomes min when multiplied with a small number and vice versa
    # Runtime Complexity: O(n)
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        min_product = max_product = result

        for i in range(1, len(nums)):

            if nums[i] < 0:
                min_product, max_product = max_product, min_product

            min_product = min(nums[i], min_product * nums[i])
            max_product = max(nums[i], max_product * nums[i])

            result = max(result, max_product)

        return result


testcases = [[2, 3, -2, 4],
             [-2, 0, -1],
             ]

sol = Solution()

for testcase in testcases:
    print('List:', testcase,
          '\nMax Product: ', sol.maxProduct(testcase), '\n')
