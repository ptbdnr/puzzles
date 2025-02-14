"""Get minimum index sum of 2 lists.

Given two arrays of strings list1 and list2, find the common strings with the least index sum.
A common string is a string that appeared in both list1 and list2.
A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
Return all the common strings with the least index sum. Return the answer in any order.
"""

class Solution:
    def getMinIndex(self, list1: list[str], list2: list[str]) -> list[str]:
        tbl1 = {list1[v]: v  for v in range(len(list1))}
        least, txts = len(list1) + len(list2), []
        for j_idx, j_txt in enumerate(list2):
            if j_txt in tbl1:
                if j_idx + tbl1[j_txt] < least:
                    least = j_idx + tbl1[j_txt]
                    txts = [j_txt]
                elif j_idx + tbl1[j_txt] == least:
                    txts.append(j_txt)
        return txts
