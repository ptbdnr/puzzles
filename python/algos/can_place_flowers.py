"""Plant solitary flowers.

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0, *flowerbed, 0]

        for i in range(1, len(flowerbed)-1):
            if sum(flowerbed[i-1:i+2]) == 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0
