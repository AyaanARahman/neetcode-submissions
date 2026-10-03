class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #we're not finding an index
        #The minimum eating speed k that lets Koko finish all bananas within h hours. so left and right should represent possible speeds
        left = 1 
        right = max(piles)

        res = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        return res


        
        


        