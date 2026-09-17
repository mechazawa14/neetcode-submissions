class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        import heapq #only a toolbox for operations on heap 
        self.k = k 
        self.heap =  nums

        heapq.heapify(self.heap)
        while  len(self.heap) > self.k :
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
    
        
    

        
