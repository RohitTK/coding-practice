"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""


class Solution:
    # Logic: Build a hashmap with containing character count of the source string
    # Iterate the second string subtracting the count from the hashmap.
    # If 0, then it is an anagram, or it is not an anagram
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for i in s:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] = hash_map[i] + 1

        for i in t:
            if i not in hash_map:
                return False
            else:
                hash_map[i] = hash_map[i] - 1

        for i in hash_map.values():
            if i != 0:
                return False

        return True


testcases = [["anagram", "nagaram"],
             ["rat", "car"]]

sol = Solution()

for testcase_source, testcase_target in testcases:
    print('Input Strings:', testcase_source, testcase_target,
          '\nIs Anagram:', sol.isAnagram(testcase_source, testcase_target), '\n')
