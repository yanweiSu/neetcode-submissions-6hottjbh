class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord('a')] += 1

            key = tuple(key)

            if key in result:
                result[key].append(s)
            else:
                result[key] = [s]

        return list(result.values())


        
