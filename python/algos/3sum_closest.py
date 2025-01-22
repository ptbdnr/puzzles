"""Find 3 integers such that the sum is closest to target.

Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
"""

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest, closest_delta = None, float("inf")
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total

                sum_delta = abs(total - target)
                if sum_delta < closest_delta:
                    closest = total
                    closest_delta = sum_delta

                if total < target:
                    left += 1
                if total > target:
                    right -= 1
        return closest

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # 2
