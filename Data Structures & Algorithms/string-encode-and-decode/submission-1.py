class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += (str(len(s)) + "#" + s)

        return ret

    def decode(self, s: str) -> List[str]:
        i = 0
        ret = []
        lenstr = ""
        while(i < len(s)):
            if s[i] == "#":
                strlen = int(lenstr)
                ret.append(s[i + 1 : i + strlen + 1])
                i = i + strlen + 1
                lenstr = ""
            else:
                lenstr += s[i]
                i += 1

        return ret

