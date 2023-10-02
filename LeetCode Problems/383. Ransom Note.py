"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

https://leetcode.com/problems/ransom-note/
"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # count number of each alphabet in string
        s1, s2 = Counter(ransomNote), Counter(magazine)
        # bitwise and operation to check if ransomeNote sring can be constructed using magazine string
        return s1 & s2 == s1