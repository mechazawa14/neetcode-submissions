class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        newinterval = intervals[0]

        for i in range(1, len(intervals)):

            # NO OVERLAP
            if newinterval[1] <= intervals[i][0]:
                newinterval = intervals[i]

            # OVERLAP
            else:
                res += 1
                if newinterval[1] < intervals[i][1]:
                    continue 
                else:
                    newinterval = intervals[i]

        return res