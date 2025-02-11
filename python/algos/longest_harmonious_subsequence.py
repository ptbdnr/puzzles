"""Determine length of longest harmonious subseqence.

We define a harmonious array as an array 
where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious 
subsequence among all its possible subsequences.
"""

from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        tbl = Counter(nums)
        vals = sorted(tbl.keys())
        res = 0
        for vi in range(len(vals)-1):
            if vals[vi] + 1 == vals[vi+1]:
                res = max(res, tbl[vals[vi]] + tbl[vals[vi+1]])
        return res
