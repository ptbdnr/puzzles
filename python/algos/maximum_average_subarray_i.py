"""Compute maximum average subarray.

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(len(nums)-k):
            curr_sum = curr_sum - nums[i] + nums[i+k]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k
