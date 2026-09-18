class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # clearly as heapifu makes  the list a min heap  which means heapop will pop the smallest elem aka the root of the heap tree , this means that to get largest elem the trick is to multiply the whole array with - and then now the largest will technically be the smallest and now it can be removed using heappop  
        self.heap = stones 
        self.stones = [-x for x in self.heap]
        heapq.heapify(self.stones)

        while len(self.stones) > 1 :
            heavieststone1 = heapq.heappop(self.stones)
            heavieststone2 = heapq.heappop(self.stones)
            diff = abs(heavieststone1) - abs(heavieststone2)
            if diff !=  0 :
                heapq.heappush(self.stones, -diff)
        if not self.stones:
            return 0 
        return -self.stones[0]
            

