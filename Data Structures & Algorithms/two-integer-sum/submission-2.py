class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mathMap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in mathMap:
                return [mathMap[complement], i]
            mathMap[num] = i
            