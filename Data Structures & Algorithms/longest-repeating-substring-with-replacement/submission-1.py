class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        track = {}
        l = 0
        r = 0
        ans = 0
        highestChar = 0
        while r < len(s):
            track[s[r]] = track.get(s[r], 0) + 1
            highestChar = max(highestChar, track[s[r]])
            while (r - l + 1) - highestChar > k:
                track[s[l]] -= 1
                highestChar = max(highestChar, track[s[l]])
                l += 1
            ans = max((r - l) + 1, ans)
            r += 1
        return ans