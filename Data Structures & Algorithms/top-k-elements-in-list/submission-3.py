class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        database = defaultdict(list)

        for i in nums:
            database[i] = 1 + database.get(i, 0)

        sorting = []

        arr = []
        for num, cnt in database.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res