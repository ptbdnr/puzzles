"""Define if student is eligible for an attendance award.

You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.
"""

MAX_ATTENDANCE = 1
MAX_CONSECUTIVE_LATE = 2

class Solution:
    def checkRecord(self, s: str) -> bool:
        a, curr_l, max_l = 0, 0, 0
        prev = 0
        for c in s:
            if c == "A":
                a += 1
            elif c == "L":
                if prev == "L":
                    curr_l += 1
                    max_l = max(max_l, curr_l)
                else:
                    prev = c
                    curr_l = 1
            prev = c
        return a <= MAX_ATTENDANCE and max_l < MAX_CONSECUTIVE_LATE
