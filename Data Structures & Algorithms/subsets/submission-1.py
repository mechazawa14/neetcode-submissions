# The Goal: "I have run out of numbers to look at, save a snapshot copy of what I have."
# The Left Branch: "Put this number in the basket and go explore everything that can happen."
# The Clean Up: "Take that number back out of the basket."
# The Right Branch: "Now go explore everything that happens without that number."

#in this problem we do not have constraint otherwise wed have to include that too
#in this prblem we wanted all the possible subsets , in some cases wed not want all the 
#nodes , thats where constraints come in 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result  = []

        def backtracking(index, path):
            #1. goal 
            if index == len(nums) : #if index == 3 > 2(max index)
                result.append(path[:])
                return 
            #2.left choice 
            path.append(nums[index])
            backtracking(index+1, path)
            path.pop() #3.clean up 

            #4. right choice 
            backtracking(index+1, path)
        backtracking (0 , [])
        return result

