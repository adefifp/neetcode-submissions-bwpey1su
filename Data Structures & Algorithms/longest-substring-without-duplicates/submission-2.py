class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        track = set()
        while r < len(s):
            while s[r] in track:
                track.remove(s[l])
                l+=1
            track.add(s[r])
            ans = max(ans, len(track))
            r += 1
        return ans