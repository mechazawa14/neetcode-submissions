class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq  #just a toolkit for operations on heap later 
        self.heap = nums #making it self. so as to keep it for usage in later fuctions like in add 
        self.maxwhichweneed = k 
        # only one heapification is enough in start 
        heapq.heapify(self.heap)
        # now never again is heapification needed even as we pop or add it is self maintained as a min heap 
        # now incase the heap we just made has more than k elems thos e extra elems must be culled 
        while len(self.heap) > self.maxwhichweneed :
            heapq.heappop(self.heap)
# return nothing as return is in add as per the question

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # now after adding incase the lenght became more than needed 
        while  len(self.heap) > self.maxwhichweneed:
            heapq.heappop(self.heap)
        return self.heap[0]



        
