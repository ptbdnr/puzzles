"""Find the maximized sum of min(ai, bi) for all i.

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
"""

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        out = 0
        for i in range(0, len(nums), 2):
            out += nums[i]
        return out
