class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            #if the new end time comes before the start time
            #append the new interval to the beginning of th elist
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                #python slicing to add the rest of the intervals in
                return res + intervals[i:]
            #if the start time of the new interval is greater than the end
            #time of the current interval, make sure the OG interval is
            #added first
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res

        