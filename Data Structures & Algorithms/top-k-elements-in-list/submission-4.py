class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        database = defaultdict(list)

        for i in nums:
            database[i] = 1 + database.get(i, 0)

        heap = []

        for num in database.keys():
            heapq.heappush(heap, (database[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

        