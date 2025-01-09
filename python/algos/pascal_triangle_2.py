"""Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```
"""


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [1] + [row[i-1] + row[i] for i in range(1, len(row))] + [1]
        return row
