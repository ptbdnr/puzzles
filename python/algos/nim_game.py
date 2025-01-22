"""Define if you can win the Nim Game.

Nim Game:
Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

"""

import sys

MIN_SELECT = 1
MAX_SELECT = 3

class Solution:
    def canWinNim(self, n: int) -> bool:
        #| Rely on the fact that if n % 4 == 0, then the opponent can always win
        return n % (MAX_SELECT+1) != 0

        #| Explicitly check all scenarios
        return self.explicit(n)

        #| Enumerate: even step is mine, odd step is of opponent
        return self.dfs(n, 0)

    def explicit(self, n: int) -> bool:
        """Check all initial scenarios."""
        scenarios = []
        for i in range(MIN_SELECT, MAX_SELECT+1):
            if i <= n:
                win = (n-i) % (MAX_SELECT+1) == 0
                scenarios.append(win)
        return any(scenarios)

    def dfs(self, n: int, lvl: int) -> bool:
        """Enumerate all scenarios."""
        if n <= MAX_SELECT:
            return lvl % 2 == 0

        scenarios = []
        for i in range(MIN_SELECT, MAX_SELECT+1):
            win = self.dfs(n-i, lvl+1)
            if lvl % 2 == 0 and win: # my turn
                return True
            # opponent's turn
            scenarios.append(win)

        return all(scenarios)

if __name__ == "__main__":
    n = 33
    sol = Solution()
    sys.exit(sol.canWinNim(n))
