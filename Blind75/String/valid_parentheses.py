"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


class Solution:
    # Logic: Maintain a hash map for closing brackets and a stack to insert opening brackets
    # Pop from stack if a closing bracket is met or keep inserting into the stack
    def isValid(self, s: str) -> bool:
        temp_queue = []
        closing_brackets_hash = {')': '(', ']': '[', '}': '{'}
        for i in s:
            t = closing_brackets_hash.get(i)
            if t and len(temp_queue) > 0:
                p = temp_queue.pop()
                if p != t:
                    return False
            else:
                temp_queue.append(i)

        if len(temp_queue) == 0:
            return True
        else:
            return False


testcases = ["()",
             "()[]{}",
             "(]"]

sol = Solution()

for testcase in testcases:
    print('Input String:', testcase,
          '\nAre parentheses valid?:', sol.isValid(testcase), '\n')
