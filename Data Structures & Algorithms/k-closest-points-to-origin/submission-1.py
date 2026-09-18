class Solution:  
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # theres literally no way we can guess which points are closer or farther from the origin and by how much until we use the distance formula first on all of them , much less that we find k closest of  em , so first just calculate distances 
        self.distances  = []
     
        for i in points :
            d = i[0]**2 +  i[1]**2 
            self.distances.append((-d, i)) 
            
        # say we had points  [[0,2],[2,0],[2,2]] till  now we got d = [4,4, 8]
        # ofc next is heapification process but we need a way to connect the distance with the coordinate we got it from in  the points, now heap is a great tool as it allows us to store a tuple in it, heapification will be done based on the first element of the tuple no stress , so order if maintained 

# also using a dict for keeping track of distances is a bad idea as multiple coordinates have same distance but duplicate keys cannot exist in a dict 
        heapq.heapify(self.distances)
        # atp we get distances = [(-8, [2,2]),(-4, [0,2]),(-4, [2,0])] aka sorted 
        self.k = k #btw were doing self.k just for fun ,simply k also works 
        # k closest = k smallest values in distances 
        while len(self.distances) > self.k:
            heapq.heappop(self.distances)
        
        # for i , j in self.distances :
        #     i = -i  order doesnt matter in which we return so this isnt needed 
        ans = []
        for  i in self.distances :
            ans.append(i[1])
        
        return ans 


        



      
       





            