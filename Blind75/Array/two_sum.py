from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}    # Create an empty hash map to store the values
        # Logic: x + y = tgt, then y = tgt - x.
        # While iterating through the given list, you insert y in the hashmap along with its index
        # When iterating, if you find x in the hashmap, you return current index and the index of found element
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            else:
                hashmap[target - nums[i]] = i


testcases = [[[2, 7, 11, 15], 9],
             [[3, 2, 4], 6],
             [[3, 3], 6]]

sol = Solution()


for testcase in testcases:
    print('Num List:', testcase[0],
          'Target List: ', testcase[1],
          '\nOutput: ', sol.twoSum(testcase[0], testcase[1]), '\n')
