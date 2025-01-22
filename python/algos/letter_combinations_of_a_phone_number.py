"""Return all possible letter combinations.

Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        d2c = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(remaining_text: str, path: list):
            if not remaining_text:
                res.append("".join(path))
                return
            for c in d2c[remaining_text[0]]:
                self.dfs(remaining_text[1:], [*path, c])

        dfs(digits, [])
        return res

