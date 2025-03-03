class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for i in strs:
            s = ''.join(sorted(i))
            if s not in dict:
                dict[s]=[i]
            else:
                dict[s].append(i)
        return list(dict.values())

            
        