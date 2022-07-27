from typing import List

"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""


class Solution:
    # Logic: Store row and column positions in an array wherever a zero is encountered
    # Runtime Complexity: O(m * n) Space:complexity: O(m + n)
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        row = []
        col = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j] = 0

    # Marking the first row and column values as 0
    # and iterate again marking all the respective column and row values with 0
    # Runtime Complexity: O(m * n) Space:complexity: O(1)
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        isColFlag = 0
        noOfRows = len(matrix)
        noOfCols = len(matrix[0])

        for i in range(noOfRows):
            # Check for 0s in the first column and store it in a flag
            if matrix[i][0] == 0:
                isColFlag = 1

            # Marking 0s in the first row and columns if the value has 0 (Ignore the first column)
            for j in range(1, noOfCols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Using the marked values, fill 0s for all the needed values except the first row and column
        for i in range(1, noOfRows):
            for j in range(1, noOfCols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # If the first value is 0 mark all the values in the first row with 0s
        if matrix[0][0] == 0:
            for i in range(noOfCols):
                matrix[0][i] = 0

        # Mark first column with 0s if we marked above that the first columns needs to 0
        if isColFlag == 1:
            for i in range(noOfRows):
                matrix[i][0] = 0

