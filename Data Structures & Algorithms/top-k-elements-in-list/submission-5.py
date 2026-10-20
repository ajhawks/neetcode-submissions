class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        database = defaultdict(list)
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            database[i] = 1 + database.get(i, 0)

        for num, cnt in database.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


        