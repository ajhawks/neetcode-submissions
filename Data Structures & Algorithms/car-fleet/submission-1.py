class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        for i in range(len(position)):
            d[position[i]] = speed[i]
        ds = dict(sorted(d.items(), reverse = True))

        t = 0
        count = 0

        for i in ds: 
            if (target - i) /  ds[i] > t:
                t = (target - i) /  ds[i]
                count += 1
        return count

        