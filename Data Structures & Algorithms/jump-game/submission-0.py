class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) ==  1:
            return True 
        
        # for i in range(len(nums)):
        #     maxjump  = nums[i]
        #     # the choice now is to jump by how much 
        #     if 
        # clearly a double loop is needed i feel or no lets just try while 
        # while i < len(nums):
        #     maxjump  = nums[i] 
        #     # 1. choice now is to jump or not and by how much 

        # ok found the idea : start from the end , and keep updating goal as we move backwards , aka if we have [1,2,1,4] we start at 4 as goal then we check if the prev index can help us get to goal is it does we make that position as our new goal and so on backwards , so eventually as we  keep proceeding if it is a proper list whose final index can be reached then at last our starting index should end upas our goal or else it means that we cant reach the final index and return False 
        goal = len(nums)-1 
        
        for i in range (len(nums)-1, -1, -1):
            if i + nums[i]  >= goal : #jump 
                goal  = i 
        return True if goal == 0 else False 
        
            