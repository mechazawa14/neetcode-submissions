class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dummy = []
        for i in nums :
            if i not in dummy :
                dummy.append(i)
            else :
                return True 
        return False 