class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seta = []
        for i in nums :
            if i not in  seta :
                seta.append(i)
            else :
                return True 
        return False 
