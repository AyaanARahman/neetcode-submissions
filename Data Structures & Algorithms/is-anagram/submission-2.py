class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for char in s:
            if char not in countS:
                countS[char] = 1
            else:
                countS[char] += 1
        for char in t:
            if char not in countT:
                countT[char] = 1
            else:
                countT[char] += 1
        
        if countS != countT:
            return False

        return True
        