class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #initiatlize is to the first num in array
        maxSub = nums[0]

        #keeping track
        currSum = 0


        for num in nums:
            #if the value becomes negative, discard it
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(currSum, maxSub)
        return maxSub
        