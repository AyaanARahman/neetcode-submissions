class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Search space = possible eating speeds
        # Slowest possible = 1 banana/hour
        # Fastest needed = largest pile (finish it in 1 hour)
        left = 1
        right = max(piles)

        res = right  # Worst-case valid answer

        while left <= right:

            # Try the middle eating speed
            k = (left + right) // 2

            hours = 0  # Total hours needed at speed k

            # Calculate how many hours each pile takes
            for p in piles:
                hours += math.ceil(p / k)

            # k is fast enough → try a slower speed
            if hours <= h:
                res = min(res, k)
                right = k - 1

            # k is too slow → need a faster speed
            else:
                left = k + 1

        return res