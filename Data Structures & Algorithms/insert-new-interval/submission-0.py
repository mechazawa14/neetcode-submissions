class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # if new interval come literally before the interval then simply add to result separately first 
            if newInterval[1] < intervals[i][0] :
                res.append(newInterval)
                return res + intervals[i:]
            # if the new intrval comes fully after an interval 
            elif newInterval[0] > intervals[i][1]:
                # just append this to result first 
                res.append(intervals[i])
                # but we dont return it just yt as further intervals may also be added in this
            # the newinterval might be overlapping with intervals on the right so 
            else :
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1], intervals[i][1])]
                 
        res.append(newInterval)
        return res
