from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        o = ['(', '{', '[']
        c = [')', '}', ']']

        pq = []

        for i in s:
            if i in o:
                pq.append(c[o.index(i)])
            if i in c:
                if pq == []:
                    return False
                if i != pq.pop():
                    return False
        if pq != []:
            return False
        return True

        