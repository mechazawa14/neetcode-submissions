class Solution:
    def jump(self, nums: List[int]) -> int:
         # backwards approach doesnt really work for this one 
       goal = len(nums) - 1 
       jumps  = 0 
       right = 0 
       left  = 0
       farthest= 0
       while right < goal:
          for i in range(left , right +1 ):
            farthest  = max(farthest , nums[i]+i)
          left = right +1 
          right  = farthest
          jumps+=1 
       return jumps 


       
          


