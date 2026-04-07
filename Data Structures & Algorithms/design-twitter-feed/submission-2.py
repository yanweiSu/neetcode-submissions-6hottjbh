class Twitter:

    def __init__(self):
        self.T = 0
        self.userTweets = {} # userId -> (t, tweetId)
        self.userFollow = {} # userId -> set(...)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.T += 1
        if userId in self.userTweets:
            self.userTweets[userId].append((-self.T, tweetId))
        else:
            self.userTweets[userId] = [(-self.T, tweetId)]


    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        if userId in self.userTweets:
            tweets.extend(self.userTweets[userId])

        if userId in self.userFollow:
            for i in list(self.userFollow[userId]):
                if i in self.userTweets:
                    tweets.extend(self.userTweets[i])

        heapq.heapify(tweets)
        ret = []
        for i in range(min(10, len(tweets))):
            top = heapq.heappop(tweets)
            ret.append(top[1])

        return ret


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.userFollow:
                self.userFollow[followerId].add(followeeId)
            else:
                self.userFollow[followerId] = set([followeeId])


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId and followerId in self.userFollow:
            self.userFollow[followerId].discard(followeeId)