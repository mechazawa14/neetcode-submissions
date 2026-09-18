class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq 
        self.hoopa = nums 
        self.thlargestweneed = k 
        heapq.heapify(self.hoopa)
        while len(self.hoopa) > self.thlargestweneed:
            heapq.heappop(self.hoopa)

    def add(self, val: int) -> int:
        heapq.heappush(self.hoopa, val)
        while len(self.hoopa) > self.thlargestweneed:
            heapq.heappop(self.hoopa)

        return self.hoopa[0]

