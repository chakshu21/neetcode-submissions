class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            encode += str(len(i))+"#"+i
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        i =0
        while i < len(s):
            j=i
            while s[j] != '#':
                j += 1
            lenght = int(s[i:j])
            i = j + 1
            j = i + lenght
            decode.append(s[i:j])
            i = j
        return decode
