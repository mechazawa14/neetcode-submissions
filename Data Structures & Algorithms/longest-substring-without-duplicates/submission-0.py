class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        charseen  = set()
        maxlen = 0
        
        for right in range(len(s)):
            while s[right] in charseen :
                charseen.remove(s[left])
                left+=1 
            charseen.add(s[right])
            maxlen = max(maxlen , right-left+1)
        return maxlen