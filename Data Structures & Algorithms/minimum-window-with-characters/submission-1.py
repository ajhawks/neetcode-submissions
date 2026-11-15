
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        l = 0
        r = 0
        d1 = {}
        d2 = {}
        counter = 0
        length = float('inf')
        res = ""

        for i in t:
            d1[i] = d1.get(i, 0) + 1
            d2[i] = 0

        while r < len(s):
            # Expand window
            if s[r] in d1:
                d2[s[r]] += 1

                if d2[s[r]] == d1[s[r]]:
                    counter += 1

            # Shrink window when valid
            while counter == len(d1):
                if r - l + 1 < length:
                    res = s[l:r+1]
                    length = r - l + 1

                if s[l] in d1:
                    if d2[s[l]] == d1[s[l]]:
                        counter -= 1

                    d2[s[l]] -= 1

                l += 1

            r += 1

        return res
