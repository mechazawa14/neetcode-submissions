class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
       
        count = Counter(tasks) #actually gives a hashmap 
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)
        
        # so we first got the heap queue of  the frequencies aka [-3, -2 so on]
        # say we consider ["A","A","A","B","C"], so heap =  [-3, -1, -1]
        # then we make a variable time to track the number of cycles done 
        time  =  0 
        # so now we pick the task with largest freq but before that 
        while heap : #as we keep  scheduling until i have tasks in heap 
            temp = [] #storage for cooldown 
            for _ in range(n+1):
                if heap:
                    freq = heapq.heappop(heap)
                    freq+=1 
                    if freq:
                        temp.append(freq)
                time+=1 
                if not temp and not heap:
                    break 

            for freq in temp :
                heapq.heappush(heap, freq)
        return time 
                    




         



