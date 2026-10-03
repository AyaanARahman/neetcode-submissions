class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * (len(nums))

        pre = 1

        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        postfix = 1

        #iterate backwards
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


        