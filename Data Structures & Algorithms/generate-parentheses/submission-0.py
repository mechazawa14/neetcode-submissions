# the 4-step framework fits this problem like a glove.Instead of an array index, 
# your choices are driven by two simple counts:open_count: How many open parentheses 
# ( you have used so far.close_count: How many closed parentheses ) you have used so far.
# The Realignment of the 4 StepsThe Goal: If your string reaches a length of 2 * n,
#  you have used all your parentheses. Save it!The Left Choice (Add an Open Parenthesis):
#   You can always add an open parenthesis ( as long as open_count < n.The Cleanse: Since we
#    can pass strings down recursively, strings handle their own cleanup automatically
#     (unlike lists, strings create a new copy when you add to them, 
#     so we don't even need .pop()!).The Right Choice (Add a Closed Parenthesis): 
#     You can only add a closed parenthesis ) if you have more open parentheses waiting
#      to be matched (close_count < open_count).


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result  = []
        def backtracking(open_count, closed_count  , currentstring):
            if len(currentstring)==2*n:
                result.append(currentstring)
                return 
            if open_count < n:
                backtracking(open_count+1, closed_count , currentstring + "(")
            if closed_count < open_count :
                backtracking(open_count,closed_count+1, currentstring + ")" )
        backtracking (0 ,0 , "")
        return result 
