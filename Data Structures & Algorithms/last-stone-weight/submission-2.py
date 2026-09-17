class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        self.heap  = [-x for x in stones]
        heapq.heapify(self.heap)

        while  len(self.heap) > 1 :
            h1 = heapq.heappop(self.heap) 
            h2 = heapq.heappop(self.heap)
            y = abs(h1)- abs(h2) 
            if  y!= 0:
                heapq.heappush(self.heap, -y)
        if not len(self.heap):
            return 0
        return -(self.heap[0])
