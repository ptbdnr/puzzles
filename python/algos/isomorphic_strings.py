"""Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        prev_s, prev_t = s[0], t[0]
        tbl_s = {prev_s: prev_t}
        tbl_t = {prev_t: prev_s}
        for i in range(len(s)):
            if s[i] == prev_s and t[i] == prev_t:
                continue
            elif s[i] != prev_s and t[i] != prev_t:
                prev_s = s[i]
                prev_t = t[i]
                if prev_s in tbl_s and tbl_s[prev_s] != prev_t:
                    return False
                elif prev_t in tbl_t and tbl_t[prev_t] != prev_s:
                    return False
                else:
                    tbl_s[prev_s] = prev_t
                    tbl_t[prev_t] = prev_s
            else:
                return False
        return True
