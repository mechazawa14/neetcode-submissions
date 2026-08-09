class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedanas  = {}
        for string in strs:
            sortedana = "".join(sorted(string))
            if sortedana in sortedanas:
                sortedanas[sortedana].append(string)
            else:
                sortedanas[sortedana] = [string]
        return list(sortedanas.values())

            
