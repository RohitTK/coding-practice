from typing import List

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


class Solution:
    # Logic: Take a separate list to store the new intervals.
    # Don't forget to sort the intervals in ascending order based on start
    # In every iteration you compare with the last interval that is present in the resultant list
    # If the current interval start is greater than the end of the last interval, you just add it to the result
    # If the current interval start is less than the last interval's end of the list, you perform a merge

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        for i in sorted(intervals, key=lambda i: i[0]):
            if len(result) > 0 and result[-1][1] >= i[0]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)

        return result


testcases = [[[1, 3], [2, 6], [8, 10], [15, 18]],
             [[1, 4], [4, 5]]]

sol = Solution()

for testcase in testcases:
    print('Intervals:', testcase,
          '\nOutput: ', sol.merge(testcase), '\n')
