class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        muneer = set()
        for i in nums:
            if i in muneer:
                return True
            muneer.add(i)
        return False
