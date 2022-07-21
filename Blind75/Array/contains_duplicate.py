from typing import List

"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution:

    # Logic: Using brute force
    # Runtime complexity: O(n*n)
    def containsDuplicate1(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

    # Logic: Using sort
    # Runtime complexity: O(nlogn)
    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True

        return False

    # Logic: Using a hashmap
    # Runtime complexity: O(n)
    def containsDuplicate3(self, nums: List[int]) -> bool:
        hash = {}
        for i in nums:
            if i in hash:
                return True
            hash[i] = 1

        return False

    # Logic: Using Python set and list
    def containsDuplicate4(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


testcases = [[1, 2, 3, 1],
             [1, 2, 3, 4],
             [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]

sol = Solution()

print('Using BruteForce', '-' * 30)
for testcase in testcases:
    print('List:', testcase,
          '\nContains Duplicate?: ', sol.containsDuplicate1(testcase), '\n')

print('Using Sort', '-' * 30)
for testcase in testcases:
    print('List:', testcase,
          '\nContains Duplicate?: ', sol.containsDuplicate2(testcase), '\n')

print('Using Hashmap', '-' * 100)
for testcase in testcases:
    print('List:', testcase,
          '\nContains Duplicate?: ', sol.containsDuplicate3(testcase), '\n')


print('Using Python set', '-' * 100)
for testcase in testcases:
    print('List:', testcase,
          '\nContains Duplicate?: ', sol.containsDuplicate4(testcase), '\n')
