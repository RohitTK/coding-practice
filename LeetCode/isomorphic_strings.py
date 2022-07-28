"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map_s_t = {}
        hash_map_t_s = {}

        for i in range(len(s)):

            if (s[i] in hash_map_s_t and hash_map_s_t[s[i]] != t[i]) \
                    or (t[i] in hash_map_t_s and hash_map_t_s[t[i]] != s[i]):
                return False

            hash_map_s_t[s[i]] = t[i]
            hash_map_t_s[t[i]] = s[i]

        return True


testcases = [["egg", "add"],
             ["foo", "bar"],
             ["paper", "title"]]

sol = Solution()

for testcase in testcases:
    print('Source String:', testcase[0],
          '\nTarget String:', testcase[1],
          '\nIsomorphic?:', sol.isIsomorphic(testcase[0], testcase[1]), '\n')
