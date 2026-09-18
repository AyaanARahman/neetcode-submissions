class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums:
            if num not in countMap:
                countMap[num] = 1
            else:
                countMap[num] += 1

        arr = []
        for num, cnt in countMap.items():
            arr.append([cnt,num])
        arr.sort()
            
        res = []
        while (k > 0):
            res.append(arr.pop()[1])
            k -= 1

        return res




        


        


        