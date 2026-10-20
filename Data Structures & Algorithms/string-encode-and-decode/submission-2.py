class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = ""
        for i in strs:
            length = len(i)
            str2 = f"%{str(length)}#{i}"
            str1 += str2
        return str1
    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            pointer1 = s.index("%")
            pointer2 = s.index("#")
            length = int(s[pointer1 + 1:pointer2])
            word = s[pointer2 + 1:pointer2 + length + 1]
            res.append(word)
            s = s[pointer2 + length + 1:]
        return res