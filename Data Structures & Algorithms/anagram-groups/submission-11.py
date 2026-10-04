class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedanas = {}
        result = []
        for i in range(len(strs)):
            sortedana = ''.join(sorted(strs[i]))
            if sortedana in sortedanas:
                sortedanas[sortedana].append(strs[i])
            else:
                sortedanas[sortedana] = [strs[i]]
        for i in sortedanas :
            result.append(sortedanas[i])
        return result