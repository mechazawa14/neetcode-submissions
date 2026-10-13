class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        muneer = set()
        for i in nums:
            if i not in muneer:
                muneer.add(i)
            else:   
                return True
        return False
