class Twitter:

    def __init__(self):
#in init, we make the data structures that would help me make the twitter  
# will be used later in further functions which are for different actions and purposes 
        self.following = {}
        self.tweets = {}
        self.time = 0 


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        if userId in self.tweets :
            self.tweets[userId].append((self.time, tweetId))
        else:
            self.tweets[userId] = [(self.time, tweetId)]
        
    def getNewsFeed(self, userId: int) -> List[int]:
        #heapq.heapify(self.tweets[userId])#sorts according to first elem of tuple , recent time aka small time is at start of min heap 
        # if len(self.tweets) < 10 :
        #     return []
        # else :
        #     tweets  = []
        #     for time , tweet in self.tweets[userId]:
        #         tweets.append(tweet)
        # return tweets 
        usefulppl = {userId}
        if userId in self.following:
            usefulppl.update(self.following[userId])
        #so far we have the people whose tweets to be shown 
        heap1 = []
        for people in usefulppl:
            if people in self.tweets:
                for time, tweetid in self.tweets[people]:
                    heap1.append((-time, tweetid))
        heapq.heapify(heap1)
        anstweets = []
        while heap1 and len(anstweets) < 10:
            time, tweetid = heapq.heappop(heap1)
            anstweets.append(tweetid)
        return anstweets

        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            # self.following[followerId] = {followeeId} or 
            self.following[followerId] = set()
            self.following[followerId].add(followeeId)
            
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            # self.following[followerId].remove(followeeId)
            self.following[followerId].discard(followeeId)
            # set uses discard to remove not 'remove' like list 

        
