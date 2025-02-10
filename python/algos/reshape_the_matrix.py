"""Reshape the matrix.

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        mrs = len(mat)
        mcs = len(mat[0])
        if r * c != mrs * mcs:
            return mat
        out = [[0 for _ in range(c)] for _ in range(r)]
        outr, outc = 0, 0
        for mr in range(mrs):
            for mc in range(mcs):
                out[outr][outc] = mat[mr][mc]
                if outc + 1 == c:
                    outr += 1
                    outc = 0
                else:
                    outc += 1
        return out
