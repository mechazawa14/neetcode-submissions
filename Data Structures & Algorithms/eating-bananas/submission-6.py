class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left  = 1
        right  = max(piles)
        result= right 
        while left <= right :
            rate  = (right + left)//2 
            hours = 0 
            for pile in piles : 
                hours += math.ceil(pile/rate)
                
            if hours <= h:
                result  = min(result , rate )
                right = rate -1 
            if hours > h:
                left = rate + 1
        return result 
                        