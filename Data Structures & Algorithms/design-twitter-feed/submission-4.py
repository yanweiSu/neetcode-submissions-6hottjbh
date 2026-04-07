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
        src = set([userId])
        if userId in self.userFollow:
            src = src.union(self.userFollow[userId])

        query = []
        for followId in list(src):
            if followId in self.userTweets:
                tmp = self.userTweets[followId][-1]
                tmp += (followId, len(self.userTweets[followId]) - 1)
                query.append(tmp)

        heapq.heapify(query)
        ret = []
        while query and (len(ret) < 10):
            top = heapq.heappop(query)
            ret.append(top[1])

            tweet_idx = top[3] - 1
            followId = top[2]
            if tweet_idx >= 0:
                new_tweet = self.userTweets[followId][tweet_idx]
                new_tweet += (followId, tweet_idx)
                heapq.heappush(query, new_tweet)

        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollow:
            self.userFollow[followerId].add(followeeId)
        else:
            self.userFollow[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollow:
            return
        if followerId == followeeId:
            return
        self.userFollow[followerId].discard(followeeId)