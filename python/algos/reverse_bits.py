class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for _ in range(32):
            b = n & 1
            rev = (rev << 1) | b
            n >>= 1
        return rev
