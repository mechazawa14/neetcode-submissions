# Think of the string s = "aab" as a single stick of wood. 
# You are walking along the stick from left to right, deciding where to saw it into pieces.
#  Every time you make a cut, the piece you just cut off must be a valid palindrome.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        # Helper function to check if a substring is a palindrome
        def is_palindrome(sub_str):
            return sub_str == sub_str[::-1]

        def backtracking(index, path):
            # 1. Goal: We carved up the entire string perfectly
            if index == len(s):
                result.append(path[:])
                return

            # 2. Choices: Try cutting the string at every position from 'index' to the end
            for i in range(index, len(s)):
                # The piece we are considering cutting off
                substring = s[index:i+1]
                
                # 3. Constraint: Only recurse if this piece is a valid palindrome
                if is_palindrome(substring):
                    path.append(substring) # Make the cut
                    
                    # Move our index to 'i + 1' to process the remainder of the string
                    backtracking(i + 1, path) 
                    
                    # 4. Cleanse: Undo the cut to try a different cutting position
                    path.pop()

        backtracking(0, [])
        return result
