"""
Problem 1337: The K Weakest Rows in a Matrix
URL: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix
Runtime: 99 ms, Beats: 99.16% 
Memory: 14.1 MB, Beats: 81.13%
Description: You are given an m x n binary matrix mat of
1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example:
Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers in each row is:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
The rows ordered from weakest to strongest are [2,0,3,1,4].
"""
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count_dict = {}
        for i, row in enumerate(mat):
            count = row.count(1)
            if count in count_dict:
                count_dict[count].append(i)
            else:
                count_dict[count] = [i]

        sorted_keys = sorted(count_dict.keys())
        result = []
        for key in sorted_keys:
            if len(result) >= k:
                break
            result.extend(count_dict[key])
        return result[:k]


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]

k = 3

solution = Solution()
print(solution.kWeakestRows(mat, k))