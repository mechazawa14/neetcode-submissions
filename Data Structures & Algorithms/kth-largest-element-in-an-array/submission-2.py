class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = nums 
        heapq.heapify(self.heap)
        # 2nd largest  = (len(nums) - 2)th smallest 
        # for i in range(k+1):
        #     heapq.heappop(self.heap) this didnt work , FUCK THIS 

        while len(self.heap) != k :
            heapq.heappop(self.heap)
# to get the second largest we can just keep the damn thing popping until we got left only 2 elems , and theyll be auto heapified wkt so dw 

            
        return self.heap[0]


