"""Given a specific rectangular area, determine the length L and width W satisfying the requirements.

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
"""

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(sqrt(area))
        while area % W:
            W -= 1
        return [int(area / W), W]
