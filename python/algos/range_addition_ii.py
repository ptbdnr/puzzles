"""Identify area of max value range.

You are given an m x n matrix M initialized with all 0's and 
an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
Count and return the number of maximum integers in the matrix after performing all the operations.
"""

class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        # if len(ops) == 0:
        #     return m*n
        # if len(ops) == 1:
        #     op = ops[0]
        #     return op[0] * op[1]
        # mat = [[0 for _ in range(n)] for _ in range(m)]
        # for (op_r, op_c) in ops:
        #     for r in range(op_r):
        #         for c in range(op_c):
        #             mat[r][c] += 1
        # counter = {k: 0 for k in range(len(ops)+1)}
        # for r in range(m):
        #     for c in range(n):
        #         counter[mat[r][c]] += 1
        # return counter[len(ops)]

        r, c = m, n
        for (op_r, op_c) in ops:
            r = min(r, op_r)
            c = min(c, op_c)
        return r*c
