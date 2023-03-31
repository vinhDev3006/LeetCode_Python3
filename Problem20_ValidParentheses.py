"""
Exercise 14: Longest Common PreFix
URL: https://leetcode.com/problems/longest-common-prefix
Runtime: 30 ms, Beat: 78.73%
Memory: 13.9 MB, Beat: 58.61%
Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
"""
import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        closingToOpen = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        appeared = []

        if len(s) % 2 == 1 or s[0] in closingToOpen.keys():
            return False

        for i in range(len(s)):
            if s[i] not in closingToOpen.keys():
                appeared.append(s[i])
            else:
                if appeared and closingToOpen.get(s[i]) == appeared[-1]:
                    appeared.pop()
                else:
                    return False

        return not appeared


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.testcase1 = "(){}[]"
        self.testcase2 = "([]){}"
        self.testcase3 = "{]"
        self.testcase4 = "}("
        self.testcase5 = "(){}]["

    def test_test_case_1(self):
        self.assertEqual(True, self.solution.isValid(self.testcase1))

    def test_test_case_2(self):
        self.assertEqual(True, self.solution.isValid(self.testcase2))

    def test_test_case_3(self):
        self.assertEqual(False, self.solution.isValid(self.testcase3))

    def test_test_case_4(self):
        self.assertEqual(False, self.solution.isValid(self.testcase4))

    def test_test_case_5(self):
        self.assertEqual(False, self.solution.isValid(self.testcase5))

if __name__ == "__main__":
    unittest.main()