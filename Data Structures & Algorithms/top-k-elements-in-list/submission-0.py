class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        database = defaultdict(list)
        for i in nums:
            if database.get(i) == None:
                database[i] = 1
            else:
                database[i] = database[i] + 1
        final = dict(sorted(database.items(), key=lambda item: item[1], reverse=True))
        return list(final.keys())[:k]