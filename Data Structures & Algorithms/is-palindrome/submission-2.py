class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer1 = 0
        pointer2 = len(s) - 1
        while pointer1 < pointer2:
            first = s[pointer1]
            last = s[pointer2]
            if not first.isalnum():
                pointer1 += 1
                continue
            if not last.isalnum():
                pointer2 -= 1
                continue
            if first.lower() != last.lower():
                return False
            pointer1 += 1
            pointer2 -= 1
        return True