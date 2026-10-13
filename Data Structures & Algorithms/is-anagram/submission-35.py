class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        for i in s:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        dict2={}
        for i in t:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
        if dict1 == dict2:
            return True
        return False
