class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums)== 0:
            return 0 
        if len(nums) == 1:
            return 1
        longest_seq_yet = []
        for i in nums :
            visited = []
            if i not in longest_seq_yet :
                current_num = i 
                current_seq = [current_num]
                visited.append(i)
                while i+1 in nums and i+1 not in visited:
                    current_num = i+1 
                    current_seq.append(current_num)
                    i+=1 
                if len(current_seq) > len(longest_seq_yet):
                    longest_seq_yet = current_seq
        return len(longest_seq_yet)



        




            
