class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts =  [[] for i in range(len(nums)+1)]
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1 
        
        for value , count in freq.items():
            counts[count].append(value)

        result  = []
        for i in range(len(counts)-1, -1, -1):
            for j in counts[i]:
                result.append(j)

                if len(result)== k :
                    return result 
            
        
        

        
        

        