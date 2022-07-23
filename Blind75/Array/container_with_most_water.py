from typing import List

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""


class Solution:
    # Logic: The water level is usually up to the smaller side
    # If the left height is less, shift to the next line.
    # Else if the height is more, shift the right to left hoping to increase the height
    # Runtime Complexity: O(n)
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_vol = 0

        while l < r:
            vol = min(height[l], height[r]) * (r - l)
            max_vol = max(max_vol, vol)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_vol


testcases = [[1, 8, 6, 2, 5, 4, 8, 3, 7],
             [1, 1]
             ]

sol = Solution()

for testcase in testcases:
    print('List:', testcase,
          '\nMax Area: ', sol.maxArea(testcase), '\n')
