class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            track[key].append(word)
        return list(track.values())
        

