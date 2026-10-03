class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #window length - most frequent character <= k is valid
        #otherwise, shrink the window and increase the left pointer

        left = 0
        right = 0
        
        maxLength = 0

        countChar = {}

        for right in range(len(s)):
            if s[right] in countChar:
                countChar[s[right]] += 1
            else:
                countChar[s[right]] = 1
            #knows the most frequent letter constantly
            mostFreq = max(countChar.values())
            print(mostFreq)
            while (right - left + 1) - mostFreq > k:
                #update the character frequency before moving the character
                countChar[s[left]] -= 1   
                left +=1   
            maxLength = max((right - left + 1), maxLength)  
        return maxLength

        
        