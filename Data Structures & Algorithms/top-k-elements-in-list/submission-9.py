class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}

        for i in  nums :
            count[i] = 1+ count.get(i, 0)
        
        for value, count in count.items():
            freq[count].append(value)
        
        result= []
        for i in range(len(freq) -1 ,0,  -1):
            for j in freq[i]:  
               result.append(j)
               if len(result) == k :
                   return result
            
        

        
        

        
        