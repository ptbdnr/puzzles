"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, out = 0, 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                if curr > out:
                    out = curr
                curr = 0
        if curr > out:
            return curr
        return out
