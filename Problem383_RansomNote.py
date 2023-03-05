"""
Problem 383: Ransom Note
URL: https://leetcode.com/problems/ransom-note
Beats: 90,36%
Description: Given two
strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and
false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = dict(Counter(ransomNote))
        magazine_dict = dict(Counter(magazine))
        for key, value in ransomNote_dict.items():
            if key not in magazine_dict or value > magazine_dict.get(key):
                return False
        return True


solution = Solution()
print(solution.canConstruct("aab", "baa"))