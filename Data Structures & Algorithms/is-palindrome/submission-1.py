class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''

        for c in s:
            if c.isalnum():
                newString += c.lower()
        print (newString)
        return newString == newString[::-1]

        