class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dummy = []
        for i in nums :
            if i in dummy :
                return True
            else :
                dummy.append(i)
        return False 
