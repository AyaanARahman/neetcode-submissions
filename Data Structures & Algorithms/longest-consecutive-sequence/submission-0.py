class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            #check if start of sequence; has no left neighbors (n-1 doesn't exist in numset)
            if (num - 1) not in numSet:
                length = 0
                #checks current number
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest