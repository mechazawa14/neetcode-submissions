class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        # we couldve also used 2 stack method like we used in minstack 
        #but here were using a monotonic stack (decreasing)
        res = [0]*len(t)
        stack = [] #contains pairs of values temp and index of that temp

        for i, temp in enumerate(t) :
            while stack and temp > stack[-1][0]:
                stackT , stackind = stack.pop()
                res[stackind] = (i-stackind)
            stack.append([temp, i])
        return res 
            
