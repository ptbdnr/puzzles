"""You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        beg, prev = None, None
        for v in nums:
            if beg is None:
                beg = v
            elif prev is None and beg + 1 == v:
                prev = v
            elif prev is None:
                ranges.append(f"{beg}")
                beg = v
            elif prev is not None and prev + 1 == v:
                prev = v
            else:
                ranges.append(f"{beg}->{prev}")
                beg, prev = v, None

        if beg is not None and prev is None:
            ranges.append(f"{beg}")
        elif beg is not None and prev is not None:
            ranges.append(f"{beg}->{prev}")
        
        return ranges
