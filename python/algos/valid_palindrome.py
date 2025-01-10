"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr, alphanum = [], string.ascii_lowercase + string.digits
        arr = [c for c in s.lower() if c in alphanum]
        return arr == arr[::-1]
