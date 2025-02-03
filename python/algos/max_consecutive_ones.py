"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n =len(nums)
        out =0
        count =0
        for i in range(n):
            if nums[i] == 1:
                count+=1
            else:
                if count > out:
                    out =count
                count=0
        if count > out:
            return count    
        return out
