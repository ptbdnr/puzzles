"""Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for i in range(numRows):
            # initialize the number of numbers in a given pascal's triangle row with 1
            row = [1] * (i+1)
            if i > 1:
                last_row = triangle[-1]
                for j in range(1,i):
                    row[j] = last_row[j-1]+last_row[j]
                triangle.append(row)
            else:
                triangle.append(row)
        return triangle
