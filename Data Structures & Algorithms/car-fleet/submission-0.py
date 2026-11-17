class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        for i in range(len(position)):
            d[position[i]] = speed[i]
        ds = dict(sorted(d.items(), reverse = True))

        t = []

        for i in ds: 
            if not t:
                t.append((target - i) /  ds[i]) 
            elif (target - i) /  ds[i] > t[-1]:
                t.append((target - i) /  ds[i]) 
        return len(t)

        