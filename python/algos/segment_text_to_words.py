"""Write a function that determines whether a given input text can be completely segmented into the words of a given vocabulary."""

from collections import List


class Solution:
    """A class to determine if a text can be segmented into words from a given vocabulary."""

    def segment(self, text: str, vocabulary: List[str]) -> bool:
        """Determine whether the given text can be completely segmented into words from the given vocabulary.

        Args:
            text (str): The input text to be segmented.
            vocabulary (List[str]): The list of words to segment the text.

        Returns:
            bool: True if the text can be segmented, False otherwise.

        """
        if len(text) == 0:
            return True
        candidate_words = [w for w in vocabulary if len(text) >= len(w) and text[:len(w)] == w]
        if candidate_words:
            results = [self.segment(text[len(w):], vocabulary) for w in candidate_words]
            return any(results)
        return False

s = Solution()

print(s.segment(
    text="pinkapplepenapple",
    vocabulary=["apple", "pen", "pink", "penguin"],
))

print(s.segment(
    text="pinkapplepenguinapple",
    vocabulary=["apple", "pen", "pink", "penguin"],
))

print(s.segment(
    text="d",
    vocabulary=["a", "b", "c"],
))
