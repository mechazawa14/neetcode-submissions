class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        compliments = {}
        for i in range(len(numbers)):
            compliment  = target  - numbers[i]
            if compliment in compliments :
                return [compliments[compliment]+1 , i+1 ]
            else:
                compliments[numbers[i]] = i 
        return []