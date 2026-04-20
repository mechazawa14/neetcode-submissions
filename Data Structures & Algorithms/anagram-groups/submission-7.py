class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedstrings = {}
        for i in strs : 
            sortedstring= ''.join(sorted(i))
            if sortedstring in sortedstrings :
                sortedstrings[sortedstring].append(i)
            else :
                sortedstrings[sortedstring]= [i]
        
        return list(sortedstrings.values())

    
