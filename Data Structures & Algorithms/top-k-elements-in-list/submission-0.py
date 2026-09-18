class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = []
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        print(arr)
        
        while len(res) < k:
            res.append(arr.pop()[1]) #pops last element (most frequent)
        return res
        
        
