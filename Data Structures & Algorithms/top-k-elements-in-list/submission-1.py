class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        database = defaultdict(list)

        for i in nums:
            database[i] = 1 + database.get(i, 0)

        final = dict(sorted(database.items(), key=lambda item: item[1], reverse=True))
        return list(final.keys())[:k]