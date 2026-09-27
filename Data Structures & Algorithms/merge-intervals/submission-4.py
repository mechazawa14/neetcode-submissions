class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # let us initiate th new interval as the first interval in intervals 
        intervals.sort() #sort first
        newinterval  = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            # were sure of one thing that the start elem of all intervals are in ascending order aka next.start >= current.start as we sorted , so theres really only 2 conditions to check tbh 
            # 1. no over lap
            if newinterval[1] < intervals[i][0]: # no overlap
                res.append(newinterval)
                newinterval = intervals[i]

            # 2. next interval starts after the first interval fully ends [1,2],[3,4]
            else:
                newinterval = [min(newinterval[0], intervals[i][0]), max(newinterval[1], intervals[i][1])]
        
        res.append(newinterval)
        return res

            