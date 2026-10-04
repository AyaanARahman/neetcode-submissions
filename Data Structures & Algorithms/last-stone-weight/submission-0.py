import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        n = len(stones)
        print(stones)
        
        for i in range(n):
            stones[i] = -stones[i]
            print(stones)
        heapq.heapify(stones)

        while len(stones) >= 2:
            firstStone = heapq.heappop(stones)
            secondStone = heapq.heappop(stones)
            firstStone,secondStone = -firstStone, -secondStone

            if firstStone == secondStone:
                continue
            elif firstStone < secondStone:
                pushVal = (secondStone - firstStone)
                pushVal = -pushVal
                heapq.heappush(stones, pushVal)
            elif firstStone > secondStone:
                pushVal = (firstStone - secondStone)
                pushVal = -pushVal
                heapq.heappush(stones, pushVal)

        if len(stones) > 0:
            return -stones[0]
        
        return 0


        



        