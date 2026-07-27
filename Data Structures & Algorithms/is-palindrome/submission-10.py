class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = re.sub(r'[^a-zA-Z0-9]' , '', s).lower()
        i = 0
        j = len(s)-1
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True

