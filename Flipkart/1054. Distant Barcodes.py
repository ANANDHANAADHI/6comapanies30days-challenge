def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
	barcodes = collections.Counter(barcodes)
	heap = []
	res = []

	for b in barcodes:
		heapq.heappush(heap, (-barcodes[b], b))

	while heap:
		a = heapq.heappop(heap)
		res.append(a[1])
		if heap:
			b = heapq.heappop(heap)
			res.append(b[1])
			if abs(b[0])>1:
				heapq.heappush(heap, (-(abs(b[0])-1), b[1]))
		if abs(a[0])>1:
				heapq.heappush(heap, (-(abs(a[0])-1), a[1]))

	return res