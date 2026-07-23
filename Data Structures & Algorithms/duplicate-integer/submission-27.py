class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lista = []
        for i in nums :
            if i not in lista :
                lista.append(i)
            else:
                return True 
        return False 
