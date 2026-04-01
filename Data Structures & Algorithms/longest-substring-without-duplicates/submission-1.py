class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        track = set()
        ans = 0
        while r < len(s):
            if s[r] in track:
                while s[r] in track:
                    track.remove(s[l])
                    l += 1
            track.add(s[r])
            if len(track) > ans:
                ans = len(track)
            r += 1
        return ans
            