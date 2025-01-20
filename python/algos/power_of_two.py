"""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        exp = 0
        while True:
            if 2 ** (exp+1) > n:
                break
            exp += 1
        return 2 ** exp == n
