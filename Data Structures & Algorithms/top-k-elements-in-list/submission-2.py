class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #count occurances of each value
        # 1, 1, 2, 3 
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arry = []

        for num, cnt in count.items():
            arry.append([cnt, num])
        arry.sort()

        answer = []
        
        while (k > 0):
            answer.append(arry.pop(len(arry)-1)[1])
            print(answer)
            k -= 1
        return answer
        


        


        