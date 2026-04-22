class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedanas = {}

        for i in strs :
            sortedstring = ''.join(sorted(i))
            if sortedstring in sortedanas :
                sortedanas[sortedstring].append(i)
            else :
                sortedanas[sortedstring] = [i]
        return list(sortedanas.values())
        

