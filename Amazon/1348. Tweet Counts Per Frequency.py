class TweetCounts:

    def __init__(self):
        self.a = collections.defaultdict(list)
        self.dic = { 'minute': 60, 'hour':60*60, 'day':60*60*24}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.a[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, start: int, end: int) -> List[int]:
        cur = 0
        N = ((end -start)//self.dic[freq])+1
        lst = [0]*N
        for i in self.a[tweetName]:
            if i < start or i > end: continue
            lst[(i-start)//self.dic[freq]]+=1
        return lst