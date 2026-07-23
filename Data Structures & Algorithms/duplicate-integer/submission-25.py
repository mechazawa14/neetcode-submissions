class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seta = set()
        for i in nums :
            if i not in  seta :
                seta.add(i)
            else :
                return True 
        return False 
        