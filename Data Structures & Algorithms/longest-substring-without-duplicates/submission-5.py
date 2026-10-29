class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict()
        biggest = 0
        length = 0
        for i in range(len(s)):
            x = d.get(s[i])
            if x != None:
                length = min(i - x, length + 1)
                d[s[i]] = i
            else:
                d[s[i]] = i
                length += 1
            biggest = max(length, biggest)
        return biggest
