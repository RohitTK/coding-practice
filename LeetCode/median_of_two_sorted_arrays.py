from typing import List

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []

        ctr1 = ctr2 = 0

        while ctr1 < len(nums1) and ctr2 < len(nums2):
            if nums1[ctr1] < nums2[ctr2]:
                merged.append(nums1[ctr1])
                ctr1 += 1
            else:
                merged.append(nums2[ctr2])
                ctr2 += 1

        if ctr1 < len(nums1):
            merged.extend(nums1[ctr1:])
        elif ctr2 < len(nums2):
            merged.extend(nums2[ctr2:])

        if len(merged) % 2 == 0:
            return (merged[len(merged) // 2] + merged[(len(merged) // 2) - 1]) / 2
        else:
            return merged[len(merged) // 2]
