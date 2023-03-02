class StockPrice:

	def __init__(self):
		self.maxPriceHeap = []
		self.minPriceHeap = []
		self.latestPrices = {} 

		# [timestamp, price]
		self.latestPrice = [0, 0] 

	def update(self, timestamp: int, price: int) -> None:
		if timestamp >= self.latestPrice[0]:
			self.latestPrice = [timestamp, price]

		self.latestPrices[timestamp] = price 
		heapq.heappush(self.maxPriceHeap, (price*-1, timestamp))
		heapq.heappush(self.minPriceHeap, (price, timestamp))

	def current(self) -> int:
		return self.latestPrice[1] 

	def maximum(self) -> int:
		# while the price at top doesn't match what its latest timestamp is, pop from heap
		while self.maxPriceHeap[0][0]*-1 != self.latestPrices[self.maxPriceHeap[0][1]]:
			heapq.heappop(self.maxPriceHeap)

		return self.maxPriceHeap[0][0]*-1

	def minimum(self) -> int:
		# while the price at top doesn't match what its latest timestamp is, pop from heap
		while self.minPriceHeap[0][0] != self.latestPrices[self.minPriceHeap[0][1]]:
			heapq.heappop(self.minPriceHeap)

		return self.minPriceHeap[0][0]