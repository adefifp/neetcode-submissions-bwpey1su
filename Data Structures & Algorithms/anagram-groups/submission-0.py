class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key not in track:
                track[key] = []
            track[key].append(string)
        return list(track.values()) 