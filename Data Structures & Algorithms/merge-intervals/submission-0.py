class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()              # Sort by start
        res = []
        current = intervals[0]        # Interval we're merging

        for i in range(1, len(intervals)):

            if intervals[i][0] > current[1]:
                # No overlap → save current, start new one
                res.append(current)
                current = intervals[i]

            else:
                # Overlap → expand current
                current = [
                    min(current[0], intervals[i][0]),
                    max(current[1], intervals[i][1])
                ]

        res.append(current)           # Don't forget the last interval
        return res