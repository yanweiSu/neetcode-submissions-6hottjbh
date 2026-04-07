class Twitter:

    def __init__(self):
        self.T = 0
        self.allUserTweets = {}
        self.allFollowees = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.T += 1
        if userId in self.allUserTweets:
            self.allUserTweets[userId].append((-self.T, tweetId))
        else:
            self.allUserTweets[userId] = [(-self.T, tweetId)]

        if userId not in self.allFollowees:
            self.allFollowees[userId] = set([userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        alltweets = []
        for followeeId in list(self.allFollowees[userId]):
            alltweets.extend(self.allUserTweets[followeeId])

        heapq.heapify(alltweets)
        ret = []
        for i in range(min(10, len(alltweets))):
            top = heapq.heappop(alltweets)
            ret.append(top[1])

        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.allFollowees:
            self.allFollowees[followerId].add(followeeId)
        else:
            self.allFollowees[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.allFollowees[followerId].discard(followeeId)
        
