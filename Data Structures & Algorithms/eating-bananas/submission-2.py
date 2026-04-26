class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1 , max(piles)
        result  = right #we start with a safe rate that will definitely work 
        # which is the maximum number of bananas in a pile 
        while left <= right :
            hours = 0
            rate  = (left+right)//2 
            for pile in piles :
                hours +=  math.ceil(pile/rate)
            if hours <= h :
                result = min(result, rate)
                right = rate -1 
            else:
                left  = rate +1
        return result 
            

        



            

