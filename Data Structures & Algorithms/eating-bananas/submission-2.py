class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            rate = (l + r) // 2
            time = 0
            for i in piles:
                time += -(-i // rate)
            
            if time == h:
                r = rate
            elif time < h:
                r = rate
            elif time > h:
                l = rate + 1 
        return l
        