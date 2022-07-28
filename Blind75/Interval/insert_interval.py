from typing import List

"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


class Solution:
    # Logic: Maintain left and right parts of the intervals
    # Then focus on building the new interval in between. Which is built like.
    # The start index of this new interval would be the minimum start intervals
    # And the end index would be the maximum of the end intervals
    # And return the concatenated left part, new interval and then the right part

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left_intervals, right_intervals = [], []

        new_interval_start = newInterval[0]
        new_interval_end = newInterval[1]

        for interval in intervals:
            if new_interval_start > interval[1]:
                left_intervals.append(interval)
            elif new_interval_end < interval[0]:
                right_intervals.append(interval)
            else:
                new_interval_start = min(interval[0], new_interval_start)
                new_interval_end = max(interval[1], new_interval_end)

        return left_intervals + [[new_interval_start, new_interval_end]] + right_intervals


testcases = [[[[1, 3], [6, 9]], [2, 5]],
             [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]]]

sol = Solution()

for testcase in testcases:
    print('Intervals:', testcase[0],
          '\nNew Interval:', testcase[1],
          '\nOutput: ', sol.insert(testcase[0], testcase[1]), '\n')
