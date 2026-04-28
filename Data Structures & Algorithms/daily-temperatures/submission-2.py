class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range (len(temperatures)):
            nextwarmer  = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i] :
                    nextwarmer  = j-i
                    break 
            res.append(nextwarmer)
        return res 