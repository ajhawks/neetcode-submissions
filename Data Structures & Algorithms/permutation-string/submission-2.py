class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        dict2 = {}
        l = 0
        r = len(s1)-1
        checker = False
        for i in s1:
            dict1[i] = dict1.get(i, 0) + 1
            dict2[i] = 0
        for i in s2[l:r+1]:
            if i in dict1:
                dict2[i] = dict2[i] + 1
        for i in dict1:
            if dict1[i] > dict2[i]:
                checker = True
        if checker == False: return True
        while r < len(s2) - 1:
            checker = False
            if s2[l] in dict1:
                dict2[s2[l]] = dict2.get(s2[l]) - 1
            if s2[r+1] in dict1:
                dict2[s2[r+1]] = dict2.get(s2[r+1]) + 1
            for i in dict1:
                if dict1[i] > dict2[i]:
                    checker = True
            if checker == False: return True
            l += 1
            r += 1
        return False
