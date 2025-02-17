"""Identify set mismatch.

You have a set of integers s,
which originally contains all the numbers from 1 to n.
Unfortunately, due to some error,
one of the numbers in s got duplicated to another number in the set,
which results in repetition of one number and loss of another number.
You are given an integer array nums
representing the data status of this set after the error.
Find the number that occurs twice and the number
that is missing and return them in the form of an array.
"""

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counter = [0 for _ in range(n)]
        for v in nums:
            counter[v-1] += 1
        missing = float("-inf")
        double = float("-inf")
        for i in range(n):
            if not counter[i]:
                missing = i+1
            if counter[i] == 2:
                double = i+1
        return [double, missing]

