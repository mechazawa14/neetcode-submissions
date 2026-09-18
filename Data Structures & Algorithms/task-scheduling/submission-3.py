class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter 
        count  = Counter(tasks)
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)
        time = 0
        
        while heap:
            temp = []
            for _ in range(n+1):
                if heap:
                        freq = heapq.heappop(heap)
                        freq+=1 
                        if freq :
                            temp.append(freq)
                time+=1 
                if not temp and not heap:
                    break 
            for freq in temp :
                    heapq.heappush(heap, freq)
        return time 
             

